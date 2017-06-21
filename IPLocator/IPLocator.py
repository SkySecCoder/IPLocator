#!/usr/bin/python

import urllib
import json
import argparse
from termcolor import colored

def main():
	parser = argparse.ArgumentParser(description='Lookup location of IPaddress.')
	parser.add_argument('-a','--addr', metavar='a', type=str, nargs='+', help='IP Address to lookup')
	parser.add_argument('-i', dest='interact', action='store_true', help='Prompt for IP address at runtime')
	parser.add_argument('--no-banner',dest='banner',action='store_true', help='Don\'t print banner')
	args = parser.parse_args()

	if not args.banner: 
		makeBanner("IPLocator")
	IP = []
	if args.interact:
		IP.append(raw_input("\n"+colored("Enter your IP: ","green")))
	else:
		for ad in args.addr:
			IP.append(ad)
	for i in IP:
		link = "http://ip-api.com/json/{0}".format(i)
		response = urllib.urlopen(link)
		data = json.loads(response.read())
		try:
			print "\n["+colored("+","green")+"] Status : "+data["status"]
		except KeyError:
			pass
		try:
			print "["+colored("+","green")+"] Query : "+data["query"]
		except KeyError:
                        pass
		try:
			print "["+colored("+","green")+"] City : "+data["city"]
		except KeyError:
			pass
		try:
			print "["+colored("+","green")+"] Zip : "+data["zip"]
		except KeyError:
                        pass
		try:
			print "["+colored("+","green")+"] CountryCode : "+data["countryCode"]
                except KeyError:
                        pass
                try:
			print "["+colored("+","green")+"] Country : "+data["country"]
                except KeyError:
                        pass
                try:
			print "["+colored("+","green")+"] Region : "+data["region"]
                except KeyError:
                        pass
                try:
			print "["+colored("+","green")+"] Internet Service Provider : "+data["isp"]
                except KeyError:
                        pass
                try:
			print "["+colored("+","green")+"] Timezone : "+data["timezone"]
                except KeyError:
                        pass
                try:
			print "["+colored("+","green")+"] as : "+data["as"]
                except KeyError:
                        pass
		try:
			print "["+colored("+","green")+"] Coordinates : "+str(data["lat"])+","+str(data["lon"])
		except KeyError:
                        pass
		try:
			print "["+colored("+","green")+"] Organisation : "+data["org"]
		except KeyError:
                        pass
		try:
			print "["+colored("+","green")+"] Region Name : "+data["regionName"]
		except KeyError:
                        pass
	print "\n[*] Exiting..."

def makeBanner(name):
    i=j=0
    while j!= 15:
        if j==0 or j==14:
            while i != 40:
                if i==0:
                    print "*",
                elif i==39:
                    print "*"
                else:
                    print "=",
                i = i+1
        i = 0
        if j>0 and j<12:
            if j == 7:
                k = 30
            elif j == 6:
                k = 40 - len(name) + 5
            else:
                k = 40
            while i != k:
                if i == 0:
                    print "|",
                elif i == k-1:
                    print "|"
                elif i == k/2 and j == 7:
                    print "- by SkySecCoder     ",
                elif i == k/2 and j == 6:
                    print name,#+"       ",
                else:
                    print " ",
                i = i + 1
        j = j + 1

if __name__=="__main__":
	main()
