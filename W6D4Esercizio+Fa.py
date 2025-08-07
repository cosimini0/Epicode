import math  # importa la libreria math per usare funzioni matematiche 

# funzione che mostra le figure geometriche disponibili e gestisce la scelta dell'utente
def scelta_utente(scelte_possibili: list[int]) -> int:
    print("Dimmi che vuoi tra")  # messaggio iniziale

    # mostra le opzioni disponibili all'utente
    if 1 in scelte_possibili:
        print("\t1) Perimetro e area del quadrato")
    if 2 in scelte_possibili:
        print("\t2) Perimetro e area del cerchio")
    if 3 in scelte_possibili:
        print("\t3) Perimetro e area del rettangolo")

    ok = False  # controllo della scelta dell'utente
    # ciclo per assicurarsi che l'utente inserisca un numero valido
    while not ok:
        try:
            opzione: int = int(input("Scegli: "))  # chiede all'utente un numero intero valido
            if opzione in scelte_possibili:  # verifica se la scelta è tra quelle disponibili
                ok = True  # se sì, esce dal ciclo
            else:
                print(f"La tua scelta ({opzione}) non andava bene!")  # altrimenti da' un messaggio di errore
        except ValueError:  # se l'input non è un numero intero
            print("Dammi un valore numerico!!")  # manda un messaggio di errore

    return opzione  # restituisce la scelta dell'utente

# acquisizione del valore iniziale da tastiera
ok = False  # controllo input
while not ok:  # ciclo finché l'utente non inserisce un numero valido
    try:
        valore: float = float(input("Scegli un valore: "))  # chiede un numero decimale anche con virgola
        ok = True  # se l'input è valido, esce dal ciclo
    except ValueError:  # se l'input non è un numero valido
        print("Dammi un valore numerico!!")  # manda un messaggio di errore

# inizializza le variabili per perimetro e area
perimetro: float = 0.0  # valore iniziale del perimetro
area: float = 0.0       # valore iniziale dell'area

# lista delle figure disponibili da scegliere
scelte_possibili = [1, 2, 3]  # 1 = quadrato, 2 = cerchio, 3 = rettangolo

# ciclo che continua finché ci sono figure disponibili
while len(scelte_possibili) > 0:
    opzione = scelta_utente(scelte_possibili)  # chiede all'utente quale figura calcolare
    scelte_possibili.remove(opzione)  # rimuove la figura scelta dalla lista

    # calcolo perimetro e area in base alla figura scelta
    if opzione == 1:  # se l'utente ha scelto il quadrato
        perimetro = valore * 4  # formula del perimetro del quadrato
        area = valore * valore  # formula dell'area del quadrato

    elif opzione == 2:  # se l'utente ha scelto il cerchio
        perimetro = 2 * math.pi * valore  # formula della circonferenza con il pi greco
        area = valore * valore * math.pi  # formula dell'area del cerchio con il pi greco
 
    elif opzione == 3:  # se l'utente ha scelto il rettangolo
        # altezza = base / 2
        # quindi perimetro = 2 * base + 2 * altezza = 2 * valore + valore = 3 * valore
        perimetro = 3 * valore  # calcolo del perimetro
        area = valore * valore / 2  # calcolo dell'area con altezza = base / 2

    else:  # caso impossibile, solo per sicurezza
        raise Exception("Eccezione Impossibile!!")  # errore se qualcosa non va come dovrebbe

    valore = area  # l'area appena calcolata diventa il nuovo valore per la figura successiva

    # stampa i risultati con massimo due numeri dopo la virgola .2f
    print(f"Perimetro {perimetro:.2f}")  # mostra il perimetro
    print(f"Area      {area:.2f}")       # mostra l'area