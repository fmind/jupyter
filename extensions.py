#!/usr/bin/env python3

import os

EXTENSIONS = [
    '@aquirdturtle/collapsible_headings',
    '@ijmbarr/jupyterlab_spellchecker',
    '@jupyter-widgets/jupyterlab-manager',
    '@jupyterlab/celltags',
    '@jupyterlab/git',
    '@jupyterlab/toc',
    '@lckr/jupyterlab_variableinspector',
    '@parente/jupyterlab-quickopen',
    '@ryantam626/jupyterlab_code_formatter',
    'jupyterlab-jupytext',
    'jupyterlab_filetree',
    'nbdime-jupyterlab',
    'qgrid2',
]

if __name__ == '__main__':
    for extension in EXTENSIONS:
        print(
            f'Installed {extension} ->',
            os.system(f'jupyter labextension install --no-build "{extension}"'),
        )
        
    print(
        'Extensions built ->',
        os.system('jupyter lab build')
     )