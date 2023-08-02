class Auv():
    def __init__(self, nome, nthursters, sensores, ano, lista):
        self.nome = nome
        self.nthursters = nthursters
        self.sensores = sensores
        self.ano = ano
        lista.append(self)
    def exibeAUV(self):
        print(f'Nome: {self.nome}, Número de Thursters: {self.nthursters}, Sensores: {self.sensores}, Ano de Construção: {self.ano}')
    def exibeAUVs(lista):
        for auv in lista:
            auv.exibeAUV()

listaAUVS = []
#sensoresLua = ["Ultrassonico", "Infravermelho"]
#sensoresBr = ["LDR", "Pressao"]
Lua = Auv("Lua", 8, ["Ultrassonico", "Infravermelho"], 2022, listaAUVS)
BrHue = Auv("BrHue", 6, ["LDR", "Pressao"], 2020, listaAUVS)
Lua.exibeAUV()
Auv.exibeAUVs(listaAUVS)