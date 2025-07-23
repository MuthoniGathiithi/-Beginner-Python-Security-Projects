import string 
print("Welcome to the Password Strength Checker!")
password_checks=0
feedback=[]
password=input("Please enter your password: ")

#check 1 : length
if len(password) >= 10:
    print(" ✅ Your password is long enough.")
    password_checks += 1
else:
    print("Your password is too short. It should be at least 10 characters long.")
    feedback.append("Password too short.")

 # check 2 : Uppercase
if any(char.isupper() for char in password):
    print(" ✅ Your password contains uppercase letters.")
    password_checks += 1
else:
    print("Your password should contain at least one uppercase letter.")
    feedback.append("Missing uppercase letter.")

# check 3 : Lowercase
if any(char.islower() for char in password):
    print(" ✅ Your password contains lowercase letters.")
    password_checks += 1
else:
    print("Your password should contain at least one lowercase letter.")
    feedback.append("Missing lowercase letter.")

# check 4 : Digits
if any(char.isdigit() for char in password):
    print(" ✅ Your password contains digits.")
    password_checks += 1    
else:
    print("Your password should contain at least one digit.")
    feedback.append("Missing digit.")   

# check 5 : Special characters

if any(char in string.punctuation for char in password):
    print("✅ Password has symbols!")
    password_checks += 1
else:
    feedback.append("❗ Add symbols like @, #, !, etc.")

#final analysis 
print("\n  final analysis:")  
if password_checks == 4:
    print("Your password is strong! ✅")
else:
    print("Your password is weak. ❌")
    print("Feedback:")
    for item in feedback:
        print(f"- {item}")
if feedback:
    print("\nPlease consider the feedback to improve your password strength.")
    for item in feedback:
        print("-", item)        