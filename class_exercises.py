
def my_func(mid,final):
    if final>50 and (0.6*mid+0.4*final)>50:
        print("passed")
    else:
        print("failed") 

def calculate_age(name,year):
    RETIREMENT_AGE = 65  # static variables goes all caps
    my_age = 2022 - year
    if my_age > 65:
        print("you already retired")
    return RETIREMENT_AGE - my_age

def swapping(x,y):
    # a = x
    # x = y
    # y = a
    x,y = y,x
    print(x)
    print(y)
    return x, y

def largest_side(val1,val2,val3):
    max_value = max([val1,val2,val3])
    list_ = [val1, val2, val3]
    max_val = sorted(list_)[2]
    
    if val1>val2 and val1>val3:
        return val1
    elif val2>val1 and val2>val3:
        return val2
    return val3  
      
def find_div(num):
    if num%4==0 and num%3==0:
        print("number is divisible by 3 and 4")
    
    elif num%3==0:
        print("number is only divisible by 3")

    else:
        print("number is only divisible by 4")
    
        
find_div(24)                         