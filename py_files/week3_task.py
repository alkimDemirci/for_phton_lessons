# -*- coding: utf-8 -*-
"""Week3 Task

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pepjwYTPRrSca3H5u5qv0u3VbgWgnRr9
"""

# First Task
my_input = input("Please enter: ")
while my_input != "coder403":
  my_input = input("Please enter: ") 
print(my_input)

# Second Task
def  check_password(password):
  my_password = password.strip()

  """
  counter = 0
  while counter < 1:
    for char in my_password:
      if char.isupper()==True:
        counter+=1
        check = True
  if check:
  """ 
  if any(char.isupper() for char in my_password): # is True
    """ 
    point = False
    for elem in my_password:
      if elem.islower()==True:
        point = True
        break
    if point:
    """
    if any(elem.islower() for elem in my_password): # is True
      if my_password.isalnum(): # is True
        return True
    else:
      return False
  else:
    return False

# Third Task
email_and_password = input("Input: ") # seperated by space
my_email = email_and_password.split(" ")[0].strip().lower()
my_pass = email_and_password.split(" ")[1]
if check_password(my_pass)==True:
  if my_pass=="Coder403" and my_email=="coder403@yalchin.info":
    print("welcome")
  else:
    print("access denied")
else:
  print("access denied")