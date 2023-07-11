print("harf bulma programına hoşgeldiniz")

metin = input("bir metin giriniz : ")

dizi =[]
for i in metin:
    if not(i in dizi) and i != " ":
        dizi.append(i)
print(dizi)

dizi2=[]

for i in dizi:
    syc=0
    for j in metin:
        if i==j:
            syc +=1
    dizi2.append(syc)

for i in range(0,len(dizi)):
    print("{}'den {} adet var".format(dizi[i],dizi2[i]))
