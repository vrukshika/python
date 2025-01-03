#
# 1. Sum of N Even Natural Numbers
# n=int(input("enter num:"))
# sum=0
# for i in range(1,n+1):
    # if i%2==0:
        # sum+=i
# print(sum)
# 

# 2. Check for Even Numbers
# n=int(input("enter num:"))
# def is_eve(num):
    # if num%2==0:
        # return True
    # else:
        # return False
# print(is_eve(n))

 
# 3. Check Prime Numbers
# n=int(input("enter num:"))
# def is_prime(num):
    # if num==0 or num==1:
        # return False
    # for i in range(2,num+1):
        # if num%i==0:
        #  return False
        # else:
        #  return True
# print(is_prime(n))


# 4. Valid Perfect Square
# import math as m
# n=int(input("enter num:"))
# def perfect_sqr(n):
    # if m.sqrt(n)*m.sqrt(n)==n:
        # return True
    # else:
        # return False
    # 
# print(perfect_sqr(n))


# 5. GCD of Two Numbers
import math as m
a=int(input("enter a:"))
b=int(input("enter b:"))
def gcd(a,b):
    return m.gcd(a,b)
print(f"gcd of {a} & {b} is:",gcd(a,b))