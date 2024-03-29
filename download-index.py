#!/usr/bin/env python3

import argparse
import json
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('index')
parser.add_argument('data_dir')
args = parser.parse_args()

with open(args.index) as index_file:
    index = json.load(index_file)
    for metadata in index:
        link = metadata.get('links')[0]
        print(f'Downloading {link}')
        subprocess.run(['wget', '--directory-prefix', args.data_dir, link])

