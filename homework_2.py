def task_6():
    a, b, c = 11, 11,15
    if a == b == c:
        print("3")
    elif a == b or b == c or a == c:
        print("2")
    else:
        print("0")


def task_5():
    dict = []
    a = input()
    b = input()
    c = input()
    dict.append(a)
    dict.append(b)
    dict.append(c)
    s = sorted(dict)
    print(s)


def task_4():
    a = 3
    b = 4
    c = 5
    if a+b>c and b+c>a and c+a>b:
        print("Yes")
    else:
        print("No")


def task_3():
    year = 1234
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        print("Yes")
    else:
        print("No")


def task_2():
    a = 25
    b = 6
    c = 123
    n = 125
    d = 12.6
    num = 123.345
    hip = (a**2 + b**2)**(1/2)
    print("2.1 Длинна гипотенузы с катетами", a, "и", b, "равна =", hip)
    des = a//10
    print("2.2 Число десятков в двухзначном числе", a, "=", des)
    sum = c//100 + c % 10 + (c//10) % 10
    print("2.3 Сумма цифр в трехзначном числе", c, "=", sum)
    if n % 2 == 0:
        print("2.4 Число парное. по этому выведу его же",n)
    else:
        print("2.4 Число не парное по этому вывожу следующее за ним",n+1)
    print("2.5 дробная часть числа", d, "=", d % 1)
    if num//1 == 0:
        print(num*10//1)
    else:
        print(int((10*(num - (num//1))//1)))


def task_1():
    s = "as df.gfg hf.hj"
    hm = "Homework"
    ll = "a dfg rth dfgn sdgfh "
    s.isalnum()
    a = s.count(" ")
    b = s.count(".")
    c = hm.center(100)
    d = ll.title()
    print(a,"\n", b, "\n", c, "\n", d, "\n")





# task_6()
# task_5()
# task_4()
# task_3()
# task_2()
task_1()