#Nombrando variables
Variable_a= 10
Variable_b= 'Fernando'
Variable_c= 3.1415
Variable_d=20
VariaBle_e=30

print (Variable_a,Variable_b,Variable_c,Variable_d,VariaBle_e)
#Esto esta interesante, podemos asignar múltiples variables en una liena de código
x,y,z = 0,1,2

#Ahora haremos un poco de condicionales (if, elif, else)
code="Python"
if code == "Python":
    print("Python es el mejor lenguaje de programación, no tiren hate por fa ")
elif code == "Java":
    print("No me mola el M I N E C R A F T JAVA ")
else:
    print ("Python your ck is the b e s t ")

#Ahora haremos un bucle(while, for, break, continue)
#while, según entendi el ciclo while ejecuta una sección mientras se cumpla una determinada condición
a=0
while a<4:
    print(a)
    a+=1

#Ahora veremos el ciclo for, el ciclo for nos permite iterar (repetir) clases iterables
for i in range(4):
    print(i)

#Continue salta hasta el final del bloque
for v1 in range (8):
    if v1 == 1:
        continue
    print(v1)
#Break rompe la ejecucion del bucle

x = 0
while True:
    print(x)
    if x == 3:
        break
    x += 1




