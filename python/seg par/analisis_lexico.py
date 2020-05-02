import ply.lex as lex
tokens=(
    "numero",
    "suma"
    )

t_numero=r'([0-9]+)'
t_suma=r'(\+)'

def t_error(t):
    print"error: simbolo ilegal '%s' en linea%s"%(t.value[0], t.lexer.lineno)
    t.lexer.skip(1)

lexer=lex.lex()
def prueba(entrada):
    lexer.input(entrada)
    while True:
        token=lexer.token()
        if not token:
            break
        print token
while True:
    entrada=raw_input('entrada: ')
    prueba(entrada)
