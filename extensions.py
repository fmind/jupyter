#!/usr/bin/env python3

import os

EXTENSIONS = [
    'qgrid2',
    '@jupyterlab/git',
    '@jupyterlab/toc',
    'nbdime-jupyterlab',
    'jupyterlab_filetree',
    'jupyterlab-jupytext',
    '@jupyterlab/celltags',
    '@parente/jupyterlab-quickopen',
    '@ijmbarr/jupyterlab_spellchecker',
    '@lckr/jupyterlab_variableinspector',
    '@jupyter-widgets/jupyterlab-manager',
    '@ryantam626/jupyterlab_code_formatter',
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
