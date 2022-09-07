else:

    while True:
        e = input("제대로 입력해주시겠어요?  ")
        if e.isdigit():
            break
        elif e == "1999" or e == "1999년":



a = ["나는", 23, 5.25, "234"]
for i in a:    try:        float(i)        a.remove(i)    except:        pass
print(a)