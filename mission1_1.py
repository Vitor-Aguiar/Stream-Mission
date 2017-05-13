# Wordlist from https://github.com/dwyl/english-words
# Filtrada apenas as palavras com tamanho 8 e gravadas em 'apenas8.txt'

import md5
import itertools


hash = '76fb930fd0dbc6cba6cf5bd85005a92a'

entrada = open('apenas8.txt').readlines()

for i in itertools.combinations(entrada,2):
	palavra1 = i[0].strip()
	palavra2 = i[1].strip()
	hash1 = md5.new()
	hash1.update(palavra1)
	hash1hex = int(hash1.hexdigest(),16)
	hash2 = md5.new()
        hash2.update(palavra2)
        hash2hex = int(hash2.hexdigest(),16)

	hashfinal = hash1hex ^ hash2hex
	#print "Palavras tentadas: %s  %s  %s"%(palavra1,palavra2,str(hex(hashfinal))[2:-1])

	if str(hex(hashfinal))[2:-1] == hash:
		print palavra1+":"+palavra2
		break
