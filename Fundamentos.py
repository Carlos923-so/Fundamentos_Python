def nuevoTema(tema):
    print("\n====",tema,"====\n")
    


    

#Este es un comentario
nuevoTema("Operadores logicos")
print("Operador division entero(10//3)",10//3)
print("Operador division entero(5**3)",5**3)#Operador**
'''Este es un comentario de varias linea1'''
print("======Operadores logicos=====")
print("Operador and(True and False):  ", True and False) #True and false siempre dan False**
#Actividad: Imprimir la tabla de verdad de los operadores logicos.**
#AND**
print("Operador and(False and False):  ", False and False) #True and false siempre dan False**
print("Operador and(False and True):  ", False and True)
print("Operador and(True and False):  ", True and False)
print("Operador and(True and True):  ", True and True)
#OR**
print("Operador OR(False and False):  ", False or False)
print("Operador OR(False and True):  ", False or True)
print("Operador OR(True and False):  ", True or False)
print("Operador OR(True and True):  ", True or True)
#NOT**
print("Operador Not(True):  ", not  True)
print("Operador Not(False):  ", not False)

nuevoTema("Operadores logicos")
print("2==3",2==3)
#Actividad:Agregar los demas operadores de comparacion.''
print("2>3",2>3)
print("2<3",2<3)
print("2>=3",2>=3)
print("2<=3",2<=3)
print("2!=2",2!=2)
print("2==3",2==3)

nuevoTema("Variables")
variable1=10
_variable2=6.2456
variable3="Juancho"
dosPalabras="Hola"
dos_palabras="Hello"  

print(variable1,_variable2,variable3,dos_palabras,dosPalabras) #variables valida*

a,b,c=10,5.16,"Palabra" #variables que se asignan.
print(a,b,c)
nuevoTema("Enteros")
w=120
x=9394857585959489387484
y=-256
z=0b00110011
h=0xffa

print(w,type(w))
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(h,type(h))

nuevoTema("Flotantes")
x=1297.50
print(x,type(x))
y=0.5637939
print(y,type(y))

nuevoTema("Numeros complejos")
x=-46j 
y=12*45j
z=2j
print(x, type(x))
print(y,type (x))
print(z,type(z))

nuevoTema("Booleanos")
lis=[8]
print(lis,"es",bool(lis))
t=()
print(t, "es", bool(t))
new="Hello"
print(new, "es", bool(new))
num=99
print(num,"es",bool(num))
comp=1+0j
print(comp, "es",bool(comp))
val=None
print(val, "es", bool(val))

nuevoTema("listas")
a=[10,20.5,"Python List"] 
print(a)
print(a[1])
a[0]="Hola"
print(a[0])

nuevoTema("Tuplas")
t=(25,"Tupla",1+10j, 3.1416)
print (t)
print(t[2])
print("t[1:4]",t[1:4])

nuevoTema("Tuplas")
t= {50,20,30,40,10,50}
print("Conjunto t=", t, type(t))


nuevoTema("Diccionario")
d={1:"Valor1", "Valor2":2j}
print(d,type(d))
print(d,type(d))
print ("d[valor2]:", d["Valor2"])

nuevoTema("Cadenas")
cadena1= "Cadena con comillas dobles"
cadena2= 'Cadena con comillas simples'

print(cadena1, type(cadena1))
print(cadena2, type(cadena2))


cadenaMultilinea='''Esta es una cadena con   tabulares y saltos 
de
linea'''
print(cadenaMultilinea)
print(cadena1[5:11])
print(cadena1[:5]) 
print(cadena1[7:]) 
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1="Hola"
cadena4=(cadena1 + "")*5
print(cadena4)
cadena5= cadena4.upper()
print(cadena4)
