class Employee:
    company = 'Visa'
    eCode = 120

class Freelancer:
    company = 'Fiver'
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer( Employee, Freelancer ):
    name = 'Rohit'

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)
# prints the company in employee as employee is 
# stated during inheritance of the class