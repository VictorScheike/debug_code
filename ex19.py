#Here we define cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("That's enough for a party!")
    print("Get a blanket. \n")

#Here we give the function on line 2-6 the worth of cheese and crackers 20 and 30
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#We switch from cheese count and boxes of crackers to the variables underneath
print("Or we can use the variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#giving the variables a connection to cheese and crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Giving them a new worth
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#They got the worth of line 10 + another set of numbers.
print("We can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("Hmm, so how many cheese and crackers do i have?")
cheese_and_crackers(amount_of_cheese +30, amount_of_crackers - 10)
