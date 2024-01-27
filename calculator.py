print("                          Simple Calculator","\n","\n")
print("You can add,subtract,multiply,divide the two number","\n")
a=int(input("Enter the first number:"))
b=str(input("Enter the operator(+,-,*,/):"))
c=int(input("Enter the second number:"))
if (b == '+'):
    print("the addition of ",a," and ",c," is ",a + c)
elif (b == '-'):
    print("the subtraction of ",a," and ",c," is ",a - c)
elif (b == '*'):
    print("the multiplication of ",a," and ",c," is ",a * c)
elif (b == '/'):
    print("the division of ",a," and ",c," is ",a / c)
else:
    print("Please enter the proper operator")
