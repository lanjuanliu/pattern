user1=int(input("enter the number"))
user2=int(input("enter the number"))
user3=int(input("enter the number"))
if user1>user2 and user1>user3:
    print("user1 is maximum")
elif user2>user1 and user2>user3:
    print("user2 is maximum")
elif user3>user1 and user3>user2:
    print("user3 is maximum")
else:
    print("manimum")
