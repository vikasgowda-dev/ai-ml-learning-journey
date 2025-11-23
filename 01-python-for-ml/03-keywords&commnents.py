
# Keywords
#  - Reserved words.

# False, def, in, While, None, del, is, with, True, elif, lambda, yield, and, else, match, case, as , except, nonlocal, assert, finally, not, async, for, or, await, from, pass, break, global, raise, class, if, return, continue, import, try.

print("-----if--------")
age = 20
if age >= 18:
    print("Vote")

print("-----else--------")

age = 16

if age >= 18:
    print("Vote")
else:
    print("Cannot Vote")

print("-------elif-----------")

marks = 70 
if marks >= 90:
    print("Grade A")
elif marks >= 65:
    print("Grade B")
else: 
    print("Grade C")

print("---------for-------")

for i in range(1, 6):
    print(i)

print("------While----------")

count = 1

while count <= 5:
    print(count)
    count += 1