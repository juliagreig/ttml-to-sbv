#	1. put this file in with all of your ttml files
#	2. run it
#	3. and now you have all dem h0t h0t .sbv files
#	keep in mind its not a classic .sbv
#	instead of 0:00:25.199,0:00:29.099
#	the timestamp is in the format 00:02:29.67;00:02:31.56
#	this was for my own needs, but you can easily change the ; in line 22 to ,
#
# 	script written by julia greig on apr 3 2017
#	plz enjoy!!

import glob
from bs4 import BeautifulSoup
fullscript = ""
for file in glob.glob("*.xml"):
    with open(file) as infile:
    	soup = BeautifulSoup(infile)
    	for p in soup.find_all('p'):
    		start = p["begin"]
    		end = p["end"]
    		text = p.contents[0].strip()
    		newline = "{};{}\n{}\n".format(start, end, text)
    		fullscript += newline
	newfilename = '{}.sbv'.format(file[:-4])
	new_file = open(newfilename, 'w')
	new_file.write(fullscript)
	new_file.close()