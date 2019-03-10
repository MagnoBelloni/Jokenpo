#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
# Importa para gerar um número aleátorio
from random import randint

moves = ['rock', 'paper', 'scissors']
jogadaAnterior = None
jogadaPlayer = ""
pontuacaoPlayer, pontuacaoOponente = 0,0
"""The Player class is the parent class for all of the Players
in this game"""



class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    # Movimento randomico
    def move(self):
        return moves[randint(0,2)]

class HumanPlayer(Player):
    def move(self):     
        while True:
            jogada = input("rock, paper, scissors?")
            for value in moves:
                if jogada == value or jogada == "quit":
                    return jogada        
    
    def learn(self, my_move, their_move):
        global jogadaPlayer
        jogadaPlayer = my_move

class ReflectPlayer(Player):
    def move(self):
        global jogadaAnterior
        if jogadaAnterior != None:
            return jogadaAnterior
        else:
           return RandomPlayer.move(self)
    
    def learn(self, my_move, their_move):
        global jogadaAnterior
        jogadaAnterior = their_move

class CyclePlayer(Player):
    def move(self):
        global jogadaAnterior
        if jogadaAnterior != None:
            for jogada in moves:
                if jogada != jogadaAnterior:
                    return jogada
        else:
           return RandomPlayer.move(self)
    
    def learn(self, my_move, their_move):
        global jogadaAnterior
        jogadaAnterior = my_move

def beats(one, two):    
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        global pontuacaoPlayer, pontuacaoOponente
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nSua jogada 1: {move1} \nOponente:     {move2}")

        #Testa e exibe resultado
        if move1 == "quit":
            print("Você escolheu sair")
        elif (move1 == move2):
            print("Empate")
        elif beats(move1,move2):
            print("Você venceu!!")
            pontuacaoPlayer+=1
        else:
            print("Oponente venceu!!")
            pontuacaoOponente+=1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!") 
        print("Digite 'quit', para sair ou espere até que um jogador esteja três pontos à frente.")      
        round = 1                 
        while True:
            print(f"\nRound {round}:")            
            self.play_round()
            round+=1
            if pontuacaoPlayer >= pontuacaoOponente+3 or pontuacaoPlayer+3 <= pontuacaoOponente or jogadaPlayer == "quit":
                break
        #Mostra placar
        print(f"Pontuação:\nPlayer:{pontuacaoPlayer}\nOponente:{pontuacaoOponente}")
        #Anuncia vencedor
        if pontuacaoPlayer > pontuacaoOponente:
            print("Você ganhou!!")
        elif(pontuacaoPlayer == pontuacaoOponente):
            print("Empate!!")
        else:
            print("Oponente ganhou!!")
        print("End Game")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
