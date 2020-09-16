#Here we define cheese_count and boxes_of_crackers
def bro_and_bros(bro_count, bros_count):
    print(f"You have {bro_count} bro!")
    print(f"You have {bros_count} bros you craw!")
    print("That's enough for a fitness")
    print("Get a dumbel. \n")

#Here we give the function on line 2-6 the worth of cheese and crackers 20 and 30
print("We can just give the function numbers directly:")
bro_and_bros(20,30)

#We switch from cheese count and boxes of crackers to the variables underneath
print("Or we can use the variables from our script:")
amount_of_bro = 10
amount_of_bros = 50
#giving the variables a connection to cheese and crackers
bro_and_bros(amount_of_bro, amount_of_bros)

#Giving them a new worth
print("We can even do math inside too:")
bro_and_bros(10 + 20, 5 + 6)

#They got the worth of line 10 + another set of numbers.
print("We can combine the two, variables and math:")
bro_and_bros(amount_of_bro + 2, amount_of_bros + 1)

print("Hmm, so how many cheese and crackers do i have?")
bro_and_bros(amount_of_bro +5, amount_of_bros - 1)
