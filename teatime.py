#! /usr/bin/python3
#Teatime
import random
import mealsData as data

#Input: Three string arguments, these must be capitalised days of the week
#Output: Mealplan for dinners for the week. Input days are not assigned dinner.
def mealplan(*working):
    working = list(working)
    threeDayWeek = random.sample(data.dinners, 4)
    index = 0
    
    if working == []:
        return annualLeave()

    for x in data.mealsDict.keys():
        if x not in working:
            data.mealsDict.update({x : threeDayWeek[index]})
            index += 1
    
    for i in data.mealsDict.items():
        print(i)



#Input: No arguments

#Output: Mealplan for dinners for the week.

def annualLeave():
    index = 0
    alWeek = random.sample(data.dinners, 7)

    for x in data.mealsDict.keys():
        data.mealsDict.update({ x : alWeek[index]})
        index += 1

    for i in data.mealsDict.items():
        print(i)

#Basic tests - they only work properly one at a time               
#mealplan()
#annualLeave()