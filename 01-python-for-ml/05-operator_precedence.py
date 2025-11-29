# Operator precedence 
# - Operator precedence decides which operations are done first in a Python expression.



#                                Higer -----------------> Lower
# (),**,'+x''-x''~x',*///%,+-,'<<''>>',&,^,|,'==''!='>'<'>='<=',not,or,'=''+=''-=''*=''/='.

# note: Higher in the table evaluated first


print("-----Example 1-----------")
a = 2 + 5 * 6
b = (2+3) * 4

print(a)
print(b)

print("------Example 2--------------")

x = 3 
y = 7
z = -2 

result = -x ** y % 4
print(result)

print("------Example 3------------")

a = 5 
b = 10
c = 3

result = a + b > c and b % c == 1 | 0
print(result)

print("-------Example 4------------")
a = 4
b = 2
c = 3

result = a + b ** c > 20 and not (b-c) == 0
print(result)