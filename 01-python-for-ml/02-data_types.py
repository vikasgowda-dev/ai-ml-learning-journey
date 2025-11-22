


# What is Datatypes?
# - Datatypes define the kind of data that a variable can store in memory.


# ---------------
# Example 1
# ---------------
print("-------- Example 1 -----------")

name = "AI System"
total_users = 3700
accuracy = 89.55
is_active = True

print(name,type(name))
print(total_users,type(total_users))
print(accuracy,type(accuracy))
print(is_active,type(is_active))



# ----------------------------------------------------------
# Example 2: AI model information using dictionary and list
# ----------------------------------------------------------


print("-------- Example 2 -----------")

ai_model = {
    "MODEL_NAME": "VisionNet",
    "Version": 2.1,
    "features": ["Image Recongination","Object Recongination"],
    "accuracy": 95.6
}
print(ai_model)
print(type(ai_model))



# --------------------------------------------------
# Example 3: Collection with multiple data types
# --------------------------------------------------


print("-------- Example 3 -----------")

dataset = [100,45.7,"AI",True,{"status":"active"}]

for item in dataset:
    print(item, "->",type(item))