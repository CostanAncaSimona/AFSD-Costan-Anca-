import random

# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)  # Alegem un cuvânt aleatoriu din listă
progres = ["_" for _ in cuvant_de_ghicit]  # Creăm lista de progres cu liniuțe

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

# Afișarea șablonului inițial (progresul inițial)
print("Bun venit la jocul Spânzurătoarea!")
print("Cuvântul de ghicit este:", " ".join(progres))

# 3. Bucla principală de joc
while incercari_ramase > 0 and "_" in progres:
    # Cererea unei litere
    litera = input("Introdu o literă: ").lower()

    # Verificarea validității literei
    if len(litera) != 1 or not ('a' <= litera <= 'z'):
        print("Te rog introduce o singură literă validă.")
        continue
    if litera in litere_incercate:
        print("Ai încercat deja această literă.")
        continue

    # Adăugăm litera încercată la lista de litere încercate
    litere_incercate.append(litera)

    # Verificăm dacă litera se află în cuvântul de ghicit
    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print("Bravo! Litera se află în cuvânt.")
    else:
        incercari_ramase -= 1
        print("Litera nu este în cuvânt. Încercări rămase:", incercari_ramase)

    # Afișăm progresul curent și încercările rămase
    print("Progres:", " ".join(progres))

# 4. Încheierea jocului
if "_" not in progres:
    print("Felicitări! Ai ghicit cuvântul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvântul era:", cuvant_de_ghicit)
