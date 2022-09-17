class soft_engr:
    def __init__(self):
        self._salary= 222 #   one under score is protected (_X) and two under score (__X) is private


    @property    #get
    def salary(self):
        return self._salary
        
    @salary.setter  #set
    def salary(self,value):
        self._salary=value
    
    @salary.deleter#set
    def salary(self):
        del self._salary

se=soft_engr()
se.salary=5000
print(se.salary)
del se.salary
print(se.salary)