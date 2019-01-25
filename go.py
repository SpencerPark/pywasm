import os
import pathlib
import subprocess
import sys


def call(command):
    print(command)
    r = subprocess.call(command, shell=True)
    if r != 0:
        sys.exit(r)


def test():
    f = pathlib.Path('./tests/test_spec.py')
    if os.name == 'nt':
        call(f'python {f}')
    else:
        call(f'python3 {f}')


def main():
    test()


if __name__ == '__main__':
    main()
