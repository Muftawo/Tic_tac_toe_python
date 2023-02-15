from typing import Type
import random


class Board:
    def __init__(self):
        self.check = '_'

        self.board = {i:self.check for i in range(1,10)}
        print(self.board)

    def show_board(self):
        print()
        print(self.board[1]," | ",self.board[2]," | ",self.board[3])
        print("---------------")
        print(self.board[4]," | ",self.board[5]," | ",self.board[6])
        print("---------------")
        print(self.board[7]," | ",self.board[8]," | ",self.board[9])
        print()



class Game:

    def __init__(self):
        player_1 = input("Player 1 pick your symbol ")

        player_2 = input("Player 2 pick your symbol ")
        self.players = {player_1:"1" , player_2:"2"}
        while player_2 == player_1:
            print(f"Make sure you pick a different symbol \n Player has picked {player_1}")
            player_2 = input("Player 2 pick your symbol ")



        self.player_1,self.player_2 = player_1, player_2
        print(f"Player 1: %s" % self.player_1 , "Player 2: %s" % self.player_2 )
        self.current_player = self.player_1
        self.game_board = Board()

    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1
        return self.current_player

    def is_valid_move(self, position):
        return self.game_board.board[position] == self.game_board.check


    def is_draw(self):
        for key in self.game_board.board.keys():
            if self.game_board.board[key] == self.game_board.check:
                return False
        return True



    def next_move(self):
        self.current_player = self.switch_player()
        self.game_board.show_board()

        position = input(f"Player {self.players[self.current_player] } Enter position between 0-9: ")
        while position not in list(str(i) for i in range(1,10)):
            print("Position not valid ")
            print("Enter position between 0-9:")
            position = input(f"Player {self.players[self.current_player] } Enter position between 0-9: ")

        position = int(position)

        self.take_position(position)

    def take_position(self, position):
        if self.is_valid_move(position) :
            self.game_board.board[position] = self.current_player
            # self.game_board.show_board()
            if self.is_draw():
                self.game_board.show_board()
                print("Drawn Game!")
                exit()
            if self.checkWin():
                self.game_board.show_board()
                print(f"Player {self.players[self.current_player]} wins!")
                exit()
            return
        else:
            print("Invalid position")
            position = int(input(f" Player {self.players[self.current_player]} please enter a new position : " ))
            self.take_position(position)
            return



    def checkWin(self):
        board= self.game_board.board
        if (board[1] == board[2] and board[1] == board[3] and board[1] != self.game_board.check):
            return True
        elif (board[4] == board[5] and board[4] == board[6] and board[4] != self.game_board.check):
            return True
        elif (board[7] == board[8] and board[7] == board[9] and board[7] != self.game_board.check):
            return True
        elif (board[1] == board[4] and board[1] == board[7] and board[1] != self.game_board.check):
            return True
        elif (board[2] == board[5] and board[2] == board[8] and board[2] != self.game_board.check):
            return True
        elif (board[3] == board[6] and board[3] == board[9] and board[3] != self.game_board.check):
            return True
        elif (board[1] == board[5] and board[1] == board[9] and board[1] != self.game_board.check):
            return True
        elif (board[7] == board[5] and board[7] == board[3] and board[7] != self.game_board.check):
            return True
        else:
            return False


    def play_game(self):
        while not self.checkWin():
            self.next_move()


my_game = Game()
my_game.play_game()

