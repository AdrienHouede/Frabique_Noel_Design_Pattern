class SantaCommand:
    def __init__(self, facade):
        self.facade = facade

    def startCommand(self, type):
        return self.facade.new_order(type)
    
    def wrapCommand(self, toy, color):
        return self.facade.wrapGift(toy, color)
    
    def deliverCommand(self, method):
        return self.facade.deliverGift(method)