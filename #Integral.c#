#include<stdio.h>
#include<math.h>
#define max 100

long double eleva(long double x,int n){
	int i;
	long double y=1.0;
	for(i=0;i<n;++i){
		y*=x;
		}
	return y;
	}
long double fucion(long double A[max],long double x,int n){
	int i;
	long double y,w;
	long double fun=0;
	for(i=0;i<n+1;++i){
		y=eleva(x,i);
		w=A[i]*y;
		fun+=w;		
		}
	return fun;
	}
void pide(long double A[max],int n){
	int i;
	for(i=0;i<n+1;++i){
		printf("a%d:",i);
		scanf("%Lf",&A[i]);
		}
	}

void imprime(long double A[max],int n){
	int i;
	printf("P(x)=");
	for(i=0;i<n+1;++i){
			if(i<n){
				printf("%1.3Lfx^%d+",A[i],i);
			}else{
				printf("%1.3Lfx^%d\n",A[i],i);	
			}
	}
}
long double integra(long double A[max],int n,long double a,long double b,long m){
	long double y,x,r;
	long double inter;
	long double integra=0;
	long i;
	
	r=1.0*m;
	inter=(b-a)/r;
	for(i=0;i<m;++i){
		x=a+((2*i+1)*inter)/2;
		y=fucion(A,x,n);
		integra+=y*inter;		
		}
	return integra;
	}

int main(){
	long double coeficientes[max];
	int n;	
	long m;
	long double a,b;
	long double integral;
	printf("\tSumas de Reimann\n");
	printf("¿Cuál es grado de su polinomio?:");
	scanf("%d",&n);
	printf("Introduce los coeficientes ai\n");
	pide(coeficientes,n);
	printf("\n");
	imprime(coeficientes,n);
	printf("\n");
	printf("Introduce los limites del intervalo [a,b]\n");
	printf("a:");
	scanf("%Lf",&a);
	printf("b:");
	scanf("%Lf",&b);
	printf("¿Cuántas particiones desea realizar?:");
	scanf("%ld",&m);
	integral=integra(coeficientes,n,a,b,m);
	printf("La integral de P en [a,b] es: %Lf\n",integral);
}
