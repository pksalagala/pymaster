#!/usr/bin/python

import sys

from main.__main__ import hello
from main.arrays import printarray


def main():
    print("IN main - {:s}".format(hello()))
    printarray()


if __name__ == '__main__':
    main()


