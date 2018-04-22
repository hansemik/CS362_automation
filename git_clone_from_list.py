import subprocess
import sys
import os
import time
import argparse

parser = argparse.ArgumentParser(description='Process name of input text file.')
parser.add_argument('file',help='text file containing onid in column one and \ngithub usernames in column two')
args = parser.parse_args()

userlist = args.file

with open(userlist) as f:
   for line in f:
      onid,github_username = line.strip().split(",")
      if github_username != '':
	 print("\nCloning for %s\n" % onid)
	 url_seq = ("https://github.com/",github_username,"/CS362-004-S2018")
	 url = ''.join(url_seq).strip()	  

	 if not os.path.exists(onid):
	    os.makedirs(onid)
	   
	 time.sleep(1)
	 os.chdir(onid)

	 clone = subprocess.Popen(["git","clone", url])
	 time.sleep(1)
		   
	 branch_seq = (onid,"-assignment-2")
	 branch = ''.join(branch_seq).strip()
	 time.sleep(1)
	 try:
	    os.chdir('CS362-004-S2018')
	    checkout = subprocess.Popen(["git","checkout", branch])
	    time.sleep(1)

	    try:
	       dom_seq = ['projects/',onid,'/dominion']
	       os.chdir(''.join(dom_seq))
	       time.sleep(1)

	       make_clean = subprocess.Popen(["make","clean",])
	       make_all = subprocess.Popen(["make","all"])
	       os.chdir('../../../')
            except:
	       print('Make failed for %s' % onid)
	    
	    os.chdir('../../')
	 except:
	    print ('Change dir to CS362-004-S2018 failed...')
	    os.chdir('../')
