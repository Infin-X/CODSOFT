import random
import string

def passw(l):
    c = string.ascii_letters + string.digits + string.punctuation
    p = ''.join(random.choices(c, k=l))
    
    return p

try:
    length = int(input("Enter the desired length of the password: "))
    
    if length <= 0:
        print("Error! :( \nLength specified should be a positive integer.")

    else:
        password = passw(length)
        print("Your Generated Password: ", password)
        print("\nThankyou for using the Generator! ")

except ValueError:
    print("Invalid input. Please enter a valid integer(positive).")
