#!/usr/bin/python

import urllib
import json
from termcolor import colored

def main():
	makeBanner("IPLocator")
	IP = raw_input("\n"+colored("Enter your IP: ","green"))
	link = "http://ip-api.com/json/" + str(IP)
	response = urllib.urlopen(link)
	data = json.loads(response.read())
	print "\n["+colored("+","green")+"] Status : "+data["status"]
	print "["+colored("+","green")+"] City : "+data["city"]
	print "["+colored("+","green")+"] Zip : "+data["zip"]
	print "["+colored("+","green")+"] CountryCode : "+data["countryCode"]
	print "["+colored("+","green")+"] Country : "+data["country"]
	print "["+colored("+","green")+"] Region : "+data["region"]
	print "["+colored("+","green")+"] Internet Service Provider : "+data["isp"]
	print "["+colored("+","green")+"] Timezone : "+data["timezone"]
	print "["+colored("+","green")+"] as : "+data["as"]
	print "["+colored("+","green")+"] Query : "+data["query"]
	print "["+colored("+","green")+"] Coordinates : "+str(data["lat"])+","+str(data["lon"])
	print "["+colored("+","green")+"] Organisation : "+data["org"]
	print "["+colored("+","green")+"] Region Name : "+data["regionName"]
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
