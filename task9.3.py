lst=set(eval(input("enter lst")))
num=int(input("enter num"))
for i in range(len(lst)):
    if num==i:
        lst.remove(num)
        print(lst)