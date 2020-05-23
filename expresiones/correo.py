import re
expresion = r'([(\w)(\.|\-|\_){1}]+)(\@)([a-z]+)(\.)([a-z]+)$'
resultado = re.compile(expresion)
prueba = raw_input("Entrada: ")
busqueda = re.search(resultado,prueba)
if busqueda:
    print busqueda.group()
else:
    print"qR"
