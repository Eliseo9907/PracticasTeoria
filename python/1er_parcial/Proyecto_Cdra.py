import math
while True:
        palabra=raw_input("Ingrese la operacion (para raiz # para elevacion % ): ") 
        if palabra == "":
             break
        palabra += ";"    
        estado="q0"
        n1 = ""
        n2 = ""
        op = ""
        
    
    
    


        for en in palabra:
            if estado=="q0":
                if en in "0123456789":
                    estado="q1"
                    n1 = en
                if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
                    estado="q7"
                    n1 = en
                if en == ";" or en=="+" or en=="-" or en=="*" or en=="/" or en==" " or en=="%" or en=="#":
                    print "error "
                    exit
                    estado="qr"
            
            elif estado=="q1":
                if en in "0123456789":
                    estado="q1"
                    n1 += en
                if en == ";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="%" or en=="#" or en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
                    estado="qr"
                if en==" ":
                    estado="q2"
           
            
            elif estado=="q2":
                if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
                    estado="q3"
                    op = en
                if en == ";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="%" or en=="#":
                    estado="q4"
                    op += en
                if en in "0123456789" or en==";" or en==" ":
                    estado="qr"
            
            elif estado=="q3":
                if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
                    estado="q3"
                    op += en
                if en in "0123456789" or en==";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="%" or en=="#":
                    estado="qr"
                if en==" ":
                    estado="q5"
            
            elif estado=="q4":
                if en==" ":
                    estado="q5"
                if en in "0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ" or en==";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="%" or en=="#":
                    estado="qr"

            elif estado=="q5":
                if en in "0123456789":
                    estado="q6"
                    n2 = en
                if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
                    estado="q8"
                    n2 = en
                if en== ";" or en=="+" or en=="-" or en=="*" or en=="/" or en==" " or en=="%" or en=="#":
                    estado="qr"
            
            elif estado=="q6":
                if en in "0123456789":
                    estado="q6"
                    n2 += en
                if en==";":
                    estado="qa"
                if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ" or en=="+" or en=="-" or en=="*" or en=="/" or en=="%" or en=="#":
                    estado="qr"
            
            elif estado=="q7":
                if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
                    estado="q7"
                    n1 += en
                if en==" ":
                    estado="q2"
                if en== ";" or en=="+" or en=="-" or en=="*" or en=="/" or en in "0123456789" or en=="%" or en=="#":
                    estado="qr"
            
            elif estado=="q8":
                if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
                    estado="q8"
                    n2 += en
                if en==";":
                    estado="qa"
                if en == " " or en=="+" or en=="-" or en=="*" or en=="/" or en in "0123456789" or en=="%" or en=="#":
                    estado="qr"
        print estado    
   
        if estado=="qa":
            if n1 == "uno" or n1 == "UNO":
              n1=1
            if n1 == "dos" or n1 == "DOS":
                n1=2
            if n1 == "tres" or n1 == "TRES":
                n1=3   
            if n1 == "cuatro" or n1 == "CUATRO":
                n1=4
            if n1 == "cinco" or n1 == "CINCO":
                n1=5
            if n1 == "seis" or n1 == "SEIS":
                n1=6
            if n1 == "siete" or n1 == "SIETE":        
                n1=7         
            if n1 == "ocho" or n1 == "OCHO":        
                n1=8
            if n1 == "nueve" or n1 == "NUEVE":      
                n1=9
            if n1 == "cero" or n1 == "CERO":
                n1=0
            
            if n2 == "uno":
              n2=1
            if n2 == "dos":
                n2=2
            if n2 == "tres":
                n2=3   
            if n2 == "cuatro":
                n2=4
            if n2 == "cinco":
                n2=5
            if n2 == "seis":
                n2=6
            if n2 == "siete":        
                n2=7         
            if n2 == "ocho":        
                n2=8
            if n2 == "nueve":      
                n2=9
            if n2 == "cero":
                n2=0
            if op == "mas":
                op="+" 
            if op == "menos":
                op="-" 
            if op == "por":
                op="*" 
            if op == "entre":
                op="/" 
            if op == "raiz":
                op="#" 
            if op == "elevado":
                op="%"
            if op == "seno":
                op ="sen"
            if op == "coseno":
                op= "cos"
            if op == "tangente":
                op="tan"
        try:
            n1=int(n1)
            n2=int(n2)
        
            op=(op)
      
            if op=="+" or op=="-" or op=="*" or op=="/" or op=="#"or op=="%" or op=="sen" or op=="cos" or op=="tan":
                if op=="+":
                    r=n1+n2
          
                elif op=="*":
                    r=n1*n2
            
                elif op=="-":
                    r=n1-n2
           
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
               
       


                print ("el resultado es:  %s %s %s = %s" % (n1, op, n2, r))
        except:
                print "error de datos"
                
        
                   
