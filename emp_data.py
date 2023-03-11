from emp_class import Employee, Address
import random


def generate_name():   
    name = ""
    for i in range(0, random.randint(4, 8)):
        s = chr(64+random.randint(1, 26))
        name += s
    return name.title()

# print(generate_name())


city_state = {"Pune": "MH", "Banglore": "KA", "Hydrabad": "TS", "Chennai": "TN", "Delhi": "DL", "Chandigarh": "PJ"}

def generate_emps(no):
    emp_list = []
    for i in range(1, no+1):
        city = random.choice(list(city_state.keys()))
        emp = Employee(eid=i+100, ename=generate_name(), eage=random.randint(18, 26), esal=random.randint(15000, 65000))
        adr = Address(pin=random.randint(111111, 999999), city=city, state=city_state[city])
        emp.EmpAddress.append(adr)
        emp_list.append(emp)
    return emp_list

    
# print(generate_emps(10))