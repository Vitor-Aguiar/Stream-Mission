# Criada uma lista com todos os hashs da wordlist e gravada em 'hashs.txt'

import md5
import itertools


hash = '76fb930fd0dbc6cba6cf5bd85005a92a'

entrada = open('hashs.txt').readlines()

entrada2 = open('hashs.txt').readlines()

val = 0

for k,i in enumerate(entrada):
	hash1 = i.split(' ')[0].strip()
	hash2 = int(hash1,16) ^ int(hash,16)
	#print i.split(' ')[0].strip()
	#print str(hex(hash2))[2:-1]
	for j in entrada2:
		if str(hex(hash2))[2:-1] in j:
			print i.split(' ')[1].strip()+":"+j.split(' ')[1].strip()
			val = 1
			break
	if val == 1:
		break
