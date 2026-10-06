class Comodo:
    def __init__(self, nome, area):
        self.nome = nome
        self.area = area


class Residencia:
    def __init__(self):
        self.comodos = []

    def adicionar_comodo(self, nome, area):
        # A própria Residencia cria o Comodo
        comodo = Comodo(nome, area)
        self.comodos.append(comodo)

    def visualizar_comodos(self):
        for comodo in self.comodos:
            print(f"Nome: {comodo.nome} - Área: {comodo.area} m²")

    def calcular_area_total(self):
        area_total = 0

        # Soma a área de todos os cômodos
        for comodo in self.comodos:
            area_total += comodo.area

        return area_total


# Programa principal

residencia = None

while True:
    print("\n--- MENU ---")
    print("1 - Criar Residencia")
    print("2 - Adicionar cômodo")
    print("3 - Visualizar cômodos")
    print("4 - Calcular área total")
    print("5 - Encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        residencia = Residencia()
        print("Residencia criada com sucesso!")

    elif opcao == 2:
        if residencia is None:
            print("Crie uma Residencia primeiro.")
        else:
            nome = input("Nome do cômodo: ")
            area = float(input("Área do cômodo em m²: "))

            residencia.adicionar_comodo(nome, area)
            print("Cômodo adicionado com sucesso!")

    elif opcao == 3:
        if residencia is None:
            print("Crie uma Residencia primeiro.")
        else:
            if len(residencia.comodos) == 0:
                print("Nenhum cômodo cadastrado.")
            else:
                residencia.visualizar_comodos()

    elif opcao == 4:
        if residencia is None:
            print("Crie uma Residencia primeiro.")
        else:
            area_total = residencia.calcular_area_total()
            print(f"Área total da Residencia: {area_total} m²")

    elif opcao == 5:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")