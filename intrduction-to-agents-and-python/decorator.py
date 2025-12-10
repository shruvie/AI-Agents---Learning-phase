def decorator(func):
    def wrapper():
        print("before exec")
        func()
        print("after exec")
    return wrapper

@decorator
def greet():
    print(5)
greet()