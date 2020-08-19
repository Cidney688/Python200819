def circle_area(x):
    num=x*x*3.14
    return num
def circle_circum(y):
    a=y*2*3.14
    return a

n=int(input('半徑:'))
n=circle_area(n)
print(n)

f=int(input('半徑:'))
f=circle_circum(f)
print(f)