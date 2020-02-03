#!/usr/bin/env python3

import os

extensions = [
    '@aquirdturtle/collapsible_headings',
    '@jupyter-widgets/jupyterlab-manager',
    '@jupyterlab/celltags',
    '@jupyterlab/shortcutui',
    '@jupyterlab/toc',
    '@krassowski/jupyterlab-lsp',
    '@krassowski/jupyterlab_go_to_definition',
    '@lckr/jupyterlab_variableinspector',
    '@parente/jupyterlab-quickopen',
    '@ryantam626/jupyterlab_code_formatter',
    'jupyterlab-jupytext',
    'jupyterlab-topbar-extension',
    'jupyterlab_vim',
]

def install(extension):
    return os.system(f'jupyter labextension install {extension}')


if __name__ == "__main__":
    for extension in extensions:
        code = install(extension)
        print(code, extension)
