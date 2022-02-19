
# First Task

def get_value(data_list, index):
    
    if len(data_list) <= index:
        return None  
    return data_list[index]

my_list = ['a', 'b', 'c']
index = int(input("Please enter your index: "))
print(get_value(my_list, index))


# Second Task

def my_calculator(my_operation):
    my_oper = my_operation.split()
    if my_oper[1] == "+":
        return int(my_oper[0]) + int(my_oper[2])
    elif my_oper[1] == "-":
        return int(my_oper[0]) - int(my_oper[2])
    elif my_oper[1] == "*":
        return int(my_oper[0]) * int(my_oper[2])
    elif my_oper[1] == "/":
        return int(my_oper[0]) / int(my_oper[2])
    else:
        raise ValueError("the operation is incorrect")     

my_operation = input("Please enter yor operation: ")
print(my_calculator(my_operation))


# Third Task

def my_func(name,surname,university,field,year):
    if name.isalpha() == False or surname.isalpha() == False or university.isalpha() == False or field.isalpha() == False:
        raise ValueError("Your fullname, university and field of study must be all consist of letters only")
    if int(year) < 1 or 4 < int(year):
        raise ValueError("Your year of studying can be only between 1 and 4 years, both inclusive")
    else:
        return name,surname,university,field,year 

