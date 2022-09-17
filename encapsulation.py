



class soft_engr:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._salary= 222 #   one under score is protected (_X) and two under score (__X) is private
        self._num_bug_solved=0

    #getter
    def get_salary(self):
        return self._salary
        
    #setter
    def set_salary(self,value):
        self._salary=value


se=soft_engr("max",12)
se.set_salary(5000)
print(se.get_salary())
se.set_salary(1000)
print(se.get_salary())
