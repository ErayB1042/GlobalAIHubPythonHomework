"""Take 5 values from the user and write a program that prints
the values you get on the screen.
Print the type of values you receives in this program on the screen.
When using print fuctions, do not forget to use f-string and format usage in
your program"""
values=[]
types=[]
print("Lütfen 5 adet değer giriniz...")
for i in range(5):
    dgr=input("Lütfen "+str(i+1)+".değeri giriniz:")
    hata=0
    if hata==0:
        try:
            dgr=int(dgr)
            values.append(dgr)
            types.append(type(dgr))
        except:
            hata+=1
            if hata==1:
                try:
                    dgr=float(dgr)
                    values.append(dgr)
                    types.append(type(dgr))
                except:
                    hata += 1
                    if hata==2:
                        values.append(dgr)
                        types.append(type(dgr))
    if (i+1) == 5:
        print("İstendiği gibi 5 adet değer girdiğiniz için teşekkür ederiz.")
for i in range(len(values)):
    print(str(i+1)+". Girilen değer {}'dir.".format(values[i]))
    print(f'Ve girilen değerin tipi {types[i]} dir.')

