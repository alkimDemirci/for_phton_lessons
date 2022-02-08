#First Task
import datetime as dt


def my_func(my_birth = 2000):
  current_dt = dt.datetime.now()
  current_year = current_dt.year
  my_age = current_year - my_birth
  return my_age


def calculated_age():
    my_birth = input("Please enter the year you were born: ")
    try:
        my_birth = int(my_birth)
        age_year = my_func(my_birth)

        return age_year

    except:
        #string
        return my_func()
my_calculated_age = calculated_age()
print(my_calculated_age)

 