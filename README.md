# IPLocator
Simple tool to look up IP address informtion quickly form the terminal. 

# Installation
```
$ pip install termcolor
$ git clone https://github.com/chowdaryd/IPLocator.git
```
# Usage
```
Interactive Mode :
python IPLocator.py -i

From Terminal:
python IPLocator.py -a <IP Address 1> <IP Address 2> ..
```

# Help banner
```
usage: IPLocator.py [-h] [-a a [a ...]] [-i] [--no-banner]

Lookup location of IPaddress.

optional arguments:
  -h, --help            show this help message and exit
  -a a [a ...], --addr a [a ...]
                        IP Address to lookup
  -i                    Prompt for IP address at runtime
  --no-banner           Don't print banner
```

