#!/usr/bin/python

import urllib
import json
import sys
import argparse
try:
	from termcolor import colored
except ImportError:
	print '[*] Missing Reqired Libraries'
	sys.exit(1)

def main():
	parser = argparse.ArgumentParser(description='Lookup location of IPaddress.')
	parser.add_argument('-i', dest='interact', action='store_true', help='Prompt for IP address at runtime')
	parser.add_argument('-b','--no-banner', dest='banner', action='store_true', help='Don\'t print banner')
	parser.add_argument('-f', dest='file', metavar='f', type=str, help='Read IP addresses from file')
	parser.add_argument('-w', dest='write', metavar='w' , type=str, help='Write output to file')
	parser.add_argument('-a','--addr', metavar='a', type=str, nargs='+', help='IP Address to lookup')
	args = parser.parse_args()

	if not args.banner:
		makeBanner("IPLocator")

	if args.write is not None:
		out_file = open(args.write,'w')

	IP = []
	if args.interact:
		IP.append(raw_input("\n"+colored("Enter your IP: ","green")))
	if args.file is not None:
		with open(args.file,'r') as fd:
			for line in fd.readlines():
				IP.append(line)
	if args.addr is not None:
		for ad in args.addr:
			IP.append(ad)

	for i in IP:
		link = "http://ip-api.com/json/{0}".format(i)
		response = urllib.urlopen(link)
		data = json.loads(response.read())
		try:
			print "\n["+colored("+","green")+"] Status : "+data["status"]
			if args.write is not None:
				out_file.write("\n\n[+] Status : "+data["status"])
		except KeyError:
			pass
		try:
			print "["+colored("+","green")+"] Query : "+data["query"]
                	if args.write is not None:
                                out_file.write("\n[+] Query : "+data["query"])
		except KeyError:
                        pass
		try:
			print "["+colored("+","green")+"] City : "+data["city"]
			if args.write is not None:
                                out_file.write("\n[+] City : "+data["city"])
		except KeyError:
			pass
		try:
			print "["+colored("+","green")+"] Zip : "+data["zip"]
			if args.write is not None:
                                out_file.write("\n[+] Zip : "+data["zip"])
		except KeyError:
                        pass
		try:
			print "["+colored("+","green")+"] CountryCode : "+data["countryCode"]
			if args.write is not None:
                                out_file.write("\n[+] CountryCode : "+data["countryCode"])
                except KeyError:
                        pass
                try:
			print "["+colored("+","green")+"] Country : "+data["country"]
			if args.write is not None:
                                out_file.write("\n[+] Country : "+data["country"])
                except KeyError:
                        pass
                try:
			print "["+colored("+","green")+"] Region : "+data["region"]
			if args.write is not None:
                                out_file.write("\n[+] Region : "+data["region"])
                except KeyError:
                        pass
                try:
			print "["+colored("+","green")+"] Internet Service Provider : "+data["isp"]
			if args.write is not None:
                                out_file.write("\n[+] Internet Service Provider : "+data["isp"])
                except KeyError:
                        pass
                try:
			print "["+colored("+","green")+"] Timezone : "+data["timezone"]
			if args.write is not None:
                                out_file.write("\n[+] Timezone : "+data["timezone"])
                except KeyError:
                        pass
                try:
			print "["+colored("+","green")+"] as : "+data["as"]
			if args.write is not None:
                                out_file.write("\n[+] as : "+data["as"])
                except KeyError:
                        pass
		try:
			print "["+colored("+","green")+"] Coordinates : "+str(data["lat"])+","+str(data["lon"])
			if args.write is not None:
                                out_file.write("\n[+] Coordinates : "+str(data["lat"])+","+str(data["lon"]))
		except KeyError:
                        pass
		try:
			print "["+colored("+","green")+"] Organisation : "+data["org"]
			if args.write is not None:
                                out_file.write("\n[+] Organisation : "+data["org"])
		except KeyError:
                        pass
		try:
			print "["+colored("+","green")+"] Region Name : "+data["regionName"]
			if args.write is not None:
                                out_file.write("\n[+] Region Name : "+data["regionName"]+"\n")
		except KeyError:
                        pass
	print "\n[*] Exiting..."
	if args.write is not None:
		out_file.close()


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
