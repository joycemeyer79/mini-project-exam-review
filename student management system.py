class student:
    def __init__(self,name,regno,department,address,number,gmail):
        self.name = name
        self.Regno = regno
        self.department = department
        self.address = address
        self.number = number
        self.gmail =gmail
    def display(self):
        print("name:", self.name)
        print("regno:", self.Regno)
        print("department:", self.department)
        print("Address:", self.address)
        print("Number:", self.number)
        print("gmail:", self.gmail)
s1=student("joyce meyer", "192319032", "Biomedical", "guntur", 1234567890, "joycemeyerm9032@gmail.com")
s2=student("Thota LOkesh","192312196","ECE","ongole",1234567891,"lokeshthota@gmail.com")
 
s1.display()
s2.display()

        