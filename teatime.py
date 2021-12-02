#! /usr/bin/python3
#Teatime
#Teatime
import random
import mealsData as data
import userSave as save

#Function to save user meals. Not called directly by the user.

#Cycle works now - not happy feeds back into mealplan function
#However, changing the days of the week doesn't work at that point.
#Not sure why yet.

#Input: Three string arguments, these must be capitalised days of the week
#Output: Mealplan for dinners for the week. Input days are not assigned dinner.
def mealplan():
    working = input('What days is Ciara working? ')
    if len(working) > 1:
        working = working.split(", ")
    print(working)
    daysWorking = random.sample(data.dinners, 7 - len(working))
    print(daysWorking)
    index = 0
    
    
    if working == []:
        return annualLeave()

    for x in data.mealsDict.keys():
        if x not in working:
            data.mealsDict.update({x : daysWorking[index]})
            index += 1
    
    for i in data.mealsDict.items():
        print(i)

    save.saveMeals()


#Input: No arguments
#Output: Mealplan for dinners for the week.
#Helper function - not called by the user.

def annualLeave():
    index = 0
    alWeek = random.sample(data.dinners, 7)

    for x in data.mealsDict.keys():
        data.mealsDict.update({ x : alWeek[index]})
        index += 1

    for i in data.mealsDict.items():
        print(i)

    save.saveMeals()

#Basic tests - they only work properly one at a time               
#mealplan('Tuesday', 'Wednesday')
#annualLeave()

mealplan()