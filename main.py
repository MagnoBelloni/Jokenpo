# Criado em python 3, utilizando o autopep 8 gerado automaticamente pelo Visual Code

Baralho = ["ás de espada", "Q de Copas", "3 de copas", "7 de ouros"]
CartaDesejada = "3 de copas"


class Buscar:
    def BuscaLinear(self):
        indice = 0
        for Carta in Baralho:
            if Carta == CartaDesejada:
                print(
                    f"A carta {CartaDesejada} está no índice '{indice}' do array.")
                return
            print(f"A carta atual é:  '{Carta}'.")
            indice += 1
        print("Não foi possivel encontrar a carta")


if __name__ == '__main__':
    buscar = Buscar()
    buscar.BuscaLinear()
