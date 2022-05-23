# -*- coding: UTF-8 -*-

# Écrivez un programme qui convertit un nombre entier de secondes fourni au départ en un
# nombre d’années, de mois, de jours, de minutes et de secondes (utilisez l’opérateur modulo : %
# ).

initNbSecond = int(input("Enter a number of seconds : "))

hours = initNbSecond // 3600
restSecond = initNbSecond % 3600
minutes = restSecond // 60
seconds = restSecond % 60

print("\n\t{} sec = {}h : {}min : {}sec".format(initNbSecond, hours, minutes, seconds))