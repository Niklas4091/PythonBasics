distance = int(input("Geben Sie die geplante Distanz in km ein: "))
speed = int(input("Geben Sie die Geschwindigkeit von Ihrem Auto in km/h ein: "))
consumption = int(input("Wie viel verbraucht Ihr Auto an Benzin in Liter pro 100 km? "))

print("Ihre Fahrzeit beträgt: " + str(distance / speed) + " Stunde(n)")
print("Ihr Benzinverbrauch in Liter beträgt: " + str((distance/100)*consumption))