def ATM():
    print("Enter password:")
    password=input()
    flag=0
    if(password==pass_code[i]):
        flag=1
    else:
        if(password!=pass_code[i]):
            print("Invalid password 2 more attempt left")
            password=input()
            if(password!=pass_code[i]):
                print("Invalid password 1 more attempt left")
                password=input()
                if(password!=pass_code[i]):
                    print("Account Blocked")
                flag=1
            flag=1
        flag=1
    if(flag==0):
        print("END")
    else:
        print("password correct")
    print("1.Withdraw")
    print("2.Deposit")
    print("3.check Balance")
    print("4.Change password")
    choice=int(input())
    if(choice ==1):
        print("Enter the pin:")
        pin_code=int(input())
        if(pin_code==pin[i]):
            print("Enter the amount to be Withdrawn:")
            amount=int(input())
            if(amount<=balance[i]):
                balance[i]=balance[i]-amount
                print("Amount withdrawn successfully!!!")
                print("your current balance is:",balance[i])
            else:
                print("Amount is insufficient,please enter a valid amount")
        else:
            print("Invalid pin,please try again")       
    elif(choice==2):
        print("Enter the pin:")
        pin_code=int(input())
        if(pin_code==pin[i]):
            print("Enter the amount to be deposited:")
            amount=int(input())
            balance[i]=balance[i]+amount
            print("your current balance is ",balance[i])
        else:
            print("Incorrect pin please try again!!!!")
    elif(choice==3):
        print("Enter the pin:")
        pin_code=int(input())
        if(pin_code==pin[i]):
            print(balance[i])
    elif(choice==4):
        print("Enter the current password:")
        password=input()
        if(password==pass_code[i]):
            print("Enter the New password:")
            new_password=input()
            print("please confirm password:")
            confirm_password=input()
            if(confirm_password==new_password):
                print("Password changed succesfully!!!!")
            else:
                print("Confirm password does not match the new password please reenter")
        else:
            print("password does not match please reenter")
    else:
         print("Invalid choice please select a correct choice")

user_name=['Nohitha','Navya','Raj','keerthi']
pass_code=['1345','8765','3456','1653']
pin=[1564,2505,1122,5643]
balance=[456789,67234,567433,123455]
name=input()
if(name not in user_name):
     print("user does not exists")
else:
     print("User Exists")
     i=user_name.index(name)
     ATM()


