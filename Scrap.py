'''lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
Sl = 3
x = (Sl-1)//2
n = len(lst)
res = []
for i in range(x, n-x):
    seq = lst[i-x:i+x+1]
    res.append(seq)
print(res)'''
import math 
e=6.112*math.exp((12.6*10)/(10+243.4))
print(e)