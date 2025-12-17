from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="macosemu",
    version="1.0.0",
    author="Python-projects123",
    description="A macOS emulation and system utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Python-projects123/macos",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: System :: Emulators",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "pyyaml>=6.0",
        "requests>=2.28.0",
        "psutil>=5.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
        "docs": [
            "sphinx>=4.5.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "macosemu=macosemu.cli:main",
        ],
    },
    keywords="macos emulation system utilities",
    project_urls={
        "Bug Reports": "https://github.com/Python-projects123/macos/issues",
        "Source": "https://github.com/Python-projects123/macos",
        "Documentation": "https://github.com/Python-projects123/macos/blob/main/README.md",
    },
    zip_safe=False,
    include_package_data=True,
)
