def pozdrav(ime):
    return "Pozdrav " + ime


pozdrav2 = lambda ime: "Dobrodošao " + ime


def poziv(funkcija):
    a = str(input("Upisite ime: "))

    print(funkcija(a))


funkcija = eval(input("Upisite naziv funkcije('pozdrav' ili 'pozdrav2': "))

poziv(funkcija)
