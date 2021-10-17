#! /usr/bin/python3
#Teatime
import random
import mealsData as data

#Input: Three string arguments, these must be capitalised days of the week
#Output: Mealplan for dinners for the week. Input days are not assigned dinner.
def mealplan(*working):
    working = list(working)
    daysWorking = random.sample(data.dinners, 7 - len(working))
    index = 0
    print(len(working))
    print(daysWorking)
    
    if working == []:
        return annualLeave()

    for x in data.mealsDict.keys():
        if x not in working:
            data.mealsDict.update({x : daysWorking[index]})
            index += 1
    
    for i in data.mealsDict.items():
        print(i)
    
    userCheck = input("Are you happy with these meals? Y/N ")

    if userCheck == "Y":
        f = open("mealset.txt", "a")
        for i in data.mealsDict.keys():
            keypair = ""
            keypair += i
            keypair += ": "
            keypair += data.mealsDict.get(i)
            f.write(i)
        print(keypair)
        f.close()
    else:
        x = input("Would you like to try again? Y/N ")
        if x == "Y":
            mealplan(working)
        elif x == "N":
            pass
        else:
            print("Y or N are only valid answers. Please try again")




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
#mealplan('Tuesday', 'Wednesday')
#annualLeave()

keypair = "John"
f = open('mealset.txt', 'a')
f.write("John")
f.close()