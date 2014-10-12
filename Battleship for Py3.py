#-------------------------------------------------------------------------------
# Created:     22/02/2014
# Copyright:   (c) Mel 2014
#-------------------------------------------------------------------------------

from random import randint

board = []
ships = 2
ship_list = []  # example [ [ [0,0],[0,1] ],[ [1,1] ] ] is two ships


def print_board():
    for row in board:
        print((" ".join(row)))


def check_vert(x, y, length):
    # if overlaps
    for n in range(x, x + length):
        if contains(n, y):
            return True
    # if doesn't overlap
    return False


def check_horiz(x, y, length):
    # if overlaps
    for n in range(y, y + length):
        if contains(x, n):
            return True
    # if doesn't overlap
    return False


def add_vertical(x, y, length, ship_id):  # adds a vertical ship
    for n in range(x, x + length):
        ship_list[ship_id].append([n, y])
        #print(ship_list[ship_id])


def add_horizontal(x, y, length, ship_id):  # adds a horizontal ship
    for n in range(y, y + length):
        ship_list[ship_id].append([x, n])
        #print(ship_list[ship_id])


def get_input(text):  # checks if input can be converted to an integer and does so
    while True:
        inp = input(text)
        print(inp)
        try:
            int(inp)
        except ValueError:
            print("Not a number")
        else:
            return int(inp)


def contains(x, y):  # checks if you hit a ship;
    for ship in ship_list:
        #print(ship)
        if [x, y] in ship:
            return True
    return False


def ship_is_sunk(x, y):  # check if ship with that id has been sunk
    # find index of ship hit
    for ship in ship_list:
        if [x, y] in ship:
            ship_id = ship_list.index(ship)
    # get all points of that ship and compare with board
    for point in ship_list[ship_id]:
        if not board[point[0]][point[1]] == "S":
            return False
    # if all points == "S"
    return True


def create_ships():  # create all ships
    current_ships = 0
    while current_ships < ships:
        ship_list.append([])  # create new ship as empty list (otherwise adding coordinates won't work)
        ship_len = randint(2, len(board))  # min size 2
        direction = randint(1, 2)  # 1 - vertical down 2 - horizontal right
        for n in range(10):  # fitting in a ship of chosen length
            ship_row = randint(0, len(board) - ship_len)  # starting point
            ship_col = randint(0, len(board) - ship_len)
            if direction == 1 and ship_row + ship_len <= len(board):  # if vertical and fits board
                if not check_vert(ship_row, ship_col, ship_len):
                    add_vertical(ship_row, ship_col, ship_len, current_ships)
                    current_ships += 1
                    break
            if direction == 2 and ship_col + ship_len <= len(board):
                if not check_horiz(ship_row, ship_col, ship_len):
                    add_horizontal(ship_row, ship_col, ship_len, current_ships)
                    current_ships += 1
                    break
    return current_ships


def play(current_ships):
    for turn in range(20):  # runs for 20 turns
        print("Turn %i" % (turn + 1))
        #print(ship_list)  # I'm cheating!
        guess_row = get_input("Guess Row:")
        guess_col = get_input("Guess Col:")

        if guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "S":
            print("You guessed that one already.")
        elif contains(guess_row, guess_col):  # if hit
            print("Bang! You hit something!")
            board[guess_row][guess_col] = "S"
            if ship_is_sunk(guess_row, guess_col):
                current_ships -= 1
                print("Congratulations! You sunk my battleship! %s ship(s) left" % current_ships)
            if current_ships == 0:
                print_board()
                print("You won!")
                break
        else:  # if miss
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 19:
            print("Game Over. You lose.")
        print_board()


def main():
    for x in range(5):  # create board
        board.append(["O"] * 5)
    print("Let's play Battleship!")
    print_board()
    current_ships = create_ships()
    #print(current_ships)
    play(current_ships)

    return


if __name__ == '__main__':
    main()
