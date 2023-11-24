
while True :
    said = input('입력해주세요 : \n')
    print(f"당신의 입력은 : {said}")
    res = input('종료하시겠습니까? y/n \n')
    if res == 'y':
        break
    elif res == 'n':
        continue
    else:
        print(f"{res} 말고 y 아니면 n 을 누르라구요")

