#initiate a class
class employee:
    #special method/magic method/dunder method-constructor
    def __init__(self):
        #print(id(self))
        #print("started executing attributes")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        #print("attributes have been initialized")
    def travel(self):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")
akash = employee()
sam = employee()
#sam.name = "Sam Kumar"
print(sam.name)
print(id(akash))
print(id(sam))
#print(akash.salary)
#akash.travel("Kolkata")
#print(type(akash))