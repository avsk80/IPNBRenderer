from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()
    
__VERSION__ = "0.0.1"

REPO_NAME = "IPNBRenderer"
AUTHOR_NAME = "avsk80"
AUTHOR_EMAIL = "avskkrish80@gmail.com"

setup(
    name=REPO_NAME,
    version=__VERSION__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for rendering ipynb files",
    long_description=long_description,
    long_description_content ="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    packages=find_packages(
                where="src",
                include=["IPNBRenderer","IPNBRenderer.*"]),
    license="MIT",
    package_dir={"": "src"}
)