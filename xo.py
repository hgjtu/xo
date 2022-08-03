def board():
    for i in m:
        for j in i:
            print(j, end = '   ')
        print()
        print()
        
def play(key, symbol):
    x = key % 3 - 1
    y = (key - 1) // 3
    if 1<= key <= 9 and m[y][x] == key:                         
        m[y][x] = symbol
        board()
        check(x, y, symbol)
    else:
        print('Некорректный ввод. Повторите попытку.')
        play(int(input()), symbol)

def check(x, y, symbol):
    global key
    if m[y][0] == m[y][1] == m[y][2] == symbol:
        print('Победа ', symbol)
        key = 'stop'
    elif m[0][x] == m[1][x] == m[2][x] == symbol:
        print('Победа ', symbol)
        key = 'stop'
    elif m[0][0] == m[1][1] == m[2][2] == symbol:
        print('Победа ', symbol)
        key = 'stop'
    elif m[0][2] == m[1][1] == m[2][0] == symbol:
        print('Победа ', symbol)
        key = 'stop'



m = [[1, 2, 3], [4, 5,6], [7, 8,9]]
board()
key = 1
t = 0
while key != 'stop':
    t += 1
    if t % 2 != 0:
        symbol = 'X'
    else:
        symbol = 'O'
    key = int(input(symbol))
    play(key, symbol)
    if t == 9 and key != 'stop':
        print('Ничья')
        key = 'stop'
        
    

