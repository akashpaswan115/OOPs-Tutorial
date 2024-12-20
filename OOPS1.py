#initiate a class
class employee:
    #special method/magic method/dunder method-constructor
    def __init__(self):
        print("started executing attributes")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes have been initialized")
    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")
akash = employee()
#print(akash.salary)
#akash.travel("Kolkata")
print(type(akash))