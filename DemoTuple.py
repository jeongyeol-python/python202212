# DemoTuple.py
tp = (1,2,3)
print( len(tp) )
print( type(tp) )
print( tp[0] )

#함수 정의
def calc(a,b):
    return a+b, a*b

print( calc(4,5) )

#call
result = calc(3,4)
print(result[0])
print(result[1])

print("id: %s, name: %s" % ("kim", "김유신"))

a = (10, 20, 30)
b = list(a)
b.append(40)
print(b)

print("---dict-----")
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print( type(device ))
print ( device )
for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)

#검색
print( device["아이폰"] )
#입력
device["맥북"] = 15
#수장
device["아이폰"] = 6
#삭제
del device["윈도우"]
print (device)