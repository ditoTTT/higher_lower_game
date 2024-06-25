from game_data import data 
from random import randint
from art import logo, vs

def first_celebrity():
    """Function return random celebrity from data"""
    random_num1 = randint(1, 49)
    first_celeb = data[random_num1]
    lis = []
    for x,y in first_celeb.items():
        lis.append(y)
    return lis
first_choice = first_celebrity()

def second_celebrity():
    """Function return random celebrity from data"""
    random_num2 = randint(1, 49)
    first_celeb = data[random_num2]
    lis = []
    for x,y in first_celeb.items():
        lis.append(y)
    return lis
second_choice = second_celebrity()

def compare(first, second):
    """Compare two celebrities and update the score"""
    player_score = 0
    success_loop = True
    while success_loop:
        comparasion_quesiton = input(f'{logo}\nCompare A: {first[0], first[2], first[3]}\n{vs}\nAgainst B: {second[0], second[2], second[3]}\nWho has more followers? Type "A" or "B" : ')
        if comparasion_quesiton == 'A' and first[1] > second[1]:
            player_score += 1
            third = second
            first = third
            second = second_celebrity()  
        elif comparasion_quesiton == 'B' and second[1] > first[1]:
            player_score += 1
            third = second
            first = third
            second = second_celebrity()
        else:
            print(f'Your score is {player_score}\nGame over')
            success_loop = False
comp = compare(first_choice, second_choice)