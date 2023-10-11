class Data:
    def __init__(self, dia, mes, ano):
        self.d = dia
        self.m = mes
        self.a = ano

    def formatada(self):
        self.dataBR()
        self.dataUS()

    def dataBR(self):
        print(f"{self.d}/{self.m}/{self.a}")

    def dataUS(self):
        print(f"{self.m}/{self.d}/{self.a}")
