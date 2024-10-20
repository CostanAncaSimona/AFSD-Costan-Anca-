
articol = "Înțelegerea publicului prin statistici sau combinații de date din surse diferite. Utilizarea de date limitate pentru a selecta publicitatea!"

n= len(articol) // 2 + (len(articol) % 2)
partea1= articol[:n]
partea2= articol[n:]

partea1= partea1.upper().strip()
partea2= partea2[::-1].capitalize()

punctuatie = ".,!,?„”"
for char in punctuatie:
    partea2 = partea2.replace(char, '')

rezultat= partea1+ partea2
print(rezultat)