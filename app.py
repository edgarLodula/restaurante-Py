from restaurante import Restaurante

novo_restaurante=Restaurante('pizza planet','Pizzaria')
novo_restaurante.alternar_estado()
novo_restaurante.receber_avaliacao('Edgar',10)
novo_restaurante.receber_avaliacao('Carlos',6)

novo_restaurante2=Restaurante('Lindo pão','Padaria')
novo_restaurante2.alternar_estado()
novo_restaurante2.receber_avaliacao('Amanda',3)
novo_restaurante2.receber_avaliacao('Rodrigo',5)
novo_restaurante2.receber_avaliacao('Maria',10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()