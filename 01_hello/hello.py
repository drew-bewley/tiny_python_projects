
# #$!/usr/bin/env python3
"""
Author: DB
Purpose: Say Hello
"""

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n', '--name', metavar='name', default='World',
                        help='Name to Greet')
    return parser.parse_args()


def main():
    """Do the thing"""
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
