import time

def timer(fmt=".6f"):
    def decorator(func):
        def warpper(*args , **kewarg):
            start_time = time.time()
            result = func(*args , **kewarg)
            end_time = time.time()
            print(f"Elapsed time: {end_time - start_time:{fmt}} seconds")
            return result
        return warpper
    return decorator

@timer(".8f")
def my_function():
    time.sleep(2)
    print("Function completed")

my_function()