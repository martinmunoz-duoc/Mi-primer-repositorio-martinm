peliculas = {"p101": ["amanecer_de_otoño", "drama", 160, "c", "eng", False ], 
"p102": ["caos_liquido", "terror", 210, "d", "fre", True ], 
"p103": ["planeta_neon", "accion", 120, "b", "esp", True]}
cartelera = {"p103": [4000, 30], "p102": [6000, 60], "p101": [8000, 0]}
"""
========Menu principal=========
1. agregar
2. buscar
3. eliminar
4. actualizar
5. mostrar
6. salir
"""
def lista_opciones():
    print("menu principal")
    print("1. agregar")
    print("2. buscar")
    print("3. eliminar")
    print("4. actualizar")
    print("5. mostrar")
    print("6. salir")

def ingresar_opcion():
 opcion=0
try:
    
 opcion=int(input)("ingrese una opcion (1-6): ")
except ValueError:
 print("debe ingresar un numero valido")
def titulo():
  amanecer_de_otoño = "p101"
  caos_liquido = "p102"
  planeta_neon = "p103"
def genero():
  accion = 1
  terror = 2
  drama = 3
def duracion_min():
  1 = 120
  2 = 160
  3 = 210
  0 = None
def clasificacion():
  a = 10 or 4
  b = 11 or 15
  c = 16 or 19
  d = 20 or 40
def idioma():
  eng = 1
  esp = 2
  fre = 3
def es_3D():
 si=True
 no=False
def principal():
  while True:
    lista_opciones()
    opcion=ingresar_opcion()
    print(opcion)
    
    if opcion==1:
     input = genero("ingrese el genero deseado: ")
    if genero == 1 or 2 or 3:
     print("el total de cupos disponibles es: ", genero)
    elif opcion==2:
    try:
     input = cartelera("ingrese precio minimo: ")
     if 4000 and 8000:
      print("las peliculas encontradas son: 1 - planeta neon 2 - amanecer de otoño 3 - caos liquido")
    except ValueError:
     print("No puede ingresar letras, solo numeros enteros")
    elif opcion==6:
    print("Gracias por usar nuestro sistema, hasta pronto.")