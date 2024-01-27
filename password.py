import random

print("                              PASSWORD GENERATOR","\n") 
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U','V','W','X','Y','Z']

number  = ['0','1','2','3','4','5','6','7','8','9']

symbol = ['!','@','#','$','%','^','&','*','(',')','?']

nol = int(input("Enter the number of alphabet : "))
non = int(input("Enter the number of integer : "))
nos = int(input("Enter the number of symbol : "))
print("\n")

paslist = []

for i in range(1,nol+1):
    ran = random.choice(alphabet)
    paslist += ran
for i in range(1,non+1):
    ran = random.choice(number)
    paslist += ran
for i in range(1,nos+1):
    ran = random.choice(symbol)
    paslist += ran
    
simple_password = ""
for i in paslist:
    simple_password += i
print("The simple password is ",simple_password,"\n")

random.shuffle(paslist)
strong_password = ""
for i in paslist:
    strong_password += i
print("The strong password is ",strong_password)    
    

