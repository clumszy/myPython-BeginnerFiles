# Create a class programmer for storing information 
# of few programmers working at microsoft.

class programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

binay = programmer("Binaya", "Skype")
alka = programmer("Alka", "Gmail")
binay.getInfo()
alka.getInfo()