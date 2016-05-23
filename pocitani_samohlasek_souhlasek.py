
with open("samohlasky.txt") as vokaly:
    samohlasky = vokaly.read()
with open("souhlasky.txt") as konsonanty:
    souhlasky = konsonanty.read()
with open("text.txt") as text:
    retezec = text.read()


pocet_samohlasek = 0
for _ in samohlasky:
    pocet_vyskytu = retezec.count(_)
    pocet_samohlasek += pocet_vyskytu

pocet_souhlasek = 0
for _ in souhlasky:
    pocet_vyskytu = retezec.count(_)
    pocet_souhlasek += pocet_vyskytu

print("Počet samohlásek: " + str(pocet_samohlasek))
print("Počet souhlásek: " + str(pocet_souhlasek))
