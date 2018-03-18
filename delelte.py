myseq = """[a:1,b:2,c:3]
[a:3,b:3,c:8]
[a:7,c:2,m:7,r:4]
[a:2,c:4,m:6,r:4]
[a:3,b:2,c:7,o:5]"""
MyList = []
MyList = myseq.split('\n')
print(MyList)
for i in range(5):
    str1 = MyList[i]
    print(type(str1))
