class WoodenToy:

    def __init__(self, type):
        self.type = type

class ElectronicToy:

    def __init__(self, type):
        self.type = type


class GiftFactory:

    @staticmethod
    def create_gift(type): 
        if type == "bois":
            return WoodenToy(type)
        elif type == "électronique":
            return ElectronicToy(type)
        else:
            raise ValueError("Type de cadeau inconnu")