X = int(input("Enter how much you withdraw= "))
Y = int(input("Enter initial balance of your account= "))
if (X % 5 != 0):
    print("Not Multiple of 5")
elif (X > Y):
    print("Account not hvaing sufficirnt balance")
else:
    Z = Y - X - 0.5
    print(f'YOur account have {Z} balance')
