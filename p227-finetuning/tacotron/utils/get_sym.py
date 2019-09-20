f = open("../../LJSpeech-1.1/metadata.txt","r")
con = f.readlines()
f.close()

sym = []
for i in range(len(con)):
	tmp = con[i].split("|")[1]
	for w in tmp:
		if w not in sym:
			sym.append(w)
sym.remove("\n")
print("".join(sym))
