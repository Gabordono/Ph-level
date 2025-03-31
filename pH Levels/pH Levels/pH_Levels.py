ph = int(input("Adj meg egy szamot 0 es 14 kozott: "))

if 0 <= ph <= 14:
    if ph > 7:
        print("Lugos")
    elif ph < 7:
        print("Savas")
    else:
        print("Semleges")
else:
    print("Hibas ertek! Csak 0 es 14 kozotti szam engedelyezett.")
