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

#함수의 기본인자값
print("---함수의 기본인자값---")
def times(a=10, b=20):
    return a*b

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드인자(파라메터명 명시)
def connectURI(server, port):
    strURL = "htt[://" + server + ":" + port
    return strURL

print( connectURI("credu.com", "80") )
print( connectURI(port="8080", server="credu.com") ) 

#가변적인 경우(가변인자 *)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print( union("HAM", "EGG") )
print( union("HAM", "EGG", "SPAM") )

#정의되지않은 인자(필수와 옵션이 같이 있는 경우 **)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#call
print( userURIBuilder("credu.com","80",id="kim", passwd="1234") )
print( userURIBuilder("credu.com","80",id="kim", passwd="1234", age="30") )

#간단, 함수정의 문법 > 람다함수
g = lambda x,y:x*y
print( g(3,4) )
print( g(5,6) )

#일회성 람다함수
print( (lambda x:x*x)(3) )
print( globals() )