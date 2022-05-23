

# Name : multiplication_table_by_seven
# Goal : Multiplication table by 7, show * after un multiple of 3
# Author : A. Wincelas
# Date & Time : 05-15-2022 at 12:02 am

from os import system

print("Display the table...")
system('pause')

for i in range(0, 20) :
    line = 7*i
    if(i % 3 == 0) :
        print("7 x {} = {}*".format(i, line))
    else :
        print("7 x {} = {}".format(i, line))

