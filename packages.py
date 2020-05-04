#!/usr/bin/env python3

import os

PACKAGES = [
  'pip',
  'nbdime',
  'nbformat',
  'jupytext',
  'papermill',
  'nbconvert',
  'jupyterlab',
  'nodejs>=13.8',
  'nteract-scrapbook',
]

if __name__ == '__main__':
    for package in PACKAGES:
        print(
            f'Installed {package} ->',
            os.system(f'conda install -y "{package}"'),
        )
        
    print('DONE')
