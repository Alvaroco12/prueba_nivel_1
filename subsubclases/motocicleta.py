from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas, tipo)