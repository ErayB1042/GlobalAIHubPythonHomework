"""The user will be defined. Get the data of this user by input method.
Obtain information from user as follow:
-First Name
-Last Name
-Age
-Date of birth
Pass the users information to the list and displays the screen using the for loop.
Print all user information on the screen.
If he is under 18, print 'You cant go out because its too dangerous' on the screen.
If he is over 18, print 'You can go out the street' on the screen."""
print ("Lütfen kayıt için bilgilerinizi giriniz...")
user=[]
user.append(input("Lütfen İsminizi girin:"))
user.append(input("Lütfen Soy isminizi girin:"))
user.append(int(input("Lütfen Yaşınızı giriniz:")))
user.append(int(input("Lütfen doğum tarihinizi-sadece yıl- giriniz:")))
for i in range(4):
    if i == 0:
        print("İsim: {}".format(user[0]))
    elif i == 1:
        print("Soy İsim: {}".format(user[1]))
    elif i == 2:
        print("Yaş: {}".format(user[2]))
    else:
        print("Doğum Tarihi: {}".format(user[3]))
if user[3] < 18 :
    print("You cant go out because it's too dangerous/ Dışarısı çok tehlikeli yalnız dışarı çıkamazsın...")
else:
    print("You can go out to the street/Yalnız dışarı çıkabilirsin...")
