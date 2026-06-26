#simple calculator
def add(x,y):
    return a+b
    def substract(a,b):
        return a-b
        def sum(a,b):
            return a+b
            def mul(a,b):
                return a*b
                def mod(a,b):
                    return a%b
                    def div(a,b):
                        if b==0:
                            return "Error: Division by zero"
                        return a/b
                        while true:
                            print("\n selectect operator")
                            print("1.substraction")
                            print("2.addition")
                            print("3.multiplication")
                            print("4.module")
                            print("5.division")
                            print("6.exist")
                            choice=input("enter your choice number(1:6)")
                            if choice in['1','2','3','4','5']:
                                num1=float(input("enter first number:"))
                                num2=float(input("enter second number:"))
                                  if choice=='1':
                                    print(result=substract(num1,num2))
                                    elif choice=='2':
                                        print(result=add(num1,num2))
                                        elif choice=='3':
                                            print(result=mulplication(num1,num2))
                                            elif choice=='4':
                                                print(result=mod(num1,num2))
                                                elif choice=='5':
                                                    print(result=div(num1,num2))
                                                    else:
                                                        print("invalid choice! please try again.")
                                                        
         

    