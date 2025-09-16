seconds = int(input("Geben Sie Sekunden an: "))
minutes = int(input("Geben Sie Minuten an: "))
hours = int(input("Geben Sie Stunden an: "))

minutesInSeconds = minutes * 60
hoursInSeconds = hours * 60 * 60

finalSeconds = seconds + minutesInSeconds + hoursInSeconds

print(round(finalSeconds / 60 / 60, 2))