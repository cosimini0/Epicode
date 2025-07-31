#include <stdio.h>   // libreria per input/output
#include <math.h>    // libreria funzioni matematiche

int main()           
{
    float D;         // dichiarazione variabile float D

    // chiediamo all'utente di inserire un numero
    printf("\nDammi un numero: ");     
    scanf("%f", &D);   // prendiamo il numero inserito dall'utente e lo inseriamo nella variabile D

    // calcoliamo e stampiamo l'area del quadrato
    //%.2f lo inseriamo perche vogliamo un massimo di 2 numero dopo la virgola
    printf("\nL'area del quadrato e` %.2f ", D * D);  

    // calcoliamo e stampiamo l'area del cerchio
    printf("\nL'area del cerchio e` %.2f ", D * D / 4 * M_PI); 

    // Calcoliamo e stampiamo l'area del triangolo equilatero
    printf("\nL'area del triangolo e` %.2f ", sqrt(3)/4 * D * D); 

    return 0;   
}