import zipfile
import sys, os
os.system("clear")
m = "\033[91m"
h = "\033[92m"
k = "\033[93m"
os.system("toilet -f slant --metal ZipCrack")
print ""
print "\033[97mTools Bruteforce password zip 2019"
print k
zip = raw_input("Nama File: ")
passfile = raw_input("Wordlist: ")
zfile = zipfile.ZipFile(zip)
os.system("sleep 1")
print h+"Melakukan Cracking..."
print ""
passfile = open(passfile, "r")
for password in passfile.readlines():
	password = password.strip("\n").strip("\r")
	try:
		zfile.extractall(pwd=password)
		print h+("[!]Found > "+password)
		sys.exit()
	except Exception, e:
		print k+("[!]Crack > "+password)
		
