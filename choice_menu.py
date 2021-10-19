# 1. 햄버거 단품 메뉴 선택하는 메서드
def choice_burger():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ BURGER MENU')
    print('□■ 1. 치즈버거: 3,500원')
    print('□■ 2. 불고기버거: 3,000원')
    print('□■ 3. 새우버거: 2,500원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

    while True:
        choice_num = int(input('>> 번호: '))
        if choice_num >= 1 and choice_num <= 3:
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_num



# 2. 사이드 단품 메뉴 선택하는 메서드
def choice_side():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ SIDE MENU')
    print('□■ 1. 프렌치프라이: 1,500원')
    print('□■ 2. 치킨너겟: 2,000원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

    while True:
        choice_side_menu_num = int(input('>> 번호: '))
        if choice_side_menu_num >= 1 and choice_side_menu_num <= 2:
            break
        else:
            print('# MSG: 1~2의 번호만 입력해주세요 :)')
    return choice_side_menu_num

# 3. 음료 단품 메뉴 선택하는 메서드
def choice_drink():

    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ DRINK MENU')
    print('□■ 1. 코카콜라: 1,000원')
    print('□■ 2. 커피: 1,200원')
    print('□■ 3. 주스: 1,500원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    while True:
        choice_drink_num = int(input('>> 번호: '))
        if choice_drink_num >= 1 and choice_drink_num <= 3:
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_drink_num