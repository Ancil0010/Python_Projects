# class Employee:
#     def __init__(self,Empname,Empno,Sal,disg):
#         self.Empname=Empname
#         self.Empno=Empno
#         self.Sal=Sal
#         self.disg=disg
#     def show(self):
#         print("Employee name =",Empname)
#         print("Employee =",Empno)
#         print("Salary =",Sal)
#         print("Designtion =",disg)
# s=Employee("Ancil",2103007,2000000,"Android Developer")
# s.show()


class Employee:
    def __init__(self,empno,name,desig,salary):
        self.empno = empno
        self.name = name
        self.desig = desig
        self.salary = salary
    def calc_tax(self):
        if(self.salary <= 250000):
            self.tax = 0
        elif (self.salary > 250000 and self.salary <=500000):
            self.tax = 0.1*(self.salary-250000)
        elif(self.salary > 500000):
            self.tax = 25000 + 0.2*(self.salary-500000)
    def display(self):
        print("Employee Name =",self.name)
        print("Employee No =",self.empno)
        print("Designation = ",self.desig)
        print("Salary =",self.salary)
        print("Tax :",self.tax)
emp = Employee(2103007
,"Ancil","B.tech",700000)
emp.calc_tax()
emp.display()