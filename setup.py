# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="ofmt",
    version="0.0.1",
    description="wat",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joedrago/ofmt",
    author="Joe Drago",
    author_email="joedrago@gmail.com",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    license="BSD",
    entry_points={"console_scripts": ["ofmt = ofmt.main:main"]},
    install_requires=["cowsay==2.0.3"],
    extras_require={"dev": []},
    dependency_links=[],
)
