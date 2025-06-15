num = int(input("정수를 입력하세요 : ")) 

def isEven(n): 
  return (n%2==0)

def isEven2(n):
  i = n
  while(i>0):
    i-=2
  if(i==0):
    return True;
  else :
    return False;

def isEven3(n):
  return ((n/2)-(n//2)==0)

def isEven4(n):
  return (int(str(float(n/2)).split(".")[1])==0)

list = []
while num > 1 :
  if(isEven4(num)):
    list.append(num) 
  num -= 1
list.reverse()
[print(a) for a in list]