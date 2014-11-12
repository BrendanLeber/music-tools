#!/usr/bin/python
'''
Convert a single flac file to mp3 while preserving metadata.
'''

import argparse

parser = argparse.ArgumentParser(description='Convert flac file to mp3')
    parser.add_argument('--quality', metavar='quality', required=False, help='VBR Quality (0-9)')

