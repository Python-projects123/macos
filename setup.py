#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup configuration for macOS Emulator package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="macos-emulator",
    version="0.1.0",
    author="Python-projects123",
    author_email="",
    description="A macOS emulator for system simulation and testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Python-projects123/macos",
    project_urls={
        "Bug Tracker": "https://github.com/Python-projects123/macos/issues",
        "Documentation": "https://github.com/Python-projects123/macos/wiki",
        "Source Code": "https://github.com/Python-projects123/macos",
    },
    packages=find_packages(where="src", exclude=["tests*", "docs*"]),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[
        "setuptools>=45.0",
        "wheel>=0.36.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.10",
            "black>=21.0",
            "flake8>=3.9",
            "isort>=5.9",
            "mypy>=0.900",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "macos-emulator=macos_emulator.cli:main",
            "macos-emu=macos_emulator.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Emulators",
        "Topic :: Utilities",
    ],
    keywords="macos emulator simulator virtualization testing",
    zip_safe=False,
    include_package_data=True,
)
