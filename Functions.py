def calculation(sum, numberofModules):

    total = sum / numberOfModules
    return total

module1 = int(input("Enter percentage for module 1 :"))
module2 = int(input("Enter percentage for module 2 :"))
module3 = int(input("Enter percentage for module 3 :"))
module4 = int(input("Enter percentage for module 4 :"))
module5 = int(input("Enter percentage for module 5 :"))

myList = [module1, module2, module3, module4, module5]

sum = sum(myList)
numberOfModules = len(myList)

total = calculation(sum, numberOfModules)
print(str("Your average mark is : " + str(total) + "%"))