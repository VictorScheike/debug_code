from sys import argv

script, user_name, colour = argv
variables = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(variables)

print(f"Where do you live {user_name}?")
lives = input(variables)

print("What kind of computer do you have?")
computer = input(variables)

print(f"What colour is your favorite colour?")
colour = input(variables)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
You also like the color {colour}
""")

print(f"I also like the colour {colour}")
