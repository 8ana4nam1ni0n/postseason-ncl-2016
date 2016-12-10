import subprocess
import time

filename = "lol"
ext = ".txt"
filecounter = 0

command = "base64 -d "

while True:
	currentfile = filename + ext if filecounter == 0 else filename + str(filecounter) + ext
	nextfile = filename + str(filecounter + 1) + ext
	execute = subprocess.Popen(command + currentfile + " > " + nextfile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output, err = execute.communicate()
	if len(err) > 0:
		print err
		print "Can't decode anymore check file " + currentfile
		break
	else:
		filecounter += 1
