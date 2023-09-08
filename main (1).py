#Implementation of recursive function in factorial
def rec_fun(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*rec_fun(n-1)

num=int(input("Enter the number:"))
ans=rec_fun(num)

print("The factorial of a number {} is:{}".format(num,ans))
   