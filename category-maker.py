#ladataan kategorioiden csv-tiedosto, ja muodostetaan child-parent
#kategoriasuhteiden avulla koko kategoriapolku kullekin kategorialle

#talletetaan saatu kategoriapolku csv-tiedostoon uuteen sarakkeeseen
#nimeltä KATEGORIAPOLKU


#luodaan luokka, joka pitää sisällään tarvittavia tietoja
class kategoria():
    ID = ""
    parent = ""
    name = ""
    path = ""


def muodostaPolku(lista, kategoria):
    if kategoria.parent == "0":
        kategoria.path = kategoria.name
    else:
        for i in lista:
            if i.ID == kategoria.parent:
                kategoria.path = i.name + "/" + kategoria.name
                if i.parent != "0":
                    for a in lista:
                        if a.ID == i.parent:
                            kategoria.path = a.name + "/" + i.name + "/" + kategoria.name
                            if a.parent !="0":
                                for b in lista:
                                    if b.ID == a.parent:
                                        kategoria.path = b.name + "/" + a.name + "/" + i.name + "/" + kategoria.name
                                        if b.parent != "0":
                                             for c in lista:
                                                 if c.ID == b.parent:
                                                     kategoria.path = c.name + "/" + b.name + "/" + a.name + "/" + i.name + "/" + kategoria.name
                                                     if c.parent != "0":
                                                         print("Ei nyt saatana")
    
        
lista = []

with open("tuoteryhmät-v5.csv", "r") as tiedosto:
        tiedosto.readline()
        while True:
                rivi = tiedosto.readline()
                if rivi == "":
                    break
                rivi = rivi.split(";")
                category = kategoria()
                category.ID = rivi[0]
                category.parent = rivi[1]
                category.name = rivi[3]
                lista.append(category)

        for i in lista:
            muodostaPolku(lista, i)
        for i in lista:
            print(i.path)

with open("tuoteryhmat-final.csv", "w") as tiedosto:
    for i in lista:
        tiedosto.write(i.ID+";"+i.parent+";"+i.name+";"+i.path+";\n")

        #for i in lista:
            #print(i.parent)
            #if i.parent == "0":
                #i.path = i.name
            #else 
        #for i in lista:
            #print(i.path)
