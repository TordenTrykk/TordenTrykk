def greet():
    print("-----------------------------")
    print("-Welcome to tic tac toe game-")
    print("---------input X and Y------- ")
    print("----X is horisontal line-----")
    print("-----Y is vertical line------ ")
    print("----------------------------- ")
greet()

field = [[" "] * 3 for i in range(3) ]

def show():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")

show()

def ask():
    while True:
        cords = input("         Your move: ").split()
        
        if len(cords) != 2:
            print(" Input two cords! ")
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Input digits! ")
            continue
        
        x, y = int(x), int(y)
        
        if 0 > x or x > 2 or  0 > y or  y > 2 :
            print(" Cords out of space! ")
            continue
        
        if field[x][y] != " ":
            print(" Field is full! ")
            continue
        
        return x, y
            
ask()

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Winner is X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Winner is 0!!!")
            return True
    return False

field = [
    [" ", "X", " "],
    [" ", "X", " "],
    [" ", "X", " "]
]

check_win()

greet()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" X to move!")
    else:
        print(" 0 to move!")
    
    x, y = ask()
    
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    
    if check_win():
        break
    
    if count == 9:
        print(" Draw!")
        break