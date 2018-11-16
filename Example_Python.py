print(1 + 1)  # returns 2
print(1 - 1)  # returns 0
print(1 * 2)  # returns 2
print(2 / 2)  # returns 1.0
print(2 // 2)  # returns 1
print("number" + str(int("1")))


class Class:
    def __init__(self, name="name", age=17):
        self.n = name
        self.a = age

    def __str__(self):
        return str(self.n) + " " + str(self.a)


class SubClass(Class):
    def __init__(self, n="name", a=13, h=False):
        super(SubClass, self).__init__(n, a)
        self.h = h

    def __str__(self):
        str = super(SubClass, self).__str__() + " "
        str += "Has Hair" if self.h else "Does Not Have Hair"
        return str


# list, queue, stack
list = []
list.append(1)
list.append(2)
list.append(3)
print(list)
print(list[1])
list.remove(list[1])
print(list)
print(list.pop())
print(list)

# tuples
t = 1, 2, 3
a, b, c = t
print(t, a, b, c)

list.clear()
for i in range(0, 17, 2):
    list.append(i)
for x in list:
    print(x)
print(list)
if __name__ == "__main__":
    bob = Class("bob")
    bob.virgin = True
    print(bob.n, bob.a)
    print(bob.virgin)
#     sub_bob = SubClass("bob", 17)
#     print(str(bob))
#     print(str(sub_bob))
#     sub_bob.h = True
#     print(str(sub_bob))
board = []
w = 1
b = 0
wr = [w, b, w, b, w, b, w, b]
br = [b, w, b, w, b, w, b, w]
front = []
for i in range(8):
    front.append(2)
back = [3, 4, 5, 6, 8, 5, 4, 3]
board.append(back)
board.append(front)
for i in range(0, 2):
    board.append(br)
    board.append(wr)
board.append(front)
board.append(back)
# pawn == 2


#for row in board:
#   print(row)

