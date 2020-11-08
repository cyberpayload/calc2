# ********** A CALCULATOR WITH A LOOP **********

# create while loop
while True:

    # pass in operation functions
    def addition(num1,num2):
        result = float(num1) + float(num2)
        print('\n')
        print(str(num1) + " " + "+" + " " + str(num2) + " " + "=" + " " + str(result))

    def subtraction(num1,num2):
        result = float(num1) - float(num2)
        print('\n')
        print(str(num1) + " " + "-" + " " + str(num2) + " " + "=" + " " + str(result))

    def multiplication(num1,num2):
        result = float(num1) * float(num2)
        print('\n')
        print(str(num1) + " " + "*" + " " + str(num2) + " " + "=" + " " + str(result))

    def division(num1,num2):
        result = float(num1) / float(num2)
        print('\n')
        print(str(num1) + " " + "/" + " " + str(num2) + " " + "=" + " " + str(result))


    # display calculator menu to user
    print('\n')
    print('***WELCOME TO CALC2***')
    print('\n')
    print('A simple looping calculator')
    print('\n')
    print('What  do you want to do?')
    print('\n')
    print('1. ADD')
    print('2. SUBTRACT')
    print('3. MULTIPLY')
    print('4. DIVIDE')
    print('\n')
    print('TYPE Q TO QUIT')

    # get user choice on operation
    operation = input()
    # add break clause
    if operation == 'q' or operation == 'Q':
        break
    else:

    # get user numbers for the operation
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        # check operation variable
        if operation == '1':
            addition(num1,num2)
        elif operation == '2':
            subtraction(num1,num2)
        elif operation == '3':
            multiplication(num1,num2)
        elif operation == '4':
            division(num1,num2)



