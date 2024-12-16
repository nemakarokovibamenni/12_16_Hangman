from country_list import get_countries

countries = get_countries()

print("Üdvözöllek az akasztófa játékban!")

def easy():
<<<<<<< HEAD
    life == 
    
=======
    life == 7
>>>>>>> a07c304acc2581b3d147b2823e3ca426baf13b8c

def kezdes():

    while True:
        jatek_valasztas = int(input("Válassz szintet!\nKönnyű (1)\nKözepes (2)\nNehéz (3)\nVálassz!: "))
        if jatek_valasztas == 1:
            print("Könnyű nehézség kiválasztva! ✅")
            easy()
        if jatek_valasztas == 2:
            print("Közepes nehézség kiválasztva! ✅")
            medium()
        if jatek_valasztas == 3:
            print("Nehéz nehézség kiválasztva! ✅")
            hard()
        else:
            print("Helytelen formátum! ❌")

