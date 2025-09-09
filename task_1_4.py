zahl1 = input("Geben Sie die erste Zahl ein: ")
zahl2 = input("Geben Sie die zweite Zahl ein: ")
print(zahl1 + " + " + zahl2 + " = " + str(round((int(zahl1) + int(zahl2)), 2)))
print(zahl1 + " - " + zahl2 + " = " + str(round((int(zahl1) - int(zahl2)), 2)))
print(zahl1 + " * " + zahl2 + " = " + str(round((int(zahl1) * int(zahl2)), 2)))
print(zahl1 + " / " + zahl2 + " = " + str(round((int(zahl1) / int(zahl2)), 2)))
print("/ ist zum geteilt rechnen von zwei Zahlen da, währendessen // grundsätzlich das gleiche tut, allerdings" \
" lässt er die Kommazahlen weg, rundet diese aber nicht!")