class software_engr:
    #class_attribute
    aliean="jid jid"
    def __init__(self,name,age,level,salary):
        #instance attributes
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
    #instance_method 
    def code(self):
        return(f"{self.name} is writing code...")
    def inform(self):
        return(f"{self.name},{self.age},{self.level},{self.salary}")
    #dunder_ method
    def __str__(self):
        information=f"{self.name},{self.age},{self.level},{self.salary}"
        return information
    def __eq__(self,other):
        return self.name==other.name and self.age ==other.age
    @staticmethod
    def entry_salary(age):
        if age > 25:
            return 5000
        return 3000
    
se1=software_engr("max",20,"junier",5000)
se2=software_engr("lisa",12,"senior",2000)
se3=software_engr("lisa",12,"senior",2000)
#print(se1.code())
#print(se1.inform())
#print(se1)
#print(se2==se3)
print(se1.entry_salary(5))