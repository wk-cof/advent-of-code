import hashlib
m = hashlib.md5()
#myStr = 'abbhdwsy6082117'
myStr = 'abbhdwsy5708769'
counter = 0
m.update(myStr.encode('utf-8'))
md5 = m.digest()
print(md5)
outerCounter = 0


# while (not(md5[0] == 0x00 and md5[1] == 0x00 and md5[2] < 0x10 and outerCounter > 7) ):
# 	m = hashlib.md5()
# 

	# print(counter)

print ('gotcha')
