#ATM_Program using control statement
i=0
for i in range(0,3):
    pin=int(input("enter your pin:-"))
    if pin==1234:
        print("you have enter the correct pin")
        j=0
        for j in range(0,3):
            account_type=input("Enter your account type:-")
            if account_type=="savings":
                print("you have enter the correct account type")
                amount=int(input("Enter the amount you want to withdraw:-"))
                print("Rs",amount," withdrawn from your account.. Thank you")
                break
            else:
                print("you have enter the wrong account type")
                #continue
            if j==2:
                print("your account is blocked....")
        break
    else:
        print("you have enter the wrong pin")
    #print(i)
    if i==2:
        print("Your account is blocked....")
