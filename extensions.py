#!/usr/bin/env python3

import os

EXTENSIONS = [
    '@jupyterlab/toc',
    'nbdime-jupyterlab',
    'jupyterlab-jupytext',
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