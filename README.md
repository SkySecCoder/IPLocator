# IPLocator
Simple tool to look up IP address informtion quickly form the terminal. 

# Installation
```
$ pip install termcolor
$ git clone https://github.com/SkySecCoder/IPLocator.git
```
# Usage
```
Interactive Mode :
./IPLocator.py -i

From Terminal:
./IPLocator.py -a <IP Address 1> <IP Address 2> ..

./IPLocator.py -f <File with IP Addresses> -w <File to write Output>
```

# Help banner
```
usage: IPLocator.py [-h] [-i] [-b] [-f f] [-w w] [-a a [a ...]]

Lookup location of IPaddress.

optional arguments:
  -h, --help            show this help message and exit
  -i                    Prompt for IP address at runtime
  -b, --no-banner       Don't print banner
  -f f                  Read IP addresses from file
  -w w                  Write output to file
  -a a [a ...], --addr a [a ...]
                        IP Address to lookup
```

