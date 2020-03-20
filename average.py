import math
import statistics


print("Engineering Average Calculator:")

y = float(input("What is your desired average?:"))


A = float(input("Math: "))
B = float(input("Physics: "))
C = float(input("Chemistry: "))
D = float(input("English: "))
E = float(input("Extra Course: "))  

my_average = [A,B,C,D,E,A]
uoft_average = [A,B,C,D,A]

u= statistics.mean(my_average)
    
print("Engineering Average:{:.2f}".format(u))
print("UofT Eng Average: {:.2f}".format(statistics.mean(uoft_average) ))


print("You need to get a mark up by", (y*6-u*6), " to get a", y, "average")





