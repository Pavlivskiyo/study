def task_1(count_str=3, count_la=3, num=0):
    if num == 0:
        l = "\n"+"la"*count_str
        print(l*count_la+".")
    elif num == 1:
        l = "\n"+"la"*count_str
        print(l*count_la+"!")


def task_2(*args):
    l = []
    l.extend(args)
    l = set(l)
    k = sorted(l)
    print(k[1])


def sort_last(tuples):
  l = sorted(tuples, key=lambda x: x[0])
  print(l)


task_2(100, 4, 6, 7, 8, 23, 2, 34, 4, 5, 6, 34, 2)
tuple = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
sort_last(tuple)

# k = ["1", "22", "3", "33", "4", "335", "221"]
# print(sorted(k, key=lambda x: int(x)))
