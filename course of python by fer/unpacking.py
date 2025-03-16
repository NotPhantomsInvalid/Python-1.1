# Unpacking
# Unpacking is the process of extracting values from a list or tuple and assigning them to variables.
a,b,c = [1,2,3]
print (a)
print (b)
print (c)

#Tuple unpacking
a,b,c = (1,2,3)
print (a)
print (b)
print (c)
#curious case
a,b,c = ("123")
print (a)
print (b)
print (c)
#diccionary unpacking
a,b,c = {'uno':1, 'dos':2, 'tres':3}
print (a)
print (b)
print (c)
#values unpacking
a,b,c = {'uno':1, 'dos':2, 'tres':3}.values()
print (a)
print (b)
print (c)
#range unpacking
a,b,c = range(3)
print (a)
print (b)
print (c)
#operator unpacking
*a,b = (1,2,3,4)
print (a)
print (b)

a,*b = (1,2,3,4)
print (a)
print (b)
#unpacking extended
a = [1,2]
b = [3,4]
c = [5,6]
print (*a,*b,*c)
#other example
a = [1,2]
b = [3,4]
c = [*a,*b]
print (c)
#unpacking **
a = {'uno':1, 'dos':2}
b = {'tres':3, 'cuatro':4}
c = {'cinco':5, 'seis':6}
print ({**a,**b,**c})
#other example
a = {'uno':1, 'dos':2}
b = {'tres':3, 'cuatro':4}
c = {**a,**b}
print (c)
#unpacking with for
for firts, * rest in [(1,2,3),(4,5,6,7)]:
    print ("First:", firts)
    print ("rest", rest)
#unpacking swapping
a, b = 1, 2
print (a,b)
a,b = b,a
print (a,b)
#unpacking with functions
def funcion(a, *args, **kwargs):
    print (f"args={a} args={args} kwargs={kwargs}")
funcion (1)
funcion (1,2)
funcion (1,2,3, cuatro=4, cinco=5)


