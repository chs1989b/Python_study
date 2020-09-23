items = []

def insert(pos, elem) :
   items.insert(pos, elem)

def delete(pos) :
   items.pop(pos)

def getEntry(pos): return items[pos]

def isEmpty( ): return len(items) == 0

def size( ):	    return len(items)
def clear( ):      items = []

def find(item) : return items.index(item)
def replace(pos, elem): items[pos] = elem
def sort() : items.sort()
def merge(lst) : items.extend(lst)

def display(msg='ArrayList:' ):
    print(msg, size(), items)

#사진의 결과 화면 구현
insert(1, 's')
insert(2, 't')
insert(3, 'r')
insert(3, 'a')
display("list = ")
