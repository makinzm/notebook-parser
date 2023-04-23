import argparse

from .convert import convert_notebook


def main():  # pragma: no cover
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    arg_parser.add_argument(
        "notebook_path",
        type=str,
        help="path of notebook to read")
    args = arg_parser.parse_args()
    if args.notebook_path != ["notebook_path"]:
        print("Please input notebook_path")
    path = args.notebook_path
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


if __name__ == '__main__':  # pragma: no cover
    main()
