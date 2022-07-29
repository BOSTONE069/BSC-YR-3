#Asking the an input from the user
name = input("What is your name? ")

#Removing the whitespaces
name = name.strip()
name = name.title()

first_name, last_name = input("Whats is your name? ").strip().title().split()


print("hi,{}".format(first_name))

"""
The

"""
print(name)

print("Hello," + name)

print("Hello,", name)

print("Hello, {}".format(name))

print(f"Hello, {name}")

print("Hellow, world")