list = []

def A(pos, elem):
    list.insert(pos-1, elem)
def P():
    print(list)
def D(pos):
    list.pop(pos-1)
def G(pos):
    if pos-1 < int(len(list)):
        print(list[pos-1])
    if pos-1 >= int(len(list)):
        print("invalid position")

print("예제.1") #연산의 개수:5 ????
A(1,'s')
A(2,'t')
A(3,'r')
A(3,'a')
P()

print("예제.2")
# A(1, 'D')
# A(2, 'a')
# A(3, 'y')
# D(1)
# P()
# G(3)
# A(1, 'S')
# G(3)