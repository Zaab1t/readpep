"""
    readpep
    ~~~~~~~
    
    Quickly read a pep when someone reference it by number :)

    Example usage:
        $ readpep 257
"""

import sys
import pydoc

import requests


URL_TEMPLATE = 'https://raw.githubusercontent.com/python/peps/master/pep-%s.'


if __name__ == '__main__':
    try:
        formatted_name = str(int(sys.argv[1])).rjust(4, '0')
    except (IndexError, ValueError):
        print("Usage:   readpep PEP\nExample: readpep 20")
        sys.exit(1)
    r = requests.get(URL_TEMPLATE % formatted_name + 'txt')
    if r.status_code == 404:
        r = requests.get(URL_TEMPLATE % formatted_name + 'rst')
    if r.status_code == 404:
        print('Pep %s not found.' % formatted_name)
        sys.exit(2)
    pydoc.pager(r.text)
