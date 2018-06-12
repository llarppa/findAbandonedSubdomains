#!/usr/bin/python

from urllib import request
from urllib import parse
from urllib import error
import argparse
import fileinput

def findAbandoned():
    parser = argparse.ArgumentParser('asdf')
    parser.add_argument('list of input', help='give a list of subdomains to check')
    args = parser.parse_args()._get_kwargs()
    domains = openFile(args)

    for sub in domains:
        print("********")
        try:
            with request.urlopen(sub) as response:
                print(sub + "Response 200, site is available")
        except error.HTTPError as e:
                    print(sub + "HTTP error! Check the error code! " + str(e.code))
        except error.URLError as e:
                    print(sub + "Invalid URL")

def openFile(parserInput):
    for _, subdomain in parserInput:
        with open(subdomain) as content:
            subdomains = []
            for c in content:
                c.replace("\n", "")
                subdomains.append(c)
            return subdomains

if __name__ == "__main__":
    findAbandoned()
