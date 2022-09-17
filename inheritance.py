#inheris,extend,override
class Employee:
    def __init__(self,name,age):  #extend
        self.name=name
        self.age=age

    
    def work(self):
        print(f"{self.name} is working ... ")


class software_engr(Employee):
    def __init__(self,name,age,level,salary):
        super().__init__(name,age)
        self.level=level
        self.salary=salary

    def debug(self):
        print(f"{self.name} is debugging ...")

    def work(self):
        print(f"{self.name} is cooding ... ")     #over ride
    


se=software_engr("max",11,"junier",500)
print(se.age)
print(se.name)
print(se.level)
print(se.work())
