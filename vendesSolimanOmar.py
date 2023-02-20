

eixir = False
articles = []
preus = []
quantitats = []


while (not eixir) :

    print("0. Introduir dades per defecte")
    print("1. Introduir un article nou")
    print("2. Fer una venda")
    print("3. Mostrar informacio")
    print("4. Esborrar un article")
    print("5. Esborrar tots els articles")
    print("6. Eixir")
    
    accio = int(input("Que vols fer? "))
    
    if accio == 0:
        articles.extend(["ratoli","teclat","monitor"])
        preus.extend([10,15,120])
        quantitats.extend([10,10,5])

    elif accio == 1:
        article = str(input("Nom de l'article: "))
        articles.append(article)

        preu = float(input("Quin es el seu preu: "))
        preus.append(preu)

        quantitats.append(0)

    elif accio == 2:
        articleven = (input("Que article has venut: "))
        
        for i in range(len(articles)):
            if articleven == articles[i]:
                quantven = int(input("Quantitat venuda: "))
                quantitats[i] += quantven
                break
  
        else:
            print("Error, l'article no existeix.")    

    elif accio == 3:
       
        articlemesven = None
        articlemesingr =  None
        mesingr = 0
        
        importotal = 0
        mesven = 0

        print("ARTICLE".center(20,' '), "QUANTITAT".center(10,' '), "PREU".center(8,' '), "IMPORT".center(10,' '))
        print("".center(20,'_'), "".center(10,'_'), "".center(8,'_'), "".center(10,'_'))
        print("")
        
        for i in range(len(articles)):
            importe = quantitats[i]*preus[i]
            importotal += importe
            quantven = quantitats[i]
            
            print(articles[i].ljust(20, ' '),"%5s %13.2f %10.2f"%(quantitats[i], preus[i], importe))
            
            if quantven > mesven:
                mesven = quantven
                articlemesven = articles[i]

            elif importe > mesingr:
                mesingr = importe
                articlemesingr = articles[i]
        
        print("Total: ".rjust(38,' '), "%12.2f"%(importotal))
        print()
        print(f"L'article mes venut es {articlemesven} amb {mesven} unitats.")
        print(f"L'article amb mes ingresos es {articlemesingr} amb {mesingr} euros")




    elif accio == 4:
        borrarart = input("Que article vols borrar? ")
        posborrar = articles.index(borrarart)
        articles.pop(posborrar)
        preus.pop(posborrar)
        quantitats.pop(posborrar)
       
                

        print(f"Esborrant l'article: {borrarart}")

    

    elif accio == 5:
        articles = []
        preus = []
        quantitats = []

        print("S'han esborrat tots els articles.")
    elif accio == 6:
        segur = input("Segur S/N? ")
        if segur == "S" or "s" or "Si" or "si" or "SI":
            eixir = True
        
        else:
            continue