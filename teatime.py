#! /usr/bin/python3
#Teatime
import random
import mealsData as data

#Input: Three string arguments, these must be capitalised days of the week
#Output: Mealplan for dinners for the week. Input days are not assigned dinner.
def daysThree(day1, day2, day3):
    working = [day1, day2, day3]
    threeDayWeek = random.sample(data.dinners, 4)
    index = 0
    for x in data.mealsDict.keys():
        if x not in working:
            data.mealsDict.update({x : threeDayWeek[index]})
            index += 1
    for i in data.mealsDict.items():
        print(i)

#Input: Four string arguments, these must be capitalised days of the week
#Output: Mealplan for dinners for the week. Input days are not assigned dinner.
def daysFour(day1, day2, day3, day4):
    working = [day1, day2, day3, day4]
    fourDayWeek = random.sample(data.dinners, 3)
    index = 0
    for x in data.mealsDict.keys():
        if x not in working:
            data.mealsDict.update({x : fourDayWeek[index]})
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
                
#daysThree('Monday', 'Tuesday', 'Wednesday')
daysFour('Monday', 'Tuesday', 'Thursday', 'Saturday')
#annualLeave()