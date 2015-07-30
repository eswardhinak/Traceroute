import os
import sys
import subprocess
import urllib.request
import json 
import re

def main():
	address = sys.argv[1]
	command = "traceroute " + address + ">" + "file"
	return_code = subprocess.call(command, shell=True)
	f = open('file', 'r')
	g = open('output', 'w')
	for line in f:
		open_paran_index = line.find('(')
		close_paran_index = line.find(')')
		ip_addr = line[open_paran_index+1:close_paran_index]
		print(open_paran_index, close_paran_index)
		if (open_paran_index == -1 or close_paran_index == -1):
			continue

		print(ip_addr)
		url = "http://freegeoip.net/json/" + ip_addr

		response = ""
		try: 
			response = urllib.request.urlopen(url)			
			if response.getcode() == 200:
				pass
			else:
				print (response.getcode())
		except Exception as inst:
			print (inst)
			sys.exit()

		read_response = response.read()
		str_response = read_response.decode(encoding="utf-8")
		json_data = json.loads(str_response)
		print(json_data['latitude'], json_data['longitude'])
		g.write(json_data['latitude'], json_data['longitude'])
	
	


if __name__ == "__main__": main()