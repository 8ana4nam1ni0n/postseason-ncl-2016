import hashlib
import whirlpool
import sys


def computeMD5(s):
	md5 = hashlib.md5()
	md5.update(s)
	return md5.hexdigest()

def computeSHA1(s):
	sha1 = hashlib.sha1()
	sha1.update(s)
	return sha1.hexdigest()

def computeWhirlpool(s):
	wp = whirlpool.new(s)
	return wp.hexdigest()

def main():
	MD5_COLLISION = "cc4"
	M1_FOUND = False
	SHA1_COLLISION = "2aa"
	S_FOUND = False
	WHIRLPOOL_COLLISION = "241"
	W_FOUND = False
	MD5_COLLISION_H = "8c1e3"
	M2_FOUND = False
	dumpfile = sys.argv[1]
	with open(dumpfile) as d:
		for w in d.readlines():
			md5 = computeMD5(w.strip('\n'))
			sha1 = computeSHA1(w.strip('\n'))
			wp = computeWhirlpool(w.strip('\n'))
			if md5[:3] == MD5_COLLISION and not M1_FOUND:
				print "1) md5: " + w + " hash: " + md5
				M1_FOUND = True
			elif md5[:5] == MD5_COLLISION_H and not M2_FOUND:
				print "4) md5 h: " + w + " hash: " + md5
				M2_FOUND = True
			elif sha1[:3] == SHA1_COLLISION and not S_FOUND:
				print "2) sha1: " + w + " hash: " + sha1
				S_FOUND = True
			elif wp[:3] == WHIRLPOOL_COLLISION and not W_FOUND:
				print "3) whirlpool: " + w + " hash: " + wp
				W_FOUND = True
			elif M1_FOUND and M2_FOUND and S_FOUND and W_FOUND:
				break
				
	print "Finished"
 

main()
