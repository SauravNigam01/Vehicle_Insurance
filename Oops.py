class employee:
    def __init__(self):
        #special_method --> constructor
        self.id = 123
        self.sal = 500000
        self.designation = "Software Engineer"

        #method
    def travel(self,destination):
        print("Travelling to ",{destination})

#creating a object of a class
sam = employee()
print(sam.sal)
# calling a method
sam.travel("Bangalore")