
import re
while True:
	
	expresion=r'^([0-9]+|[a-z]+)\s(\+|\-|\*|\/|\#|\%|\sen|\cos|\tan|[a-z]+)\s([0-9]+|[a-z]+)$'
	resultado=re.compile(expresion)
	prueba=raw_input("Entrada (ingresa el/la (sen,cos, tan, ),: ")
	if prueba=="":
		break
	busqueda=re.search(resultado,prueba)
	if busqueda:
		print busqueda.group(1)
		n1=busqueda.group(1) 
		
		print busqueda.group(2)
		op=busqueda.group(2)
		print busqueda.group(3)
		n2=busqueda.group(3)
		
			
                if n1=="uno":
			n1=1
		if n1=="dos":
			n1=2
		if n1=="tres":
			n1=3
		if n1=="cuatro":
			n1=4
		if n1=="cinco":
			n1=5
		if n1=="seis":
			n1=6
		if n1=="siete":
			n1=7
		if n1=="ocho":
			n1=8
		if n1=="nueve":
			n1=9
		if n1=="cero":
			n1=0
			
		if op=="mas":
			op= "+"		
		if op=="menos":
			op= "-"
		if op=="por":
			op= "*"
		if op=="entre":
			op= "/"
		if op=="raiz":
			op= "#"		
		if op=="elevado":
			op= "%"
		if op=="seno":
			op= "sen"
		if op=="coseno":
			op= "cos"
		if op=="tangente":
			op= "tan"		
		
		
			
                if n2=="uno":
			n2=1
		if n2=="dos":
			n2=2
		if n2=="tres":
			n2=3
		if n2=="cuatro":
			n2=4
		if n2=="cinco":
			n2=5
		if n2=="seis":
			n2=6
		if n2=="siete":
			n2=7
		if n2=="ocho":
			n2=8
		if n2=="nueve":
			n2=9
		if n2=="cero":
			n2=0
	
	try:	
			n1=int(n1)		
			n2=int(n2)	
						
		
			if op=="+" or op=="-" or op=="*" or op=="/" or op=="#"or op=="%" or op=="sen" or op=="cos" or op=="tan":
				if op=="+":
					r=n1+n2
				elif op=="-":
					r=n1-n2
				elif op=="*":
					r=n1*n2
				elif op=="/":
					r=n1/n2
				elif op=="#":
                                        r=n1**(1.0/n2)
                                
                                elif op=="%":
                                        r= n1**n2
                                    
                                elif op=="sen":
                                        r= math.sin(n2)
                                    
                                elif op=="cos":
                                        r= math.cos(n2)
                                    
                                elif op=="tan":

                                        r= math.tan(n2)
               
					
				print "El esultado es: ",r	
		
	except:
		print ("qr \nIntentelo de Nuevo")
