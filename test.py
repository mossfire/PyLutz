from functools import reduce


F=open('script.py')

L=[line.rstrip().upper() for line in open('script.py')  if line[0] !='p' ]
print(L)
