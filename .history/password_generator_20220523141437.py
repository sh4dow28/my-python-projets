# -*- coding: UTF-8 -*-

# Name : password_generator
# Goal : Strong password generator
# Author : A. Winceslas
# Date : 05-23-2022 at 1:48 pm

import random

from pandas import concat

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "./$*&()-_=#;}{[]@%?,"

concat_all = lower + upper + numbers + symbols

min_lenght = 8

password = "".join(random.sample(concat_all, min_lenght))

print(password)