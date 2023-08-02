class Auv():
    def __init__(self, nome, nthursters, sensores, ano, lista):
        self.nome = nome
        self.nthursters = nthursters
        self.sensores = sensores
        self.ano = ano
        lista.append(self)

def exibeAUVs(Au):
    for a in Au:
        print(f'Nome: {a.nome}, Número de Thursters: {a.nthursters}, Sensores: {exibeSensores(a.sensores)}, Ano de Construção: {a.ano}')

def exibeSensores(listaS):
    for sensor in listaS:
        print(sensor)
listaAUVS = []
sensoresLua = ["Ultrassonico", "Infravermelho"]
Lua = Auv("Lua", 6, sensoresLua, 2020, listaAUVS)
exibeAUVs(listaAUVS)