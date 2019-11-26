#Wirte a program to convert second into hour and minute takeing input from the users
a=int(input("Enter a time in second:"))
b=a//60
c=a//(60*60)
print("The time in minutes from second is:",b)
print("The time in hour from second is:",c)