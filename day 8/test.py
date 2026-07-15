# def check(a,b):
#     assert b!=0, ZeroDivisionError
#     return a/b

# print(check(10,2))
# print(check(10,0))
#

class AgeError(Exception):
    def __init__(self,age):
        self.age = age
    def __str__(self):
        return f"age issue : {self.age}"

age = int(input("enter your age : "))

try:
    if age<18:
        raise AgeError("Age must be greater than 18")
except AgeError as e:
    print(e)
finally:
    print("you see??")
