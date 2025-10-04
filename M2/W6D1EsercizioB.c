#include <stdio.h>       // libreria standard per input/output 
#include <ctype.h>       // libreria per manipolare caratteri
#include <string.h>      // libreria per la gestione di stringhe
#include <stdbool.h>     // libreria booleana 

#define DEFAULT_NAME "---UNSET---"  //nome utente non settato

int partita();                      // dichiaro funzione intera partita
int domanda(char*, int);           // dichiaro la funzione domanda come stringa e intero
bool contains(int*, int);         // dichiaro una funzione booleana che restituisce un valore vero o falso

int main () 
{                      
    char *intro = "Questo giochino fantastico e pieno di adrenalina ti fara' emozionare come mai prima d'ora!"; //dichiariamo la stringa contenente l'intro del gioco
    printf("%s\n\n", intro);       // stampiamo a schermo l'intro del gioco

    char *prompt_scelta = "\nScegli tra: \n\tA) Iniziare una nuova partita\n\tB) Uscire dal gioco";  // dichiariamo la stringa contenente il menu iniziale
    char scelta;                   // dichiariamo la variabile per memorizzare la scelta dell’utente
    int score = 0;                 // dichiariamo la variabile per il punteggio totale
    char nome[512] = DEFAULT_NAME; // dichiariamo la variabile con il nome dell'utente

    while(true) 
    {   // ciclo infinito per mantenere il gioco attivo finché l’utente non esce
        printf("%s\n", prompt_scelta);   // mostra a schermo il menu di scelta all’utente
        printf("\nComunicami la tua scelta: "); // mostra a schermo la richieda di input all’utente
        scanf(" %c", &scelta);  // legge il carattere inserito

        switch(tolower(scelta)) 
        {  // convertiamo la scelta in minuscolo perche' abbiamo i caratteri A e a
            case 'a': // se l’utente sceglie di giocare
                if(strcmp(nome, DEFAULT_NAME) == 0) // se il nome utente è ancora quello di default
                { 
                    printf("\nComunicami il tuo nome: "); // richiede il nome
                    scanf("%s", nome); // salva il nome inserito dall’utente
                    printf("\n");  // va a capo
                }
                score += partita(); // avvia la partita e somma il punteggio ottenuto
                break;

            case 'b':   // se l’utente sceglie l'opzione b
                printf("scelta b, congratulazioni (forse), il tuo risultato e: %d", score); // mostra punteggio finale
                return 0; // termina il programma

            default:    // se l’utente inserisce un valore che non abbiamo dichiarato
                printf("scelta sbagliata!\n"); // notifica di errore
                break;
        }
    }
}

int partita()  // inizializziamo la funzione partita
{                   
    int score = 0;  // inizializza punteggio della partita

    // il gioco pone le domande e incrementa il punteggio se la risposta è corretta
    score += domanda("Qual è il pianeta più grande del Sistema Solare?\n\t1) Saturno\n\t2) Giove\n\t3) Terra\n", 2);
    score += domanda("In che anno è caduto il muro di Berlino?\n\t1) 1999\n\t2) 1882\n\t3) 1989\n", 3);
    score += domanda("Quale poeta è considerato il padre della lingua italiana?\n\t1) Cosimo Gallo\n\t2) Leopardi\n\t3) Alighieri\n", 3); 
    score += domanda("Quante regioni ha l'Italia?\n\t1) 19\n\t2) 20\n\t3) 21\n", 2);
    score += domanda("Quante lingue ci sono nel mondo?\n\t1) 10\n\t2) 10023\n\t3) 7151\n", 3);

    printf("\nComplimenti hai totalizzato %d punti su 5!\n", score); // stampa il punteggio ottenuto

    return score;                
}

bool contains(int *arr, int element) // funzione che controlla se un elemento è presente nell’array
{ 
    int len = 3;  // lunghezza array fissata manualmente

    for(int i = 0; i < len; i++) // esegue un ciclo che parte da i = 0 e arriva a i < len
        { 
        if(arr[i] == element) {   // se l’elemento corrisponde a quello cercato
            return true;   // restituisce true (trovato)
        }
    }
    return false;  // se non lo trova, restituisce false
}

int domanda(char *d, int correct) // funzione che stampa una domanda e valuta la risposta
{ 
    int scelta;  // variabile per memorizzare la risposta dell’utente
    int possible_answers[] = {1, 2, 3}; // lista delle risposte valide

    while(true) // ciclo infinito finché l’utente non dà una risposta valida
    {                   
        printf("%s\nRisposta: ", d); // stampa la domanda
        scanf("%d", &scelta);   // acquisisce la risposta numerica

        if(scelta == correct)  // se la risposta è corretta
        {     
            return 1;   // restituisce 1 punto
        } 
        else if(contains(possible_answers, scelta)) // se la risposta è valida ma sbagliata
        { 
            return 0; // restituisce 0 punti
        } 
        else // se la risposta non è tra quelle previste
        {                     
            printf("Not an option\n"); // avvisa l’utente che non e' valida
        }
    }
}
