# Calculating Expected Offspring

#Method 1
# number of couples in each type
C1, C2, C3, C4, C5 = 19118, 18071, 17753, 16614, 19504
# expected value for each couple to have a offspring with dominant phenotype (*2)
ev1, ev2, ev3, ev4, ev5 = 2, 2, 2, 1.5, 1
# calculating expected offspring
Exp_offspring = C1 * ev1 + C2 * ev2 + C3 * ev3 + C4 * ev4 + C5 * ev5
Exp_offspring

#Method 2

c = 19118, 18071, 17753, 16614, 19504
ev = 2, 2, 2, 1.5, 1
sum([a*b for a, b in zip(c, ev)])
