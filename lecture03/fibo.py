
# A Number is one of:
#   -- 0
#   -- 1 + Number
#
# purpose statement: calculate the n-th fibonacci number
# examples: fibo(0) is  1
#           fibo(1) is  1
#           fibo(2) is  2
#           fibo(3) is  3
#           fibo(4) is  5
#           fibo(5) is  8
#           fibo(6) is 13
# fibo : Number -> Number
def fibo(n):
  if n == 0: return 1
  elif n == 1: return 1
  else:
    return fibo(n-1) + fibo(n-2)
  
