
f1 = open('add.txt','r')
f2 = open('new.txt','r')
w = open('raw.dict','w')
d = {}
for line in f1 :
	term = line.strip()
	d[term] = 1
	
for line in f2 :
	term = line.strip()
	d[term] = 1
	
for term in sorted(d.keys()) :
	w.write(term + ' 100 n\n' )
