"""
Write a function that receives a list of numbers
and a term 'n' and returns only the elements that are divisible
by that term 'n'. You must use List comprehensions to solve it.

Example:
    divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)  # [9, 6, 3]

"""


def divisible_numbers(a_list, term):
    divisible = [x for x in a_list if x % 3 == 0]
    return divisible
    
    
    
print (divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3))