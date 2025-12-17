#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup configuration for macOS Emulator Package
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Core dependencies
install_requires = [
    'psutil>=5.9.0',
    'pyyaml>=6.0',
    'click>=8.0.0',
    'requests>=2.28.0',
    'paramiko>=2.12.0',
    'fabric>=3.0.0',
    'virtualenv>=20.0.0',
]

# Optional dependencies for development and extras
extras_require = {
    'dev': [
        'pytest>=7.0.0',
        'pytest-cov>=4.0.0',
        'pytest-mock>=3.10.0',
        'black>=22.0.0',
        'flake8>=5.0.0',
        'isort>=5.11.0',
        'mypy>=0.990',
        'pylint>=2.15.0',
    ],
    'docs': [
        'sphinx>=5.0.0',
        'sphinx-rtd-theme>=1.0.0',
        'sphinx-autodoc-typehints>=1.19.0',
    ],
    'ui': [
        'PyQt6>=6.0.0',
        'PyQt6-WebEngine>=6.0.0',
    ],
    'networking': [
        'scapy>=2.5.0',
        'netifaces>=0.11.0',
    ],
    'monitoring': [
        'prometheus-client>=0.15.0',
        'datadog>=0.44.0',
    ],
}

# Add 'all' extra that includes all optional dependencies
extras_require['all'] = sum(extras_require.values(), [])

setup(
    name='macos-emulator',
    version='1.0.0',
    description='A comprehensive macOS emulator and virtualization package for system testing and development',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Python Projects',
    author_email='contact@python-projects123.com',
    url='https://github.com/Python-projects123/macos',
    project_urls={
        'Documentation': 'https://github.com/Python-projects123/macos/wiki',
        'Source Code': 'https://github.com/Python-projects123/macos',
        'Issue Tracker': 'https://github.com/Python-projects123/macos/issues',
        'Changelog': 'https://github.com/Python-projects123/macos/releases',
    },
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.8',
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'macos-emulator=macos_emulator.cli:main',
            'macos-vm=macos_emulator.cli:vm_command',
            'macos-config=macos_emulator.cli:config_command',
            'macos-monitor=macos_emulator.cli:monitor_command',
            'macos-network=macos_emulator.cli:network_command',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: System :: Emulators',
        'Topic :: System :: Monitoring',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    keywords=[
        'macos',
        'emulator',
        'virtualization',
        'vm',
        'simulator',
        'testing',
        'development',
    ],
    include_package_data=True,
    zip_safe=False,
    platforms=[
        'Darwin',
        'Linux',
        'Windows',
    ],
)
