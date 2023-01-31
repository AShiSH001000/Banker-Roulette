import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
a=len(names)
random_person=random.randint(0,a-1)
b=names[random_person]
print(f"{b} is going to buy the meal today!")
