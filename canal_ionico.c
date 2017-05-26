#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <math.h>
#define SEED 35791246

/*Definimos las constantes y los metodos*/
int tam=42;
void printArchivo(double *x, double *y, double *r, int n, FILE *archivo);
double calc_r_max(double x, double y, double *xs, double *ys);
void leerArchivo(FILE *archivo, double *x, double *y);
double randomNormal (double mu, double sigma);

int main()
{
  /*Se leen los primeros datos y se guardan en sus respetivos punteros*/
  FILE * archivo1;
  archivo1 = fopen("Canal_ionico.txt", "r");
  double *x1 = malloc(tam*sizeof(double));
  double *y1 = malloc(tam*sizeof(double));
  leerArchivo(archivo1, x1, y1);

  /*El numero de iteraciones*/  
  int n_iter=200000;
  
  /*Se crean los punteros donde se almacenaran los datos de las caminatas*/
  double *x_walk1 = malloc(n_iter*sizeof(double));
  double *y_walk1 = malloc(n_iter*sizeof(double));
  double *r_walk1 = malloc(n_iter*sizeof(double));
  
  /*Se inicia con un valor aleatorio dentro de las moleculas*/
  x_walk1[0]=((double)rand()/RAND_MAX*20.0)-5.0;
  y_walk1[0]=((double)rand()/RAND_MAX*20.0)-5.0;;
  r_walk1[0]=calc_r_max(x_walk1[0], y_walk1[0], x1, y1);

  /*Se realiza la caminata*/
  int i;
  for(i=1; i<n_iter; i++)
  {
    /*Los nuevos datos*/
    double x_prima=randomNormal(x_walk1[i-1], 0.1);
    double y_prima=randomNormal(y_walk1[i-1], 0.1);
    /*Se calcula el radio maximo con el nuevo centro*/
    double r_prima=calc_r_max(x_prima, y_prima, x1, y1);
    double r_init=calc_r_max(x_walk1[i-1], y_walk1[i-1], x1, y1);
    /*Definimos alpha*/
    double alpha=r_prima/r_init;
    /*Si alpha es mayor a 1 se agregan los datos a la caminata*/
    if(alpha>=1.0)
    {
      x_walk1[i]=x_prima;
      y_walk1[i]=y_prima;
      r_walk1[i]=r_prima;
    }
    /*Sino, solo si alpha es mayor a beta se agrean*/
    else{
      double beta=(double)rand()/RAND_MAX;
      if(beta<=alpha){
	x_walk1[i]=x_prima;
	y_walk1[i]=y_prima;
	r_walk1[i]=r_prima;
      }
      else{
	x_walk1[i]=x_walk1[i-1];
	y_walk1[i]=y_walk1[i-1];
	r_walk1[i]=r_walk1[i-1];
      }
    }
  }
  
  /*Se imprimen los resultados*/
  FILE * arch;
  arch = fopen("walk1.txt", "w");
  printArchivo(x_walk1, y_walk1, r_walk1, n_iter, arch);
  
  /*El procedimiento es exactamente el mismo con el segundo grupo de datos*/
  FILE * archivo2;
  archivo2 = fopen("Canal_ionico1.txt", "r");
  double *x2 = malloc(tam*sizeof(double));
  double *y2 = malloc(tam*sizeof(double));
  leerArchivo(archivo2, x2, y2);

  double *x_walk2 = malloc(n_iter*sizeof(double));
  double *y_walk2 = malloc(n_iter*sizeof(double));
  double *r_walk2 = malloc(n_iter*sizeof(double));

  x_walk2[0]=((double)rand()/RAND_MAX*20.0)-5.0;;
  y_walk2[0]=((double)rand()/RAND_MAX*20.0)-5.0;;
  r_walk2[0]=calc_r_max(x_walk2[0], y_walk2[0], x2, y2);

  int j;
  for(j=1; j<n_iter; j++)
  {
    double x_prima=randomNormal(x_walk2[j-1], 0.1);
    double y_prima=randomNormal(y_walk2[j-1], 0.1);

    double r_prima=calc_r_max(x_prima, y_prima, x2, y2);
    double r_init=calc_r_max(x_walk2[j-1], y_walk2[j-1], x2, y2);
    double alpha=r_prima/r_init;
    if(alpha>=1.0)
    {
      x_walk2[j]=x_prima;
      y_walk2[j]=y_prima;
      r_walk2[j]=r_prima;
    }
    else{
      double beta=(double)rand()/RAND_MAX;
      if(beta<=alpha){
	x_walk2[j]=x_prima;
	y_walk2[j]=y_prima;
	r_walk2[j]=r_prima;
      }
      else{
	x_walk2[j]=x_walk2[j-1];
	y_walk2[j]=y_walk2[j-1];
	r_walk2[j]=r_walk2[j-1];
      }
    }
  }
  
  FILE * arch2;
  arch2= fopen("walk2.txt", "w");
  printArchivo(x_walk2,y_walk2, r_walk2, n_iter, arch2);
  

  
}

/*Este metodo permite leer un archivo y escribir sus datos en dos arreglos. El tamano del archivo debe ser de 42 filas por 2 columnas,*/
void leerArchivo(FILE *archivo, double *x, double *y)
{
  unsigned int i = 0;
  if (archivo != NULL) {
    double temp_x;
    double temp_y;
    while (!feof(archivo)) {
      fscanf(archivo,"%lf %lf",&temp_x,&temp_y);
      x[i]=temp_x;
      y[i]=temp_y;
      i++;
    }
  }
  fclose(archivo);
}

/*Este metodo imprime tres arreglos de datos en un archivo que le llega por parametro*/
void printArchivo(double *x, double *y, double *r, int n, FILE *archivo){
  int i;
  for(i=0;i<n;i++){
    fprintf(archivo, "%lf %lf %lf \n", x[i], y[i], r[i]);
  }
  fclose(archivo);

}

/*Este metodo calcula la distancia a la que se encuentra el punto mas cercano. Lo que es lo mismo, calcula el radio maximo del circulo.*/
double calc_r_max(double x, double y, double *xs, double *ys)
{
  int i;
  double d_min=1000.;
  for(i=0; i<tam; i++)
  {
    double d_act=sqrt((xs[i]-x)*(xs[i]-x)+(ys[i]-y)*(ys[i]-y));
    if(d_act < d_min)
    {
      d_min=d_act;
    }
  }
  if(x<-5.0 || x>15.0 || y<-7.07 || y>17.96)
    d_min=0.1;
  
  return d_min;
}
/*Este metodo permite crear un numero aleatorio entre -1 y 1 con una distribucion normal. Referencia: Phoxis.org. Extraido de https://phoxis.org/2013/05/04/generating-random-numbers-from-normal-distribution-in-c/*/

double randomNormal (double mu, double sigma)
{
  double U1, U2, W, mult;
  static double X1, X2;
  static int call = 0;
 
  if (call == 1)
    {
      call = !call;
      return (mu + sigma * (double) X2);
    }
 
  do
    {
      U1 = -1 + ((double) rand () / RAND_MAX) * 2;
      U2 = -1 + ((double) rand () / RAND_MAX) * 2;
      W = pow (U1, 2) + pow (U2, 2);
    }
  while (W >= 1 || W == 0);
 
  mult = sqrt ((-2 * log (W)) / W);
  X1 = U1 * mult;
  X2 = U2 * mult;
 
  call = !call;
 
  return (mu + sigma * (double) X1);
}



