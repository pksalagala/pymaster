#!/usr/bin/python

import sys
import requests


def main():
	print("IN main - ")
	filepath = 'links.txt'
	with open(filepath) as fp:
		line = fp.readline()
		cnt = 1
		year = 2001   #change year abs month after downloading fwe files
		month = 12;
		while line:
			print("Line {} {}-{}: {}".format(cnt, year, month, line.strip()))
			if(line.strip() != "---"):
				r = requests.get(line.strip(), allow_redirects=True) 
				open("{}-{}.pdf".format(year, month), 'wb').write(r.content)
			if month == 12:
				month = 1
				year = year + 1
			else:
				month = month + 1
			cnt = cnt + 1
			line = fp.readline()
		print("Total {}".format(cnt))
		
if __name__ == '__main__':
	#if len (sys.argv) != 2:
	#	print(sys.argv[0], sys.argv[1], sys.argv[2])
	main()

