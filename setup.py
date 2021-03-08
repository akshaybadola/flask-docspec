#!/usr/bin/env python3

import os
from setuptools import setup
from flask_docspec.version import __version__


os.environ.update({"SKIP_CYTHON": "1"})
description = """Flask Doc OpenAPI Specification.
Generate OpenAPI specifications from python docstrings of the endpoints."""

with open("README.md") as f:
    long_description = f.read()

setup(
    name="flask-docspec",
    version=__version__,
    description=description,
    long_description=long_description,
    url="https://github.com/akshaybadola/flask-docspec",
    author="Akshay Badola",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Documentation",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Software Development :: Documentation",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Natural Language :: English",
    ],
    packages=["flask_docspec"],
    include_package_data=True,
    keywords='documentation openapi',
    python_requires=">=3.7, <=3.9",
    install_requires=["pockets==0.9.1",
                      "six==1.15.0",
                      "Flask==1.1.2",
                      "sphinx==3.5.1",
                      "pydantic @ git+https://github.com/akshaybadola/pydantic.git@master"]
)
