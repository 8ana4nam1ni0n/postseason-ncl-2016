password = "NCL-KRBX-"

for i in range(10000):
	tmp = password + "000" + str(i) if i < 10 else password + "00" + str(i) if i < 100 else password + "0" + str(i) if i < 1000 else password + str(i)
	print tmp
