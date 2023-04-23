import os

import pytest

from nparse.convert import convert_notebook

def test_notebook_conversion():
    # テスト用のNotebookファイルを作成する
    nb_path = 'test_notebook.ipynb'
    with open(nb_path, 'w') as f:
        f.write("""
        {
          "cells": [
            {
              "cell_type": "markdown",
              "metadata": {},
              "source": "# This is a markdown cell"
            },
            {
              "cell_type": "code",
              "execution_count": 1,
              "metadata": {},
              "outputs": [],
              "source": "print(\\\"This is a code cell\\\")"
            }
          ],
          "metadata": {},
          "nbformat": 4,
          "nbformat_minor": 0
        }
        """)

    # Notebookを変換する
    convert_notebook(nb_path)

    # 変換されたファイルが存在することを確認する
    assert os.path.isfile('test_notebook.py')
    assert os.path.isfile('test_notebook.md')

    # 変換されたファイルを読み込んで中身を確認する
    with open('test_notebook.py') as f:
        code_content = f.read()
    with open('test_notebook.md') as f:
        markdown_content = f.read()
    assert code_content == f"""####################
#	1/1
# date_reading: 
# thought: 
# words: 
# reference: 

####################

print(\"This is a code cell\")"""
    assert markdown_content == f"""<hr>
1/1
<br>
date_reading:
<br>
thought:
<br>
words:
<br>
reference:<hr>
<hr>

# This is a markdown cell"""

    # 変換されたファイルを削除する
    os.remove(nb_path)
    os.remove('test_notebook.py')
    os.remove('test_notebook.md')
