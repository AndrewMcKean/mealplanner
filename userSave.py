#Teatime
#Helper function
import mealsData as data
import teatime

#Function to save user meals.  Not called  directly by the user.
def userSave():
    userCheck = input("Are you happy with these meals? Y/N ")

    if userCheck == "Y":
        f = open("mealset.txt", "a")
        for i in data.mealsDict.keys():
            keypair = ""
            keypair += i
            keypair += ": "
            keypair += data.mealsDict.get(i)
            f.write(keypair)
        f.close()
    else:
        x = input("Would you like to try again? Y/N ")
        if x == "Y":
            teatime.mealplan()
        elif x == "N":
            pass
        else:
            print("Y or N are only valid answers. Please try again")
