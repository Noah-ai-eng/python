
age = int(input("enter your age:"))
if age <= 20:
    print("You are a teenager.")
elif age <= 50:
    print("You are an adult.")
elif age > 50:
    print("You are an elder.")
else:
    print("Invalid age entered.")