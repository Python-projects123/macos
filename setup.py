#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup configuration for the macos package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="macos",
    version="0.1.0",
    author="Python-projects123",
    author_email="author@example.com",
    description="A Python package for macOS utilities and tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Python-projects123/macos",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: MacOS",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "black>=22.0",
            "flake8>=4.0",
            "isort>=5.0",
            "mypy>=0.950",
            "pylint>=2.12",
            "pre-commit>=2.15",
        ],
        "docs": [
            "sphinx>=4.5",
            "sphinx-rtd-theme>=1.0",
            "sphinx-autodoc-typehints>=1.12",
        ],
        "test": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "pytest-xdist>=2.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "macos-cli=macos.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="macos macos-x osx utilities",
    project_urls={
        "Bug Reports": "https://github.com/Python-projects123/macos/issues",
        "Documentation": "https://github.com/Python-projects123/macos#readme",
        "Source Code": "https://github.com/Python-projects123/macos",
    },
)
