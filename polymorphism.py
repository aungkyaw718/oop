class Employee:
    def __init__(self,name,age): 
        self.name=name
        self.age=age
    def work(self):
        print(f"{self.name} is working ... ")
class software_engr(Employee):
    def __init__(self,name,age,level,salary):
        super().__init__(name,age)
        self.level=level
        self.salary=salary
    def work(self):
        print(f"{self.name} is cooding ... ")     #over ride
class desinger(Employee):
    def __init__(self,name,age):
        super().__init__(name,age)

    def work(self):
        print(f"{self.name} is drawing...")

se=software_engr("max",11,"junier",500)
se1=software_engr("lisa",23,"senier",900)
ds=desinger("john",23)
se1.work()
se.work()
ds.work()

employees=[software_engr("max",11,"junier",500),software_engr("lisa",23,"senier",900),desinger("john",23)]
            
#polymorphism

def motinate_employee(employees):
    for employee in employees:
        employee.work()
motinate_employee(employees)