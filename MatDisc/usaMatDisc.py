import matDisc

m = matDisc.Conjunto()
z = matDisc.Conjunto()


m.inserir('1')
m.inserir('2')
m.inserir('3')

z.inserir('1')
z.inserir('2')
#z.inserir('z')

m.insereNome('A')

z.insereNome('B')

print('Tamanho :', m.tamanho())

m.imprimir()

z.imprimir()

print('Diferença :', m.diferenca(z))

#print(m.uniao(z))

print('Interseccao :', m.intersecao(z))

print('Complemento :', z.complemento(m))

print('Conj Partes :', m.conjunto_partes())

m.conjuntoProprio(z)
