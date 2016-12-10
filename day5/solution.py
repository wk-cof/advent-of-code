import hashlib
m = hashlib.md5()

myStr = 'abbhdwsy'
counter = 0
m.update(myStr.encode('utf-8'))
md5 = m.hexdigest()
outerCounter = 0


while (not(md5[0] == '0' and md5[1] == '0'and md5[2] == '0' and md5[3] == '0' and md5[4] == '0' and outerCounter > 7) ):
	m = hashlib.md5()
	myStr = 'abbhdwsy' + str(counter)
	m.update(myStr.encode('utf-8'))
	md5 = m.hexdigest()
	if (md5[0] == '0' and md5[1] == '0'and md5[2] == '0' and md5[3] == '0' and md5[4] == '0'):
		print(md5)
		outerCounter += 1
	counter += 1

print ('gotcha')
