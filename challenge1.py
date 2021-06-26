#Welcome message.
print ("Welcome to practice to Python")

#User and Password saved whithin the program.
user="5991"
password="1995"
user_enter= None
captcha_enter=None
password_enter=None

# The captcha is the sum of the numbers user
captchauser= 5+9+9+1
captcha1num= 5
captcha= captchauser + captcha1num 

# The program confirm access whit the correct User and Password 
user_enter = input ("Type your User: ")

if user==user_enter:
    password_enter=input("Type your Password: ")
    if   password== password_enter:
        # The program confirm access whit the captcha
        captcha_enter=int(input(f"Type the captcha: {captchauser} + {captcha1num} = "))
        if captcha==captcha_enter:
            print ("Session initiated with success. ")
        else:
            print ("Error, Wrong Captcha. ")
    else:
        print ("Error, Wrong Password. ")
else:
    print ("Error, Wrong User. ")