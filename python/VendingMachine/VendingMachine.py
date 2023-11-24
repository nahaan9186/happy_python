def input_cash():
    # 돈 넣기
    cash = int(input('돈을 넣어주세요 : \n'))
    if cash < 500 :
        print('거지에게 제공할 음료는 없습니다')
    else:
        print('어서오세요 고객님 무엇을 도와드릴까요?')
    return cash

def menu(money):
    # 메뉴 가격 설정
    콜라가격 = 500
    사이다가격 = 600
    닥터페퍼가격 = 700
    잔돈 = money

    # 메뉴판 출력
    print('========================================')
    print(f"콜라 : {콜라가격}원")
    print(f"사이다 : {사이다가격}원")
    print(f"닥터페퍼 : {닥터페퍼가격}원")
    print('========================================')
    
    # 주문 받기
    choice = input('무엇을 주문하시겠습니까? : \n')
    if choice == '콜라': 
        if money < 콜라가격:
            print('투입한 금액이 부족합니다')
        else:
            잔돈 = money - 콜라가격
            print(f"주문하신 {choice} 드리겠습니다")
    elif choice == '사이다':
        if money < 사이다가격:
            print('투입한 금액이 부족합니다')
        else:
            잔돈 = money - 사이다가격
            print(f"주문하신 {choice} 드리겠습니다")
    elif choice == '닥터페퍼':
        if money < 닥터페퍼가격:
            print('투입한 금액이 부족합니다')
        else:
            잔돈 = money - 닥터페퍼가격
            print(f"주문하신 {choice} 드리겠습니다")
    else:
        print('그런 메뉴는 없습니다')

    # 거스름돈 돌려주기
    return 잔돈
        
def change_and_exit(잔돈):
    # 잔돈 출력
    print(f"거스름돈 {잔돈}원 드리겠습니다")
    print('========================================')
    return


while True:  # 무한 루프
    money = input_cash()  # 사용자 입력 받기
    if money < 500:
        최종잔돈 = money
    else:
        최종잔돈 = menu(money)  # 입력된 값 출력하기
    
    change_and_exit(최종잔돈)
    
    # 루프 탈출 조건
    exit_command = input("계속하려면 엔터를 누르고, 종료하려면 'exit'을 입력하세요: ")
    if exit_command == 'exit':
        break