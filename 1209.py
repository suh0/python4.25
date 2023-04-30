class Line:
    length = 0
    def __init__(self, length):
        self.length = length
        print(self.length, "길이의 선이 생성되었습니다.")
        
    def __del__(self):
        print(self.length, "길이의 선이 삭제되었습니다.")
    
    def __add__(self, other):
        print("선의 길이를 합칩니다.")
        return self.length + other.length
    
    def __lt__(self, other):
        print("선의 길이를 비교합니다.")
        return self.length < other.length
    
    def __eq__(self, other):
        print("선의 길이를 비교합니다.")
        return self.length == other.length
    

myLine1 = Line(100)
myLine2 = Line(200)

print(myLine1)

print('길이 합 = ', myLine1 + myLine2)

if myLine1 < myLine2:
    print("myLine2가 더 깁니다.")
    
elif myLine1 == myLine2:
    print("두 선 길이가 같습니다.")

else:
    print("모릅니다.")
    
del(myLine1)