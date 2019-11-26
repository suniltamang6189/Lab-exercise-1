""" A school decided to replace the desks in three classrooms.Each desk sits two students.
Given the number of students in each class,print the smallest possible number of desks that can be  purchased.
"""

a=int(input("Enter a number of students in first class:"))
b=int(input("Enter a number of students in second class:"))
c=int(input("Enter a number of students in third class:"))
d=a//2
e=b//2
f=c//2
t=d+e+f
print("The total no. of desk to be purchased:",t)
