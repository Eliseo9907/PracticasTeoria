import re
expresion = r'1{5}'
resultado = re.compile(expresion)
prueba = raw_input("Entrada: ")
busqueda = re.search(resultado,prueba)
if busqueda:
    print busqueda.group()
else:
    print"qR"
    
expresion = r'^1{5}'
resultado = re.compile(expresion)
prueba = raw_input("Entrada: ")
busqueda = re.search(resultado,prueba)

if busqueda:
    print busqueda.group()
else:
    print"qR"
expresion = r'1{5}$'
resultado = re.compile(expresion)
prueba = raw_input("Entrada: ")
busqueda = re.search(resultado,prueba)

if busqueda:
    print busqueda.group()
else:
    print"qR"
