#!/usr/bin/env python3

import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument('index')
parser.add_argument('data-dir')
args = parser.parse_args()



with open(args.index) as index_file:
    index = json.load(index_file)
    for metadata in index:
        links = metadata.get('links')
        if not links: continue
        for link in links:
            print(link)


