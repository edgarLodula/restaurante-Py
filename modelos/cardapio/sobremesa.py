from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self,nome,preco,tipo,tamanho,descricao):

        super().__init__(nome,preco)
        self._=tipo
        self._tamanho=tamanho
        self._descricao=descricao


    def desconto(self):
        self._preco -=(self._preco*0.02)