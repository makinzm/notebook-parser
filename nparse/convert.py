import nbformat


def join_cells(cells: list, cell_type: str):
    output = ""
    num_pages = len(cells)
    for i, cell in enumerate(cells):
        _page = str(i + 1) + "/" + str(num_pages)
        if cell_type == "code":
            _code_note = "\n# date_reading: \n# thought: \n# words: \n# reference: \n"
            _num = 20
            _middle = "#\t" + _page
            _edge = "#" * _num
            output += "\n\n" + _edge + "\n" + _middle + _code_note + "\n" + _edge + "\n\n"
            
        elif cell_type == "markdown":
            _markdown_note = "\n<br>\ndate_reading:\n<br>\nthought:\n<br>\nwords:\n<br>\nreference:<hr>"
            output += "\n\n<hr>\n" + _page + _markdown_note + "\n<hr>\n\n"
        else: # pragma: no cover
            pass
        output += cell.strip() + "\n\n"
    return output.strip()


def convert_notebook(notebook_path: str):
    """Convert notebook to markdown and python file.

    Args:
        notebook_path (str): Notebook Path
    """
    prefix = notebook_path.split(".")[0]

    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    code_cells = []
    markdown_cells = []
    for cell in nb.cells:
        if cell.cell_type == "code":
            code_cells.append(cell.source)
            # Shoud we add more option such as cell.outputs
            # https://nbformat.readthedocs.io/en/latest/format_description.html
        elif cell.cell_type == "markdown":
            markdown_cells.append(cell.source)
        else: # pragma: no cover
            pass

    with open(f"{prefix}.py", "w") as f:
        f.write(join_cells(code_cells, "code"))
    print(f"Overwrite: {prefix}.py")
    with open(f"{prefix}.md", "w") as f:
        f.write(join_cells(markdown_cells, "markdown"))
    print(f"Overwrite: {prefix}.md")


if __name__ == "__main__":# pragma: no cover
    path: str = input("Please input notebook_path: ")
    count_dot: int = path.count(".")
    if count_dot != 1:
        print(f"Path should include only one dot. : {path}")
    else:
        ipynb: str = path.split(".")[1]
        if ipynb != "ipynb":
            print(f"Path should be notebook. : {path}")
        else:
            try:
                convert_notebook(path)
            except FileNotFoundError as ex:
                print(ex)
