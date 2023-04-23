import setuptools

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "readme.md").read_text()

setuptools.setup(
    name="nparse",
    version="0.0.16",
    description="Notebook Parser for kaggler especially for english-learner",
    long_description=long_description,
    author="Nozomi Maki",
    url="https://github.com/makinzm/notebook-parser",
    license="MIT License",
    install_requires=["nbformat"],
    packages = ["nparse"],
    entry_points={
        'console_scripts': [
            'nparse = nparse.main:main',
        ]
    }
)
