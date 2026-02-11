from DeliveryMethod import Sled, Drone, Bike, SetStrategy
from Workshop import Workshop, Elf
from GiftFactory import GiftFactory
from WrapppingGift import WrapppingGift, Delivery
from SantaCommand import SantaCommand

class Santa:
    def __init__(self):
        self.factory = GiftFactory()
        self.workshop = Workshop()
        self.workshop.register(Elf("Patoche", "bois"))
        self.workshop.register(Elf("Jean Eude", "électronique"))

    def new_order(self, type):
        #Factory
        print("Le cadeau a été fabriqué")
        return self.factory.create_gift(type)        

    def wrapGift(self, gift, ribbonColor):
        # Decorator
        toy = WrapppingGift(gift)
        toy = toy.deliverGift(ribbonColor)
        
        print(Delivery.newDelivery(toy))
        # Oberserver
        print(self.workshop.notify(toy, gift.type))

    def deliverGift(self, method):
        # Dictionary pointer function
        dictionnaire_strat = {
            "moderne" : SetStrategy(Drone()),
            "traditionnelle" : SetStrategy(Sled()),
            "écologique" : SetStrategy(Bike())}
        
        if method in dictionnaire_strat:
            print(dictionnaire_strat[method].execute_strategy())
        else:
            raise ValueError(f"Erreur : La méthode '{method}' n'est pas reconnue.")


santa = Santa()
# Command 
command = SantaCommand(santa)

type = input("Choisissez le type de matériau entre bois ou électronique\n")
toy = command.startCommand(type)
color = input("Choisissez la couleur du ruban\n")
command.wrapCommand(toy, color)
method = input("Choisissez le mode de livraison entre moderne, traditionnelle et écologique\n")
command.deliverCommand(method)
