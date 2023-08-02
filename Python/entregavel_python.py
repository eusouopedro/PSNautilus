class Auv():
    def __init__(self, nome, nthursters, sensores, ano, liberdade, lista):
        self.nome = nome
        self.nthursters = nthursters
        self.sensores = sensores
        self.ano = ano
        self.liberdade = liberdade
        lista.append(self)
    def exibeAUV(self):
        print_sensores = ""
        for sensor in self.sensores:
            print_sensores += " " + sensor + ","
        print(f'Nome: {self.nome}, Número de Thursters: {self.nthursters}, Sensores: {print_sensores} Ano de Construção: {self.ano}, Graus de Liberdade: {self.liberdade}')
    def exibeAUVs(lista):
        for auv in lista:
            auv.exibeAUV()
    def ordenaAno(lista):
        lista.sort(key=lambda i: i.ano)
        for auv in lista:
            print(f'AUV: {auv.nome}, Ano: {auv.ano}')

resposta = 0
listaAUVS = []
Lua = Auv("Lua", 8, ["HIdrofones", "BAR 30", "BMP 380", "Vazamento", "Camera"], 2022, 6, listaAUVS)
BrHue = Auv("BrHue", 6, ["Hidrofones", "Camera", "IMU", "Pressao"], 2020, 5, listaAUVS)

while resposta != 5:
    print("Você deseja: ver os AUVs em tabela(1), ver a Lua(2), ver o BrHUE(3), ver os AUVs em ordem de construção(4)?")
    resposta = int(input("Digite sua resposta:(5 para sair) "))
    if resposta == 1:
        Auv.exibeAUVs(listaAUVS)
    elif resposta == 2:
        Lua.exibeAUV()
    elif resposta == 3:
        BrHue.exibeAUV()
    elif resposta == 4:
        Auv.ordenaAno(listaAUVS)
    elif resposta == 5:
        print("Tchau!!")
    else:
        print("Não entendi, digite novamente")
