print("------------------------ CGPA calculation ---------------------------")
student_name = input("Student Name: ")
student_num = input("Student Number: ")
CU_num = int(input("Number of course units: "))


# Mapping marks to credit units using a python dictionary
dict_marks = {}

for i in range(1,(CU_num + 1)):
    mark = int(input(f"Marks for course unit {i}: "))
    credit_unit = int(input(f"Credit unit for course unit {i}: "))

    dict_marks[mark] = credit_unit


# Feed the function with a mark, it determines the grade and returns the respective grade point
def grade_point_generator(_marks):
    if(_marks>=90):
        grade = 'A'
        grade_point = 5
    
    elif(_marks>=80):
        grade = 'B'
        grade_point = 4
    
    elif(_marks>=70):
        grade = 'C'
        grade_point = 3
    
    elif(_marks>=60):
        grade = 'D'
        grade_point = 2
    
    elif(_marks>=50):
        grade = 'E'
        grade_point = 1
    
    else:
        grade = 'F'
        grade_point = 0
    return grade_point


# Replacing the mark in the dictionary with its respective grade point
marks = list(dict_marks.keys())
for i in range(0,len(marks)):
    dict_marks[grade_point_generator(marks[i])] = dict_marks.pop(marks[i])


# Multiplying the grade point with its repective credit unit, and then summing up the products
SUM = 0
for GP,CU in dict_marks.items():
    SUM = SUM + (GP*CU)


# Calculating the the sum of the credit units
CU_list = list(dict_marks.values())
CU_sum = 0
for CU in CU_list:
    CU_sum = CU_sum + CU

# Calculating CGPA and rounding to 1 decimal place
CGPA = round((SUM / CU_sum),1)

print(f"CGPA of {student_name} is {CGPA}")
print("\n")



print("------------- Basic Calculator Using the last 2 digits of Student Number -------------")
import math
def basic_calc1():
    digits = int(student_num[-2:])   #the last 2 digits at once
    num1 = int(student_num[-1])   #only the last digit
    num2 = int(student_num[-2])   #only the 2nd last digit
    result = 0


    operations = ["(1)+","(2)x","(3)/","(4)-","(5)sin","(6)cos","(7)tan","(8)log","(9)In","(10)sqroot","(11)cuberoot"]
    n = 0
    while n < len(operations):
        print(operations[n], end="      ")
        n = n + 1
    
    operand = input("\n Choose one of the options above(1-11): ")
        
    if(operand == "1"):
        result = num1 + num2
        return result

    elif(operand == "2"):
        result = num1 * num2
        return result

    elif(operand == "3"):
        result = num1 / num2
        return result

    elif(operand == "4"):
        result = num1 - num2
        return result
    elif(operand == "5"):
        result = math.sin(digits)
        return result
    elif(operand == "6"):
        result = math.cos(digits)
        return result
    elif(operand == "7"):
        result = math.tan(digits)
        return result
    elif(operand == "8"):
        result = math.log10(digits)
        return result
    elif(operand == "9"):
        result = math.log(digits)
        return result
    elif(operand == "10"):
        result = math.sqrt(digits)
        return result
    elif(operand == "11"):
        result = math.cbrt(digits)
        return result    

calc_result1 = round(basic_calc1(),1)
print(f"Result : {calc_result1}")

print("\n")
print("------------------- Basic Calculator using the User's Input ----------------------")
def basic_calc2():
    operations = ["(1)+","(2)x","(3)/","(4)-","(5)sin","(6)cos","(7)tan","(8)log","(9)In","(10)sqroot","(11)cuberoot"]
    n = 0
    while n < len(operations):
        print(operations[n], end="      ")
        n = n + 1
    
    operand = input("\n Choose one of the options above(1-11): ")
        
    if(operand == "1"):
        num1 = float(input("Enter num1 : "))
        num2 = float(input("Enter num2 : "))
        result = num1 + num2
        return result

    elif(operand == "2"):
        num1 = float(input("Enter num1 : "))
        num2 = float(input("Enter num2 : "))
        result = num1 * num2
        return result

    elif(operand == "3"):
        num1 = float(input("Enter num1 : "))
        num2 = float(input("Enter num2 : "))
        result = num1 / num2
        return result

    elif(operand == "4"):
        num1 = float(input("Enter num1 : "))
        num2 = float(input("Enter num2 : "))
        result = num1 - num2
        return result
    elif(operand == "5"):
        num = float(input("Enter any number : "))
        result = math.sin(num)
        return result
    elif(operand == "6"):
        num = float(input("Enter any number : "))
        result = math.cos(num)
        return result
    elif(operand == "7"):
        num = float(input("Enter any number : "))
        result = math.tan(num)
        return result
    elif(operand == "8"):
        num = float(input("Enter any number : "))
        result = math.log10(num)
        return result
    elif(operand == "9"):
        num = float(input("Enter any number : "))
        result = math.log(num)
        return result
    elif(operand == "10"):
        num = float(input("Enter any number : "))
        result = math.sqrt(num)
        return result
    elif(operand == "11"):
        num = float(input("Enter any number : "))
        result = math.cbrt(num)
        return result    

calc_result2 = round(basic_calc2(),2)
print(f"Result : {calc_result2}")
