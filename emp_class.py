class CommonClass:
    def __str__(self):
        return f"\n{self.__dict__}"

    def __repr__(self):
        return str(self)

class Employee(CommonClass):
    def __init__(self, eid, ename, eage, esal):
        self.EmpID = eid
        self.EmpName = ename
        self.EmpAge = eage
        self.EmpSalary = esal
        self.EmpAddress = []

class Address(CommonClass):
    def __init__(self, pin, city, state):
        self.Pincode = pin
        self.City = city
        self.State = state

if __name__ == "__main__":
    e1 = Employee(eid=101, ename="ABC", eage=24, esal=48000)
    a1 = Address(pin=546545, city="Pune", state="MH")
    a2 = Address(pin=656164, city="Pune", state="MH")
    e1.EmpAddress.append(a1)
    # e1.EmpAddress.append(a2)

    
