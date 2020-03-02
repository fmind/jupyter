#!/usr/bin/env python3

import os

print(
    'Created environment: ide ->',
    os.system('conda env create -f conda.yaml --force')
)