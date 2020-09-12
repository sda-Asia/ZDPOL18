#zmienne

a = input("podaj liczbę a")
b = input("podaj liczbę b")
operacja = input("Co chcesz zrobić?")

#działania

if operacja == "/":
    wynik = float(a) / float (b)
    print(wynik)
elif operacja == "*":
    wynik = float(a) * float(b)
    print(wynik)
elif operacja == "+":
    wynik = float(a) + float(b)
    print(wynik)
elif operacja == "-":
    wynik = float(a) - float(b)
    print(wynik)
elif operacja == "**":
    wynik = float(a) ** float(b)
    print(wynik)
else:
    print("Zła operacaja spróbuj ponownie")
