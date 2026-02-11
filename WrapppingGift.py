class WrapppingGift:
    def __init__(self, gift):
        self.gift = gift

    def deliverGift(self, ribbonColor):
        return f"Le cadeau en {self.gift.type} emballé avec un ruban {ribbonColor}"
    
class Delivery:
    def newDelivery(gift):
        return f"Un nouveau {gift} à livrer."