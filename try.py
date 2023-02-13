#python code to illustrate
# working of try()
def divide(x,y):
    try :
        #Floor division : gives only fractionnal part as answer
        result = x//y
        print("your answer is :", result)
    except ZeroDivisionError:
        print("sorry ! you are dividing by zero")
#look at parameters and note the working of program
divide(3,0)   


print("________________________________________")

#python program to demonstrate finally
#no exception exception raised in try block
try:
    k = input("Enter number ")
    a = int(input("Enter number "))
    b = k//a
    
#hendles type arrer exception
except TypeError :
    print("you have type arrer")
else:
    print(b)

finally :                              #this block is always executed
                                        #regerdless of exception generation.
        print("this is always executed")    


print("-----------------------stop--------------------")