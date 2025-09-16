weight = int(input("Geben Sie Ihr Gewicht in kg ein: "))
size = float(input("Geben Sie Ihre Grösse in m ein: "))
BMI = (weight / (size**2))
print("Dein BMI ist: " + str(round(BMI, 2)))