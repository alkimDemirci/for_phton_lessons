# -*- coding: utf-8 -*-
"""Untitled77.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r2e0SAtqIPkb2bYaVFYWa4dxThYb7K6u
"""

# Second Task
class my_class:
  def generateString(self,my_string):
    self.string = my_string
  def readString(self):
    print(self.string)

x = my_class()
my_string = input("write your word: ")
x.generateString(my_string)
x.readString()

# Third Task
class Account:
  def create_accout(self,username,money_amount = 100):
    self.name = username
    self.money = money_amount
  def new_balance(self,my_balance):
    if self.money < my_balance:
      print("Not enough money in account to pull!")
    else:
      self.money -= my_balance
      print(f"You have pulled {my_balance}$ from your account. Now you have {self.money}$ in your account")
  def growth(self,year):
     ammount_to_add = self.money*0.04*int(year)
     print(f"the amount of money that will be added to you in {year} years is {amount_to_add}$.")
     self.money += amount_to_add
  def showBalance(self):
    print(f"currently the amount of the money you have in your account is {self.money}$, annual interest included.")