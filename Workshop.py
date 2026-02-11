class Workshop:
    def __init__(self):
        self.teamElfs = []

    def register(self, elf):
        self.teamElfs.append(elf)

    def notify(self, gift, type):
        for elf in self.teamElfs:
            if elf.specialty == type:
                return elf.makeDelivery(gift)
            else:
                raise ValueError("Aucun lutin n'est capable de livrer ce cadeau")

class Elf:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def makeDelivery(self, gift):
        return f"Le lutin {self.name} va s'occupé de la livraison du cadeau : {gift}"