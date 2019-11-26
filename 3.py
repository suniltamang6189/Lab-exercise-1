"""N studentss take K apples and distributes them among each other evenly.The reamining(the undivisible) part remains in
the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads the
numbers N and K. It should print the two answers of the above questions above."""
a=int(input("Enter no.of students:"))
b=int(input("Enter no. of apples:"))
c=b//a#// is float division while / is integer division
d=b%a
print("The no. of apples received by individual student:",c)
print("The no. of remaining apples in the basket:",d)