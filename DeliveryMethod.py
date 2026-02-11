class Sled:
    def makeDelivery(self):
        return "La livraison a été effectué en traineau."

class Drone:
    def makeDelivery(self):
        return f"La livraison a été effectué en drone."
    
class Bike:
    def makeDelivery(self):
        return f"La livraison a été effectué en vélo."
    
class SetStrategy:
    def __init__(self, method):
        self.method = method

    def execute_strategy(self):
        return self.method.makeDelivery()