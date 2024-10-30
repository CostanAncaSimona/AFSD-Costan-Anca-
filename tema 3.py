meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

# Dicționar pentru stocarea cantităților de comenzi pe fiecare produs
contor_comenzi = {"papanasi": 0, "ceafa": 0, "guias": 0}
incasari_totale = 0

# Pasul 1: Servirea comenzilor
print("1. Comenzi:")
for student in studenti:
    if comenzi and tavi:
        comanda_curenta = comenzi.pop(0)
        tavi.pop()
        istoric_comenzi.append(comanda_curenta)
        contor_comenzi[comanda_curenta] += 1

        # Calculăm incasarea comenzii
        pret_comanda = next(pret[1] for pret in preturi if pret[0] == comanda_curenta)
        incasari_totale += pret_comanda

        # Afișăm comanda curentă
        print(f"{student} a comandat {comanda_curenta}.")
    else:
        print("Nu mai sunt tăvi disponibile sau comenzi în coadă.")
        break

# Pasul 2: Inventar
print("\n2. Inventar:")
print(f"S-au comandat {contor_comenzi['guias']} guias, {contor_comenzi['ceafa']} ceafa, {contor_comenzi['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")
print(f"Mai este ceafa: {'ceafa' in meniu and contor_comenzi['ceafa'] < meniu.count('ceafa')}.")
print(f"Mai sunt papanasi: {'papanasi' in meniu and contor_comenzi['papanasi'] < meniu.count('papanasi')}.")
print(f"Mai sunt guias: {'guias' in meniu and contor_comenzi['guias'] < meniu.count('guias')}.")

# Pasul 3: Finanțe
print("\n3. Finanțe:")
print(f"Cantina a încasat: {incasari_totale} lei.")
produse_ieftine = [produs for produs in preturi if produs[1] <= 7]
print(f"Produse care costă cel mult 7 lei: {produse_ieftine}")

