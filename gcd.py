#recap of while loop 

a=50
b=20

while b > 0:
    #python allows multiple assignments at once
    a,b=b,a%b

print (a)