"""
Number Guessing Game

@author: AmBha

"""

from random import randint

def check_num(user_input):
    return (user_input.isdigit() and 0<int(user_input))

while True:
    top_num=input("Input a number greater than 0: ")
    if check_num(top_num) == True:
        int_top_num=int(top_num)
    else:
        continue
    rand_num=randint(0, int_top_num)
    print (rand_num)
    count=0
    while True:
        user_guess=input("Guess a number: ")
        if int(user_guess)!=(rand_num):
            count+=1
            continue
        count+=1
        break 
    break
print ("It took you "+ str(count)+" tries to get the right number")
        
    


    



 


        
        