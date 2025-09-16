password = input("Bitte geben Sie ein sicheres Passwort ein: ")
if(len(password) > 8):
    print("Das Passwort ist stark!")
else:
    print("Das Passwort muss länger als 8 Zeichen sein!")