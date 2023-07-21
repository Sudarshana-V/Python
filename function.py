def funct():
    print("Hello world")

if __name__=='__main__':
    funct()

def funct(name):
    print("Hello " +name)

if __name__=='__main__':
    funct("Students")

def funct(name,message):
    print("Hello " ,name, message)

if __name__=='__main__':
    funct("Students","How r u")

def add(num1,num2):
    return num1+num2

if __name__=='__main__':
    result=add([1,2],[2,3])
    print(result)

def add(number1='a', number2='1'):
    return number1 + number2

if __name__ == '__main__':
    result = add()
    print(result)
