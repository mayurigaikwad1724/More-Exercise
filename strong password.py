
password=input("enter the password")
if len(password)>6 or len(password)>16:
    if "$" in password:
        if "2" or "8" in password:
            if "A" or "Z" in password:
                print("strong password")
            else:
                print("week password")
        else:
            print("number is wrong")
    else:
        print("different")
else:
    print("password is not right")
