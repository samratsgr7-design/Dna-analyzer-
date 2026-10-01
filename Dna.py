
dna = input("Enter DNA: ").upper()
print(f"Length: {len(dna)}")
print(f"A:{dna.count('A')} T:{dna.count('T')} G:{dna.count('G')} C:{dna.count('C')}")
gc = (dna.count('G')+dna.count('C'))/len(dna)*100
print(f"GC%: {gc:.2f}%")
comp = dna.translate(str.maketrans("ATGC","TACG"))[::-1]
print(f"Reverse Complement: {comp}")
rna = dna.replace('T','U')
print(f"RNA: {rna}")
