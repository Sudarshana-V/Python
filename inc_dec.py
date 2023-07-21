value=1
def increment():
    global value
    value=value+1
    print("incremented value ", value)

def decrement():
    global value
    value-=1
    print("decremented value ", value)

def method_executor(function_obj):
    print("within method_execution")
    print("calling ",function_obj)
    function_obj()
    print("calling done...")

if __name__ == "__main__":
    method_executor(increment)
