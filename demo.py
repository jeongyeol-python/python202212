# demo.py
strA="파이썬은 강력해"
print( strA )
print( len(strA ))
print ( strA[0:3] )
colors=["red","green","bule"]
print(colors)
colors.insert(1, "white")
print(colors)

t=(1,2,3)
type(t)

def calc(a,b):
    return a+b, a*b
x,y=calc(5,4)
print(x,y)
args=(3,4)
print(calc(*args))