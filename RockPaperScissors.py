#!/usr/bin/env python3
import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = "none"
    their_move = "none"

    def move(self):
        pass

    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, Paper, Or Scissors?\n").lower()
            if move in moves:
                return move
                break
            else:
                print("Im sorry what was that?")


class ReflectPlayer(Player):
    def move(self):
        if self.my_move == "none":
            return random.choice(moves)
        else:
            return self.my_move


class CyclePlayer(Player):
    def move(self):
        if self.their_move == "none":
            return random.choice(moves)
        elif self.their_move == "rock":
            return "paper"
        elif self.their_move == "paper":
            return "scissors"
        else:
            return "rock"


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        self.tie = 0
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            self.p1_score += 1
            print(f"Player 1 wins!\n")
        elif beats(move2, move1) is True:
            self.p2_score += 1
            print(f"Player 2 wins!\n")
        else:
            print("TIE!... REMATCH!")
            self.tie = 1
        print(f"Player 1:{self.p1_score}\nPlayer 2:{self.p2_score}\n\n")
        time.sleep(5)

    def play_game(self):
        print("Game start!")
        round = 1
        while round < 4:
            print(f"Round {round}:\n")
            time.sleep(3)
            self.play_round()
            round += 1
            if self.tie == 1:
                round -= 1
        if self.p1_score > self.p2_score:
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
        print("Game over!")


if __name__ == '__main__':
    p1 = HumanPlayer()
    p2 = CyclePlayer()
    game = Game(p1, p2)
    game.play_game()
