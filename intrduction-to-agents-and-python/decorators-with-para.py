
def decorator(func):
    def wrapper(*args,**kwargs):
        print("I am a call it back")
        res= func(*args,**kwargs)
        print("I am a call it front")
        return res
    return wrapper

@decorator
def greet(a,b):
    print(a*b)

greet(4,5)