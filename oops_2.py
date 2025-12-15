class Employee:
    def __init__(self):
        self.__name = "Default"
    

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

emp = Employee()
print(emp.get_name())
emp.set_name("Akshay")
print(emp.get_name())