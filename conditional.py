"""
> GreaterThan
< LessThan
>= GreaterThanOrEqual
<= LessThanOrEqual
== Equal to
!= Not Equal To
"""

first_number = int(input("Enter the first number? "))
second_number = int(input("Enter the second number? "))

if first_number > second_number:
    print("First number is greater than the second number.")
elif second_number > first_number:
    print("Second number is be greater than first_number")
elif second_number < first_number:
    print("Second number is less than the first number.")
elif first_number < second_number:

elif first_number == second_number:
    print("First number is equal to the second number.")
else:
    print("Enter only integers")
