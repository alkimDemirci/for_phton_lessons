# First Task
my_degree = float(input("Degree : ")) # 1 radi = 57.3 degree
my_radi = my_degree/57.3
print(my_radi)

# Second Task
my_radi = float(input("Radian : ")) # 1 radi = 57.3 degree
my_degree = my_radi*57.3
print(my_degree)

# Third Task
height = float(input("Height : "))
base1=float(input("Base, first value : "))
base2=float(input("Base, second value : "))
Area = float(height*(base1+base2)/2)
print("Area is :",Area)

# Fourth Task
height = float(input("Height of parallelogram : "))
base = float(input("Length of base : "))
area = float(height*base)
print(area)

# Fifth Task
x,y = list(input("volume: ").split(","))
x = x.strip()
y = y.strip()
if " " in x:
  x = x.split(" ")
  height = float(x[1].strip("()"))
else:
     x = x.split("(")
     height = float(x[1].rstrip(")"))
if " " in y:
  y = y.split(" ")
  rad = float(y[1].strip("()"))
else:
     y = y.split("(")
     rad = float(y[1].rstrip(")")) 
sur_area = float((2*3.14*rad**2)+(height*2*3.14*rad))
volume = float(height*3.14*rad**2)  
print("Surface Area is :",sur_area)
print("Volume is :",volume) 

#Sixth Task
radius = float(input("Radius of sphere : ")) # V = 4/3 πr³ and surface area is 3.14*4r^2
surface_area = float(3.14*4*radius**2)
volume = float((4*3.14*radius**3)/3)
print("Surface Area is :",surface_area)
print("Volume is :",volume)

#Seventh Task
diameter = float(input("Diameter of a circle : "))
angle = float(input("Angle measure : "))
radius = float(diameter/2)
arc_length = float(2*3.14*radius*angle/360)
print("Arc Length is :",arc_length)

