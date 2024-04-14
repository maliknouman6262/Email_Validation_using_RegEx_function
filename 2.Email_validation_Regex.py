# A-Z
# 0-9
# ., _,for example gmail egt gmail. time_1
# @ for example gmail. time_1
# .2,3
import re
while True:
    email_condition="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    user_email=input("Enter your email: ")
    if user_email=="exit":
        break
    if re.search(email_condition, user_email):
        print("Valid Email")
    else:
        print("Invalid Email")