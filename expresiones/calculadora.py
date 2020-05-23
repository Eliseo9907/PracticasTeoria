import re

try:
    while True:
        busqueda = re.search(r'([0-9]+)([\/|\*|\-|\+])([0-9]+)', raw_input("Entrada: "))
        
          
                    

        if busqueda:
            print busqueda.group(1)
            print busqueda.group(2)
            print busqueda.group(3)
            n1=int(busqueda.group(1))
            n2=int(busqueda.group(3))
            op=(busqueda.group(2))
          

            if op=="+":
                res=n1+n2
                  
            elif op=="*":
                res=n1*n2
                    
            elif op=="-":
                res=n1-n2
                   
            elif op=="/":
                res=n1/n2
                            
            elif op=="^":
                res=n1**(n2)

            print ("el resultado es:  %s %s %s = %s" % (n1, op, n2, res))
                
        
        else:
         print"qR"


except KeyboardInterrupt:
    pass
