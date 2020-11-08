# ********** A CALCULATOR WITH A LOOP **********

# create while loop

# display calculator menu to user
print('1. ADD')
print('2. SUBTRACT')
print('3. MULTIPLY')
print('4. DIVIDE')
print('TYPE Q TO QUIT')

# get user choice on operation
operation = input()

# get user numbers for the operation
num1 = input()
num2 = input()

# check operation variable
if operation == '1':
    add(num1,num2)
elif operation == '2':
    sub(num1,num2):
elif operation == '3':
    mult(num1,num1)
elif operation == '4':
    div(num1,num2)

# pass in operation functions


