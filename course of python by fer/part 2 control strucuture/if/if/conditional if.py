#Conditional if
#The conditional if is used to execute a block of code if a condition is true.
a=4
b=2
if b!=0:
    print (a/b)

# The output is the same, but the code is more readable and maintainable 
if b!=0:
    c=a/b
    d=c+1
    print (d)

#Other example
if b!=0:
    print ("Inside if")
print ("Outside if")

#If with other operators
if b>0:
    print (a/b)
if a>3 and a<8:
    print ("Variable a is higger than 3 and less than 8")

#If in one block of code
if a>4: print ("Is > 4"); print ("Is inside the if")
#Don't do it this, its not recommended

#if with else
if a==4:
    print ("Is 4")
else:
    print ("Is not 4")

#If with elif
if a==4:
    print ("Is 4")
elif a==3:
    print ("Is 3")
else:
    print ("Is not 3 or 4")

#operator ternary
print ("Is 4") if a==4 else print ("Is not 4")

