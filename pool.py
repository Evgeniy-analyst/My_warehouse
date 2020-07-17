# put your python code here
from math import ceil
a = 6  # float(input()) #storona m
b = 150  # float(input()) #rashod ml
v = 3  # int(input()) #banka ob

if a <= 1 or b <= 50 or v <= 0:
    print("error")
    exit()

S = 5*pow(a, 2)
B_1 = b/1000
B = B_1*S
Q = B/v
print(ceil(Q), S, B)
print(round(Q))
