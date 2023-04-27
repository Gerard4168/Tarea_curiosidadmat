sum_impares = lambda n: 2 * ((n * (n+1)) / 2) - n # Formula de algebra

n = int(input("Ingrese un número entero positivo n: ")) 
n_cuadrado = n ** 2

sum_n_impares = sum_impares(n)

if n_cuadrado == sum_n_impares:
  print("==============================================")
  print("La curiosidad matematica se cumple para n =", n)
  print("==============================================")
else:
  print("=================================================")
  print("La curiosidad matematica NO se cumple para n =", n)
  print("=================================================")
