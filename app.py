from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato 

novo_restaurante=Restaurante('pizza planet','Pizzaria')
novo_suco=Bebida('Suco de Melancia',5.0,'Grande')
novo_suco.desconto()
novo_prato=Prato('Paozinho',2.0,'Pao na chapa tostado')
novo_prato.desconto()
novo_restaurante.adicionar_cardapio(novo_suco)
novo_restaurante.adicionar_cardapio(novo_prato)


def main():
    novo_restaurante.exibir_cardapio()

if __name__ == '__main__':
    main()