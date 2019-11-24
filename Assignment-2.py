'''Q1:Make a calculator using Python with addition , subtraction , multiplication ,
division and power.'''

number_1 = int(input('Enter your first number: '))
operator_sign = input('Enter operator: ')
number_2 = int(input('Enter your second number: '))

def calculator(value_1,operator,value_2):
    if operator == '+':
        print('Your value is '+ str(value_1 + value_2))
    elif operator == '-':
        print('Your value is '+ str(value_1 - value_2))   
    elif operator == '*': 
        print('Your value is '+ str(value_1 * value_2))   
    elif operator == '/': 
        print('Your value is '+ str(value_1 / value_2))   
    elif operator == '%': 
        print('Your value is '+ str(value_1 % value_2))   
    elif operator == '**': 
        print('Your value is '+ str(value_1 + operator + value_2))   
    else:
        print('Invalid ')

calculator(number_1,operator_sign,number_2)        


'''Q2:Write a program to check if there is any numeric value in list using for loop.'''

arr = ['hammad', 21,'ali', 34, 55,'umer', 89]

for i in arr:

    if type(i) == int:

        print(i)
            

'''Q3:''' 

usr_info = {
    'Name': 'Hammad',
    'Age': 21,
    'university': 'UBIT'
}

print(usr_info)

usr_info['city']='karachi'

print(usr_info)


'''Q4:Write a Python program to sum all the numeric items in a dictionary.'''

num_val = {
    'Num1': 65,
    'Num2': 21,
    'Num3': 43
}

print(sum(num_val.values()))

