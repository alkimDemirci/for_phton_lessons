# -*- coding: utf-8 -*-
"""Untitled74.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kXzJ8i_JWysJujhIWzNVeHfIIf672orW

First Task

tuples are unmutube/unchangable, hashable and iterable data type, and can keep repeating variables and has no limitation about the type of variables it keeps 

dictionaries are the iterable data types that are mutuble and contains their variables in key:value pair format. aDictionaries are itirated over the keys values as well as giving the value variebles over the keys. So keys are unique and hasable variables, meaning they cant duplicate or be changed. However, since there is no specific role for them, value variables can duplicated, changed and has no restriction about their data types unlike key variables
"""

# Second Task
def hist(parameter):
  my_dict = {}
  for char in parameter:
    if char not in my_dict:
      my_count = parameter.count(char)
      my_dict.update({char:my_count})
  return my_dict

my_input = input()

print(hist(my_input))

def tupl(my_input):
  my_list = my_input.strip().split(" ")
  sec_list = []
  for elem in my_list:
    if elem.isdigit()==True:
      sec_list.append(elem)
  return tuple(sec_list)    

my_input = input("Pleas enter your numbers: ")
print(tupl(my_input))

# FizzBuzz Game
def my_game(my_limit):
  for lim in range(1,my_limit+1):
    if lim %3 == 0 and lim %5 == 0:
      print("FizzBuzz")
    elif lim %3 == 0 :
      print("Fizz")
    elif lim %5 == 0:
      print("Buzz")
    else:
      print(lim)
  print("Thank you for paticipating in FizzBuzz game!!!")

my_limit = input("Please enter your limit for FizzBuzz game: ")

check = True
while check:
  if my_limit.isdigit()==True:
    check = False
  else:
    print("Please enter a digit!!")
    my_limit = input("Please enter your limit for FizzBuzz game: ")

my_game(int(my_limit))