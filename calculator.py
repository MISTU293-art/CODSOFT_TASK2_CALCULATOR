print("----Calculator----")



def cal():
    while True:
        try:
            num_1 = float(input("Enter First Number:"))
            num_2=float(input("Enter Second Number:"))
        except:
            print("Please Enter Valid Numbers!!")
            continue    
        choices=['+','-','*','/','exit']
        print(choices)
        user_choice=input("Enter Your Choice:")
        if(user_choice==choices[0]):
            addition=num_1+num_2
            print("Addition Is:",addition)
        elif(user_choice==choices[1]):
            subtraction=num_1-num_2
            print("Subtraction:",subtraction)
        elif(user_choice==choices[2]):
            multiplication=num_1*num_2
            print("Multiplication:",multiplication) 
        elif(user_choice==choices[3]):
            if(num_2==0):
                print("Can't divide by zero")
            else:
                division=num_1/num_2
                print("Division:",division)
        elif(user_choice==choices[4]):
            print("Calculator Closed")
            break
        else:
            print("invalid Choice")                   

        

cal()