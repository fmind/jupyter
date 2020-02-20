#!/usr/bin/env python3

import os

print(
    'Created environment ->',
    os.system('conda env create -f conda.yaml --force')
)