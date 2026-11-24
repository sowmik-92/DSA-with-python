def calculate_sum(a,b):
    return a+b
def calculate_sub(a,b):
    return a-b
def calculate_mul(a,b):
    return a*b
def calculate_div(a,b):
    return a/b

print("1.Calculate two value summation.\n2.Calculate two value subtaction.")
print("3.Calculate two value multiplication.\n4.Calculate two value divide.")

print()

a=float(input("Enter first value : "))
b=float(input("Enter second value : "))

print()

choice=int(input("Choice any operation : "))

if choice==1:
    print("Sum : ",calculate_sum(a,b))
    
if choice==2:
    print("Sub : ",calculate_sub(a,b))
    
if choice==3:
    print("Mul : ",calculate_mul(a,b))
if choice==4:
    print("Div : ",calculate_div(a,b))