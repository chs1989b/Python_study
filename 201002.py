shirt_size = ["XS", "S", "S", "M", "L", "XL", "XXL"]
XS = []
S = []
M = []
L = []
XL = []
XXL = []

def SS(shirt_size):
    for i in shirt_size:
        if i == "XS":
            XS.append("XS")
        if i == "S":
            S.append("S")
        elif i == "M":
            M.append("M")
        elif i == "L":
            L.append("L")
        elif i == "XL":
            XL.append("XL")
        elif i == "XXL":
            XXL.append("XXL")
    print(len(XS))
    print(len(S))
    print(len(M))
    print(len(L))
    print(len(XL))
    print(len(XXL))

print(SS(shirt_size))