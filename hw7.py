shopping_bag = {}

while True:
    item = input('상품명? ')
    if item == '':
        break
    quantity = int(input('수량은? '))
    shopping_bag[item] = quantity
    print('장바구니에 {0} {1}개가 담겼습니다.'.format(item, quantity))

print('>>> 장바구니 보기:', shopping_bag)

print('[검색]')
search_item = input('장바구니에서 확인하고자 하는 상품은? ')
if search_item in shopping_bag:
    print('{0}은(는) {1}개 담겨 있습니다.'.format(search_item, shopping_bag[search_item]))

  