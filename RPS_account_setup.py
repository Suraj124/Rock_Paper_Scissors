print("----------------------------")
print("ROCK PAPER SCISSORS ACCOUNT")
print('----------------------------')
while True:
    username=input("Enter your Username : ")
    password=input("Enter your Password : ")
    password_comfirm=input("Confirm yous password : ")

    if password!=password_comfirm:
        print("Password did not match")
    if password==password_comfirm:
        print("Account setup successfully")
        try:
            f=open("accounts.txt","a")
            f.write("\n")
            f.write(username)
            f.write("\n")
            f.write(password)
        except:
            print("Error in file handling")
        finally:
            f.close()
    break