sayi = [1,2,3,4,5,6,7,8,9]

value = int(input("hedef sayiyi giriniz : "))

for i in range(len(sayi)):
    if value == sayi[i]:
        print("{} buna eşittir".format(sayi[i]))
    for n in range(len(sayi)):
        if value == sayi[i]+sayi[n]:
            print("{} {} toplamına eşittir".format(sayi[i],sayi[n]))
        for j in range(len(sayi)):
            if value == sayi[i] + sayi[n]+sayi[j]:
                print("{} {} {} toplamlarına eşittir".format(sayi[i], sayi[n],sayi[j]))
