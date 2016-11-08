###Dependency: 

prettytable, docopt, requests

<code>pip install prettytable docopt requests</code>

###Personal Progress:
####1.docopt usage:

<code>ticket [-gdztk] \<from_station\> \<to_station\> [\<train_date\>]</code>

run python file with param just like linux command and get args as:

<code>ticket -gd 北京 上海 2016-11-08</code>

```python
args = docopt(__doc__, version='Ticket Query 1.0')
'''
args will be:

{
  '--help': False,
  '--version': False,
  '-d': True,
  '-g': True,
  '-k': False,
  '-t': False,
  '-z': False,
  '<from_station>': '北京',
  '<to_station>': '上海',
  '<train_date>': '2016-11-08'
}
```
####2,color 
using format:

'\033[(method);(front-color);(backgroud)m(your text)\033[0m'

```
'\033[91mtest content\033[0m'

method:
  reset='\033[0m'
  bold='\033[01m'
  disable='\033[02m'
  underline='\033[04m'
  reverse='\033[07m'
  strikethrough='\033[09m'
  invisible='\033[08m'
  
front-color:
  black='\033[30m'
  red='\033[31m'
  green='\033[32m'
  orange='\033[33m'
  blue='\033[34m'
  purple='\033[35m'
  cyan='\033[36m'
  lightgrey='\033[37m'
  darkgrey='\033[90m'
  lightred='\033[91m'
  lightgreen='\033[92m'
  yellow='\033[93m'
  lightblue='\033[94m'
  pink='\033[95m'
  lightcyan='\033[96m'

backgroud:
  black='\033[40m'
  red='\033[41m'
  green='\033[42m'
  orange='\033[43m'
  blue='\033[44m'
  purple='\033[45m'
  cyan='\033[46m'
  lightgrey='\033[47m' 
```
