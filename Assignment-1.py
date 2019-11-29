'''Q1: Write a program which takes 5 inputs from user for different subject’s
 marks, total it and generate mark sheet using hello'''
 
math_marks = int(input('Mathematics Marks From 100 : '))
english_marks = int(input('English Marks From 100 : '))
physics_marks = int(input('Physics Marks From 100 : '))
chemistry_marks = int(input('Chemistry Marks From 100 : '))
urdu_marks = int(input('Urdu Marks From 100 : '))

student_total_marks = math_marks + english_marks + physics_marks + chemistry_marks + urdu_marks

student_percentage = student_total_marks / 500 * 100 

total_student_percentage = student_percentage.__round__()

if total_student_percentage >= 85:
    print('You got "A+" Grade')   
elif total_student_percentage >= 70:
    print('You got "A" Grade')
elif total_student_percentage >= 60:
    print('You got "B" Grade')
elif total_student_percentage >= 50:
    print('You got "C" Grade')
else:
    print('You FAILED')         


'''Q2: Write a program which take input from user and identify that the given
number is even or odd?'''

usr_num = int(input("Enter a number to identify that your given number is even or odd ?"))

if usr_num % 2 == 0:
    print("It's Even ...!!")
else: 
    print("It's Odd ...!!")


'''Q3: Write a program which print the length of the list?'''
arr_length = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("The length of given array is: "+ str(len(arr_length)))


'''Q4:Write a Python program to sum all the numeric items in a list?'''
arr_sum = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('Sum of all items in a list is :'+ str(sum(arr_sum)))


'''Q5:Write a Python program to get the largest number from a numeric list.'''
arr_largest_num = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('The largest number from a numeric list is :' + str(max(arr_largest_num)))


'''Q6:Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are
less than 5.'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:

    if i < 5:

        print(i)
