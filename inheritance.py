class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def display(self):
        print(f"Name : {self.name}")
        print(f"age : {self.age}")
        print(f"gender : {self.gender}")

class employee:
    def __init__(self,emp_id,dept):
        self.emp_id = emp_id
        self.dept = dept

    def display(self):
        print(f"Employee id : {self.emp_id}")
        print(f"Dept : {self.dept}")


class manager:
    def __init__(self,name,age,gender,emp_id,dept):
        person.__init__(self,name,age,gender)
        employee.__init__(self,emp_id,dept)

    def display(self):
        person.display(self)
        employee.display(self)

print("Enter details")
name=input("enter the name : ")
age=input("enter the age : ")
gender=input("enter the gender : ")
emp_id=input("enter the emp id : ")
dept=input("enter the dept : ")

mgr=manager(name,age,gender,emp_id,dept)
print("DEtails are")
mgr.display()