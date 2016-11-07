#!/home/alex/local/python_evns/web_env/bin/python
# -*- coding=utf-8 -*-


"""Naval Fate.

Usage:
  docc.py [-gdztk] <from_station> <to_station> <train_date>
  docc.py (-h | --help)
  docc.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  -g            高铁.
  -d            动车.
  -z            直达.
  -t            特快.
  -k            快客.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')

    print('in')


    print(arguments)