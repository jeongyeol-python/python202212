# function3.py
#가변형식의 경우
wordList = ["J","A","M"]

#함수정의
def change(x):
    x1 = x[:]
    x1[0] = "H"
    print("내부:", x1)

#호출
change(wordList)
print(wordList)

print("---global---")
g = 1
def testScope(a):
    g=2
    return g+a

testScope(1)
print("전역변수 g:", g)

def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print( intersect("HAM", "SPAM"))