#include <stdio.h>
#include <math.h>

int main()
{
    float D;


    printf("\nDammi un numero: ");
    scanf("%f", &D);

    printf("\nL'area del quadrato e` %.2f ", D * D);
    printf("\nL'area del cerchio e` %.2f ", D * D / 4 * M_PI);
    printf("\nL'area del triangolo e` %.2f ", sqrt(3)/4 * D * D);

    return 0;
}
