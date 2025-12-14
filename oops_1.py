class Employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"

    def travel(self, destination):
        print(f"Employee travelling to {destination}")

# create an object of employee

sam = Employee()

print(sam.salary)

sam.travel("London")