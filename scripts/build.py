import os
import subprocess
import tempfile
from typing import List

import click
import jupytext
from jupytext.compare import compare_notebooks


CONFIG_FILENAME = ".notebooks"


class Notebook:
    def __init__(self, notebook_path: str) -> None:
        self.basename = os.path.splitext(notebook_path)[0]

    @property
    def py(self) -> str:
        return f"{self.basename}.py"

    @property
    def ipynb(self) -> str:
        return f"{self.basename}.ipynb"


def call_jupytext(notebook: Notebook, out_fname: str, to_ipynb: bool) -> None:
    to_fmt = "ipynb" if to_ipynb else "py:percent"
    from_fmt = "py:percent" if to_ipynb else "ipynb"
    args = [
        "jupytext",
        "--to",
        to_fmt,
        "--from",
        from_fmt,
        "--opt",
        "notebook_metadata_filter=-all",
        notebook.py if to_ipynb else notebook.ipynb,
        "-o",
        out_fname,
    ]
    if to_ipynb:
        args.append("--execute")
    subprocess.run(args, check=True)


def get_notebooks(tutorial_dir: str) -> List[Notebook]:
    path = os.path.abspath(tutorial_dir)
    config_path = os.path.join(path, CONFIG_FILENAME)
    if not os.path.isfile(config_path):
        raise ValueError(f"No {CONFIG_FILENAME} config file in {path}")
    with open(config_path, "r") as f:
        notebooks = f.read().splitlines()
    return [Notebook(os.path.join(path, nb)) for nb in notebooks if nb]


def check_notebook(notebook: Notebook) -> None:
    assert os.path.exists(notebook.py), f"No file {notebook.py}"
    notebook_actual = jupytext.read(notebook.ipynb, fmt=dict(extension="ipynb"))
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as f:
        call_jupytext(notebook, f.name, to_ipynb=True)
        notebook_expected = jupytext.read(f.name, fmt=dict(extension="ipynb"))
        compare_notebooks(notebook_actual, notebook_expected)


def build_html_notebook(notebook: Notebook, build_dir: str) -> None:
    assert os.path.exists(notebook.ipynb), f"No file {notebook.ipynb}"
    os.makedirs(build_dir, exist_ok=True)
    args = [
        "jupyter",
        "nbconvert",
        notebook.ipynb,
        "--to",
        "html",
        "--output-dir",
        build_dir,
    ]
    subprocess.run(args, check=True)


def sync_notebook(notebook: Notebook) -> None:
    assert os.path.exists(notebook.py), f"No file {notebook.py}"
    call_jupytext(notebook, notebook.ipynb, to_ipynb=True)


def sync_py(notebook: Notebook) -> None:
    assert os.path.exists(notebook.ipynb), f"No file {notebook.ipynb}"
    call_jupytext(notebook, notebook.py, to_ipynb=False)


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.argument("tutorial_dir")
def test(tutorial_dir: str) -> None:
    for notebook in get_notebooks(tutorial_dir):
        check_notebook(notebook)


@cli.command()
@click.argument("tutorial_dir")
def html(tutorial_dir: str) -> None:
    build_dir = os.path.abspath(os.path.join(tutorial_dir, "..", "build"))
    for notebook in get_notebooks(tutorial_dir):
        build_html_notebook(notebook, build_dir)


@cli.command()
@click.argument("tutorial_dir")
@click.option("--py", is_flag=True)
def sync(tutorial_dir: str, py: bool) -> None:
    for notebook in get_notebooks(tutorial_dir):
        if py:
            sync_py(notebook)
        else:
            sync_notebook(notebook)


if __name__ == "__main__":
    cli()