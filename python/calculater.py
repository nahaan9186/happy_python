while True :
    a = int(input("숫자 : "))
    b = input("기호 : ")
    c = int(input("숫자 : "))

    if b == '+':
        print(f"{a} + {c} = {a+c}")
    elif b == '-':
        print(f"{a} - {c} = {a-c}")
    elif b == '*':
        print(f"{a} * {c} = {a*c}")
    elif b == '/':
        print(f"{a} / {c} = {a/c}")

    
    res = input('종료하시겠습니까? y/n \n')
    if res == 'y':
        break
    elif res == 'n':
        continue
    else:
        print(f"{res} 말고 y 아니면 n 을 누르라구요")

