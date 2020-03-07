class Conjunto():
    def __init__(self):
        self.lista = []
        self.quant = 0
        self.comp = {}

    def inserir(self,valor):
        if valor in self.lista:
            return print("Já possui!")
        else:
            self.lista.append(valor)
            self.quant += 1
            return self.lista
            
    def imprimir(self):
        print(*self.lista, sep=',')

    def tamanho(self):
        return self.quant

    def pertence(self, valor):
        return valor in self.lista

    def subconjunto(self, valor):
        for i in valor:
            if i in self.lista:
                return True
            else:
                return False     
        

    def uniao(self,b):
        #------------------------------------------------------
        #Elemento neutro---------------------------------------
        uniao = []
        if self.lista == []:
            for i in b.lista:
                uniao.append(i)

            return("A é vazio!",b.lista)
        if b.lista == []:
            for i in self.lista:
                uniao.append(i)

            return("B É vazio!",self.lista)

        #------------------------------------------------------
        #Idempotencia------------------------------------------
        if self.lista == b.lista:
            return self.lista

        #------------------------------------------------------
        #União-------------------------------------------------
        for i in b.lista:
            uniao.append(i)

        for i in self.lista:
            if i not in b.lista:    
                uniao.append(i)

        return uniao

        #------------------------------------------------------
        #Comutativa--------------------------------------------
        
    

            
            
