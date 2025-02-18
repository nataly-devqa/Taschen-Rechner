def rechner():
    while True:
        try:
            zahl1 = float(input("Gib die erste Zahl ein: "))
            zahl2 = float(input("Gib die zweite Zahl ein: "))
            break  # Beende die Schleife, wenn die Eingabe gültig ist
        except ValueError:
            print("Ungültige Eingabe. Bitte gib Zahlen ein.")


    while True:
        operation = input("Wähle eine Operation (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            break  # Beende die Schleife, wenn eine gültige Operation eingegeben wurde
        else:
            print("Ungültige Operation. Bitte wähle +, -, *, /.")


    if operation == '+':
        ergebnis = zahl1 + zahl2
    elif operation == '-':
        ergebnis = zahl1 - zahl2
    elif operation == '*':
        ergebnis = zahl1 * zahl2
    elif operation == '/':
        if zahl2 == 0:
            print("Division durch Null ist nicht erlaubt.")
            return  # Beende die Funktion, wenn durch Null dividiert wird
        else:
            ergebnis = zahl1 / zahl2


    print("Ergebnis:", ergebnis)


# Starte den Rechner
rechner()

