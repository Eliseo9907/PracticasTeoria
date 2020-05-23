import re
expresion = r'([0-9])'
resultado = re.compile(expresion)
prueba =  raw_input("Entrada: ")

busqueda = re.search(resultado,prueba)
if busqueda:

    rango= range(1,11)
    for i in rango:
        mult= busqueda.group()*i
        print busqueda.group(),"x", i,"=", mult
    
