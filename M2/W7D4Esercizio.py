import sys                                                                                      # esercizio per inviare pacchetti UDP con ritardi casuali
import socket                                                                                   # e gestire la connessione con un server
import random                                                                                   # per generare pacchetti casuali
import time                                                                                     # per gestire i ritardi


if len(sys.argv) !=4:                                                                           # controllo che siano passati 3 argomenti
    print("Usage: python esercizio.py <ip> <porta> <numero_pacchetti>")                         # messaggio di utilizzo dei parametri
    sys.exit(254)                                                                               # esco con codice di errore 254

ip = sys.argv[1]                                                                                # prendo l'ip dal primo argomento
porta = sys.argv[2]                                                                             # prendo la porta dal secondo argomento
npack = int(sys.argv[3])                                                                        # prendo il numero di pacchetti dal terzo argomento

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                                            # creo un socket UDP
s.connect((ip, int(porta)))                                                                     # mi connetto all'indirizzo e porta specificati

for i in range (npack):                                                                         # invio i pacchetti

    packet = random.randbytes(1024)                                                             # crea un pacchetto di 1024 byte
    s.send(packet)                                                                              # invio il pacchetto al server
    print(f"Inviato pacchetto {i + 1} / {npack} a {ip}:{porta}")                                # stampo il pacchetto inviato

    time_casuale = random.randint(0, 100)                                                       # ritardo casuale tra 0 e 100 millisecondi
    time_casuale = float(time_casuale) / 1000.0                                                 
    print(f"Ritardo casuale di {time_casuale:.2f} secondi prima del prossimo pacchetto")        # stampo il ritardo casuale
    time.sleep(time_casuale)                                                                    # attendo il ritardo casuale prima di inviare il prossimo pacchetto

s.close()                                                                                       # chiudo la connessione
print("Tutti i pacchetti sono stati inviati.")                                                  # messaggio di fine invio pacchetti
