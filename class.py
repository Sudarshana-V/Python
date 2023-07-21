class SomeClassName:
    var1 = "value1"
    var2 = "value2"

    def function():
        print("function 1")
    
    def function2():
        print("function 2")

if __name__ == "__main__":
    
    SomeClassName.var1 = "new value"
    print(SomeClassName.var1)
    some_obj = SomeClassName()
    # some_obj.var1 = "new value"
    print(some_obj.var1)
    
    some_obj2 = SomeClassName()
    print(some_obj2.var1)


class SomeClassName:
    var1 = "value1"
    var2 = "value2"

    def function(self):
        print(self.var1)
    
    def function2(self):
        print("function 2")

if __name__ == "__main__":
    some_obj = SomeClassName()
    some_obj.function()
