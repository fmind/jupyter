#!/usr/bin/env python3

import os
import argparse

PACKAGES = [
    'jupytext',
]

EXTENSIONS = [
    '@jupyterlab/toc',
    'jupyterlab-jupytext',
]

parser = argparse.ArgumentParser('extensions.py')
parser.add_argument('--user', action='store_true')


def build_extension() -> int:
    return os.system('jupyter lab build')


def install_extension(extension: str) -> int:
    return os.system(f'jupyter labextension install {extension} --no-build')


def install_package(package: str, user: bool = False) -> int:
    return os.system(f'python -m pip install {"--user" if user else ""} "{package}"')


if __name__ == '__main__':
    args = parser.parse_args()

    for package in PACKAGES:
        print(f'Installing package: {package} {args.user}')
        print(f'-> {install_package(package, args.user)}')

    for extension in EXTENSIONS:
        print(f'Installing extension: {extension}')
        print(f'-> {install_extension(extension)}')

    print(f'Building extension: {len(EXTENSIONS)}')
    print(f'-> {build_extension()}\n\nBuild: DONE')
