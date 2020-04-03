class Conjunto():
    def __init__(self):
        self.lista = []
        self.comp = {}
        self.nome = ''

    def insereNome(self, nome):
        self.nome = nome

    def inserir(self,valor):
        if valor in self.lista:
            return print("Já possui!")
        else:
            self.lista.append(valor)
            return self.lista
            
    def imprimir(self):
        print("Nome do Conjunto: ",self.nome,", Conjunto: ","{",*self.lista,"}.", sep="")

    def tamanho(self):
        return len(self.lista)

    def pertence(self, valor):
        return valor in self.lista

    def subconjunto(self, valor):
        for i in valor:
            if i in self.lista:
                return True
            else:
                return False     
        
    def uniao(self,b):
        #Elemento neutro
        uniao = []
        if self.lista == []:
            for i in b.lista:
                uniao.append(i)

            return("A é vazio!",b.lista)
        if b.lista == []:
            for i in self.lista:
                uniao.append(i)

            return("B É vazio!",self.lista)

        
        #Idempotencia
        if self.lista == b.lista:
            return self.lista

        
        #União
        for i in b.lista:
            uniao.append(i)

        for i in self.lista:
            if i not in b.lista:    
                uniao.append(i)
        return uniao
    
    def intersecao(self, b):
        #Elemento neutro
        inter = []
        if self.lista == []:
            for i in b.lista:
                inter.append(i)

            return("Impossivel realizar a interseção pois contem elemento neutro!")
        if b.lista == []:
            for i in self.lista:
                inter.append(i)

            return("Impossivel realizar a interseção pois contem elemento neutro!")

        else:
            for i in self.lista:
                if i in b.lista:
                    inter.append(i)
            return inter

    def complemento(self, b):
        comp = []
        for i in self.lista:
            if i not in b.lista:
                comp.append(i)
        return comp

    def diferenca(self, b):
        dif = []
        for i in self.lista:
            if i not in b.lista:
                dif.append(i)
                
        for i in b.lista:
            if i not in self.lista:
                dif.append(i)
        return dif

    def conjunto_partes(self):
        a = self.lista
        conjunto = [[None]]
        for i in range (len(a)):
            conjunto.append([a[i]])
            for j in range(1,len(a)):
                if not a[i] == a[j]:
                    if [a[j],a[i]]not in conjunto:
                        conjunto.append([a[i],a[j]])
        for i in range(len(a)):
            for e in range(i+1,len(a)):
                for u in range(e+1,len(a)):
                    conjunto.append([a[i],a[e],a[u]])     
        return conjunto

    def conjuntoProprio(self, b):
        msg = 'Não é conjunto próprio'

        if self.lista == b.lista:
            print(msg)
        else:
            aux = True
            for i in self.lista:
                if i not in b.lista:
                    aux = False

            if aux == False:
                print(msg)
            else:
                msg = 'É subconjunto próprio'
                print(msg)

    


    
                


        
