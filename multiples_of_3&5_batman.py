value=range(1,31)
for i in value:
    if(i%3==0 and i%5==0):
        print("batman")
    elif(i%3==0):
        print("bat")
    elif(i%5==0):
        print("man")
    else:
        print(i)
