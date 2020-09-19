#Bot for solving calculation
#def for Inserting data
def Name(content,info_name):
    print(content)
    data = input()
    data = data.strip()
    data = data.upper()
    info = info_name +" : "+ data
    file.write(info)
    return(data)
    
def Insert_Data(content,info_name):
    print(content)
    data = input()
    data = data.strip()
    data = data.upper()
    info = info_name +" : "+ data
    file.write(info)
    return(data)
# Here are the arrays to check the input and determine what to do.
Sum = ["SUM","ADDITION","+","ADD"]
Mul = ["MULT","MULTIPLY","PRODUCT","*"]
Div = ["DIVISON","DIV","/"]
Sub = ["SUBTRACT","SUBTRACTION","DIFFERENCES","DEFFERENCE","-"]
symmbol = [""]
#Here is the function to take number from user, calculating and printting result
def Calculation(reply):
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    if reply in Sum:        
        result = num1 + num2
    elif reply in Mul:
        result = num1*num2
    elif reply in  Div:
        result == num1/num2
    elif reply in Sub:
        result = num1-num2
    print("Result -> ",result)
#Here is the function which will take the feedback from the user
def feedback():
    print("Any Feedback-","\U0001F603")
    user_feedback = input("-->")
    feedback = ", user_feedback: "+user_feedback
    file.write(feedback)
    return
#Here is the command to open the file so that user input data can be stored in the file
try:
    file = open("Chat_bot_user_reply.txt","wt")
    #From here the bot will start interacting with user
    print("Hello","\U0001f600","I'm Robin.")
    #Bort is asking to input name from user
    Insert_Data("What's your name?(name)","name")
    #Here bot is asking the user, if they need help in calculation
    reply1 = Insert_Data("May I help you ?(Yes/No)",", need help")
    #Here condition is yes or no. To procced further
    if reply1 == "YES":
        print("Ok, I can help you in calculation..","\U0001F603")
        print()
        reply = Insert_Data("What you wanna do?('+' / '*' / '/' / '-')",", calculation")
        reply = reply.upper()
        Calculation(reply)
    elif reply == "NO":
        print("Your reply has been Submited..")
    else:
        print("UNEXPECTED_VALUE_INPUTED")
    feedback()
    file.close()
    print("Thanks for Your Feedback.","\U0001F603")
except:
    feedback()
    file.close()
    print("Thanks for Your Feedback.","\U0001F603")
