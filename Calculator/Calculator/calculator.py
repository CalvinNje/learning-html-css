import math
import time

second_time = False

def take_first_number():

    while True:
        try:
            num_1 = int(input("Enter value 1: "))
        except ValueError:
            continue
        return num_1


def take_second_number():
    
    while True:
        try:
            num_2 = int(input("Enter value 2: "))        
        except ValueError:
            continue
        return num_2

  
def take_sign():

    valid_signs = ["+", "/", "*", "^", "-"]
    
    while True:
        try:
            sign = input("Enter sign: ")
        except Exception:
            continue
        if sign not in valid_signs:
            continue
        else:
            return sign
    

def show_values():

    global num_1, num_2, answer

    print(f" VALUE 1 - {num_1}")
    print(f" VALUE 1 - {num_2}")
    print(f" VALUE 1 - {answer}")


def show_options():
    print("""
    Continue: (Y/ N) 
 99. Use previous values
 0. Use previous result
 1. Use previous value 1
 2. Use previous value 2 
 3. Show previous values
 4. Go to menu ( STOP )
 5. Start calcutor
 """)

    
def do_the_math(second_time, sign):

    global answer

    if sign == "+":
        answer = num_1 + num_2
    elif sign == "/":
        answer = num_1 / num_2
    elif sign == "*":
        answer = num_1 * num_2
    elif sign == "^":
        answer = num_1 ** num_2
    elif sign == "-":
        answer = num_1 - num_2

    print(f"Result = {answer}")
    control_chip()


def control_chip():
    global num_1, num_2, answer

    done = False
    second_time = True
    show_options()

    while not done:
        try:
            check = input(""" - Choose an option above - 
 - """).upper()

        except Exception:
            continue

        if check == "5" or check == "Y":
            num_1 = take_first_number()
            sign = take_sign()
            num_2 = take_second_number()
            do_the_math(second_time, sign)

        elif check == "N":
            done = True

        elif check == "0":
            num_1 = answer
            sign = take_sign()
            num_2 = take_second_number()
            do_the_math(second_time, sign)

        elif check == "1":
            num_1 = num_1
            sign = take_sign()
            num_2 = take_second_number()
            do_the_math(second_time, sign)

        elif check == "2":
            num_1 = take_first_number()
            sign = take_sign()
            do_the_math(second_time, sign)

        elif check == "3":
            show_values()

        elif check == "4" or check == "STOP":
            brain()

        else:
            continue


def global_storage():

    global num_1_list, num_2_list, result_list
    
    num_1_list = []
    num_2_list = []
    result_list = []


    