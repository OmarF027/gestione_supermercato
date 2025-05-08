# ESERCIZIO 1. Dizionario per memorizzare i prodotti
supermercato = {}

# Funzione per aggiungere un prodotto
def aggiungi_prodotto():
    print("Inserisci un nuovo prodotto:")
    nome = input("Nome: ")
    prezzo = input("Prezzo: ")
    supermercato[nome] = (nome, prezzo)  
    print(f"Prodotto '{nome}' aggiunto!")

# Funzione per modificare il prezzo di un prodotto esistente
def cambia_prezzo():
    prodotto_ricerca = input("Inserisci il nome del prodotto a cui vuoi cambiare il prezzo: ")
    if prodotto_ricerca in supermercato:
        nuovo_prezzo = input("Inserisci il nuovo prezzo: ")
        nome, _ = supermercato[prodotto_ricerca]  
        supermercato[prodotto_ricerca] = (nome, nuovo_prezzo)  
        print(f"Il prezzo del prodotto '{prodotto_ricerca}' è stato cambiato in €{nuovo_prezzo}.")
    else:
        print("Prodotto non trovato.")

# Funzione per eliminare un prodotto
def rimuovi_prodotto():
    nome_ricerca = input("Inserisci il nome del prodotto da rimuovere: ")
    if nome_ricerca in supermercato:
        del supermercato[nome_ricerca] 
        print(f"Prodotto '{nome_ricerca}' rimosso.")
    else:
        print("Prodotto non trovato.")        

# Funzione per visualizzare tutti i prodotti
def stampa_prodotti():
    if supermercato:
        print("Tutti i prodotti nel catalogo:")
        for nome, (autore, prezzo) in supermercato.items():  
            print(f"Nome: {nome}, Prezzo: €{prezzo}")
    else:
        print("Non ci sono prodotti nel catalogo.")

# ESERCIZIO 2. Funzione per calcolare la spesa totale
def calcola_scontrino():
    totale = 0
    n = int(input("Quanti articoli hai acquistato? "))
    for i in range(n):
        prezzo = float(input(f"Prezzo articolo {i + 1}: "))
        totale += prezzo
    print(f"Totale da pagare: €{totale:.2f}")

# ESERCIZIO 3. Funzione per calcolare lo sconto fedeltà
def sconto_fedelta():
    categoria = (input("Inserisci la categoria del cliente (standard, silver, gold, platinum): "))
    if categoria == "standard":
        print("Sconto: 0%")
    elif categoria == "silver":
        print("Sconto: 10%")
    elif categoria == "gold":
        print("Sconto: 20%")
    elif categoria == "platinum":
        print("Sconto: 30%")    
    else:
        print("Non hai inserito una categoria valida.")    

# Testing del programma
while True:
    print("\nCosa vuoi fare?")
    print("1. Aggiungi prodotto")
    print("2. Cambia prezzo")
    print("3. Rimuovi prodotto")
    print("4. Stampa prodotti")
    print("5. Calcolare la spesa totale")
    print("6. Calcolare sconto fedeltà")
    print("7. Esci")

    scelta = input("Scelta (1-7): ")

    if scelta == "1":
        aggiungi_prodotto()
    elif scelta == "2":
        cambia_prezzo()
    elif scelta == "3":
        rimuovi_prodotto()
    elif scelta == "4":
        stampa_prodotti()
    elif scelta == "5":
        calcola_scontrino()    
    elif scelta == '6':
        sconto_fedelta()    
    elif scelta == "7":
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida.")
