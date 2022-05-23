# -*- coding: UTF-8 -*-

# Name : second_convert_time
# Goal : Convert a number of seconds to hours : minutes : seconds
# Author : A. Winceslas
# Date : 05-14-2022 at 11:51 pm

initNbSecond = int(input("Enter a number of seconds : "))

hours = initNbSecond // 3600
restSecond = initNbSecond % 3600
minutes = restSecond // 60
seconds = restSecond % 60

print("\n\t{} sec = {}h : {}min : {}sec".format(initNbSecond, hours, minutes, seconds))