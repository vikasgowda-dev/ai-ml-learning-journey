
# 1) Airthemetic operator?
#  - Used for mathematical calculations like +,-,*,/,%,**,//.

a = 10
b = 3 
print("-----------Airthemetic operator(operands 10 and 3)-----------")
print("Addition:",a+b)
print("Substraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Modulus:",a%b)
print("Exponent:",a**b)
print("Floor Division:",a//b)


# 2) Relational operator?
# - Compare two values and return true or false.

x = 10
y = 15
print("------Relational operator(operands 10 and 15)-------")
print("Equal to:",x == y)
print("Not Equal:",x != y)
print("Greater-than:",x > y)
print("Less-than:",x < y)
print("Greater or Equal:",x >= y)
print("Less or Equal:",x <= y)

# 3) Logical operator?
# - Used to combine conditions.

age = 22
has_id = True
print("-------Logical operator--------")
print("Both true(and):",age > 18 and has_id)
print("One true(or):",age < 18 or has_id)
print("Not(Reverse):", not has_id)

# 4) Assignment operator?
# - Assign values to variables.

print("--------Assignment operator-------")
num = 10
print("Intial value:",num)
num += 5
print("After += 5:",num)
num -= 3
print("After -= 3:",num)
num *= 2
print("After *= 2:",num)
num /= 4
print("After /= 4:",num)
num %= 2
print("After %= 2:",num)
