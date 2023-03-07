def greet():
    print("-----------------------------")
    print("-Welcome to tic tac toe game-")
    print("---------input X and Y------- ")
    print("----X is horisontal line-----")
    print("-----Y is vertical line------ ")
    print("----------------------------- ")
greet()

field = [["[ ]"] * 3 for i in range(3) ] 

def show():
    print(f"   0   1   2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")

show()

