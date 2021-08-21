#Teatime
import random
import mealsData

#Input: Three string arguments, these must be capitalised days of the week
#Output: Mealplan for dinners for the week. Input days are not assigned dinner.
def daysThree(day1, day2, day3):
    working = [day1, day2, day3]
    threeDayWeek = random.sample(dinners, 4)
    index = 0
    for x in mealsDict.keys():
        if x not in working:
            mealsDict.update({x : threeDayWeek[index]})
            index += 1
    for i in mealsDict.items():
        print(i)

#Input: Four string arguments, these must be capitalised days of the week
#Output: Mealplan for dinners for the week. Input days are not assigned dinner.
def daysFour(day1, day2, day3, day4):
    working = [day1, day2, day3, day4]
    fourDayWeek = random.sample(dinners, 3)
    index = 0
    for x in mealsDict.keys():
        if x not in working:
            mealsDict.update({x : fourDayWeek[index]})
            index += 1
    for i in mealsDict.items():
        print(i)
                
