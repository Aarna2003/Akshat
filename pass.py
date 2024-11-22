#password generator
import random
import string

def generate_password(length):
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
  
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

def password_generator():
    print("Strong Password Generator!")
    
  
    try:
        length = int(input("Enter how long do you want your password to be? (e.g., 8, 12, 16): "))
        
 
        if length < 4:
            print("Password should be at least 4 characters long. Try again!")
        else:
            password = generate_password(length)
            print(f"Your new password is: {password}")
    except ValueError:
        print("Error! Please enter a number for the length.")

if __name__ == "__main__":
    password_generator()
