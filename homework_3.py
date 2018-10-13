def task_9_distance(x1, x2, y1, y2):
    l = (x1-x2)**2 + (y1-y2)**2
    return l


def task_8_word():
    while True:
        ll = input("print word without space\n\r")
        ll = ll.strip()
        if " " in ll:
            print ("again\n\r")
        else:
            print("good job")
            return ll


def task_8_number():
    while True:
        num = input("print the number\n\r")
        if not num.isdigit():
            print("again")
        else:
            print("good job")
            return num


def task_7(a, b, c):
    if a == b and b == c and c == a:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Versatile triangle")


def task_6_1(year):
    if year % 4 == 0 and year%100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def task_6_2(a,b,c):
    if a+b > c and b+c > a and c+a > b:
        return True
    else:
        return False


def task_5_1(ll):

    a = ll.replace("\n", " ").split(" ")
    print("количество слов в сроке",len(a))


def task_5_2(ll):
    # a = ll.replace("\n", " ").split(" ")
    for word in ll:
        ls = word.strip(".").strip("!").strip("(").strip(")")
        return ls


def task_5_3(ll):
    a = ll.replace("\n", " ").split(" ")
    a.sort()
    return a


def task_4_1(k):
    """Три способа выполнения задачи, через два разных цикла и метод pop"""
    # while k:
    #     k.pop(0)
    #     print(k)
    for _ in range(len(k)):
        k = k[1:]
        # k.pop(0)
        print(k)


def task_4_2(ll):
    while ll:
        ll = ll[1:]
        print(ll)


def task_4_3(k):
    for _ in range(len(k)):
        k.sort()
        k = k[1:]
        print(k)


def task_3():
    a = 0
    while a<11:
        print(a, end=" ")
        a += 1

    print("\n")

    b = 20
    while b > 0:
        print(b, end=" ")
        b -= 1


def task_2():
    p = input("Print string ")
    if len(p) % 2 == 0:
        z = p[:int(len(p)/2)]
        r = p[int(len(p)/2):]
        print(r+z)
    else:
        z = p[:(int(len(p)/2+1))]
        r = p[int((len(p)/2+1)):]
        print(r+z)



def task_1():
    g = input("print str >10 ")
    try:
        len(g) > 10
    except:
        print("to short")

    print(g[2], g[-2], g[:5], g[:-2:1], g[::2], g[1::2], g[::-1], g[::-2], g[len(g)-2:0:-1], len(g), sep="\n")


ll = """We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
(Football Coach)"""

k = [12, 34, 2, 123, 3, 5, 4, 9]

#  task_8_word()
# task_8_number()
#  task_5_2(ll)
#  task_5_3(ll)
#  task_4_1(k)
#  task_4_2(ll)
#  task_4_3(k)
#  task_3()
# task_2()
task_1()
