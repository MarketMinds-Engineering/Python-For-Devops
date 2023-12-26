import sys
import os
def add(num1,num2):
     num3=num1+num2;
     return num3;

def sub(num1,num2):
     num3=num1-num2;
     return num3;

def mul(num1,num2):
     num3=num1*num2;
     return num3

     
def div(num1,num2):
     num3=num1 / num2
     return num3;


num1=int(sys.argv[1]);
op=sys.argv[2];
num2=int(sys.argv[3]);

if op == "+":
     res=add(num1,num2);
     print(res)

getMypassword=os.getenv("password")
print(getMypassword)