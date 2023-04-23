import random, os
from art import logo, vs
from game_data import data

'''
Select a random piece of data from list
Remove item from selectable list
Parse dictionary
Hide follower count, show the rest
Assign dictionaries as A and B
Take user input 
Keep user score
Check if user is correct and add to score if so
Repeat until all data has been gone through
'''

loop_amount = len(data)

#use random shuffle
random.shuffle(data)

def game():
    score = 0
    first_round = True
    random.shuffle(data)
    first_data = data[0]
    a_name = first_data["name"]
    a_description = first_data["description"]
    a_country = first_data["country"]
    a_follower_count = first_data["follower_count"]
    while first_round:
        print(logo)
        first_round = False

    for i in data:
        second_data = i
        #print(i)
        b_name = i["name"]
        b_description = i["description"]
        b_country = i["country"]
        b_follower_count = i["follower_count"]
        if b_name == a_name:
            pass
        else:
            score += round(a_name, a_description, a_country, a_follower_count, second_data, score)
            a_name = b_name
            a_description = b_description
            a_country = b_country

def round(a_name, a_description, a_country, a_follower_count, second_data, score):
    print(f"Contender A:\n")
    print(f"Name: {a_name}")
    #print(f"follower count: " + str(first_data["follower_count"]))
    print(f"Description: {a_description}")
    print(f"Country of Origin: {a_country}")
    print(vs)
    print(f"Contender B:\n")
    print(f"Name: " + second_data["name"])
    #print(f"Follower Count: " + str(second_data["follower_count"]))
    print(f"Description: " + second_data["description"])
    print(f"Country of Origin: " + second_data["country"])
    choice = input("Who has the higher follower count? Type A or B:\n") 
    if a_follower_count > second_data["follower_count"]:
        correct_answer = "a"
    else:
        correct_answer = "b"
    if choice.lower() == correct_answer:
        print(f"\n\nCorrect! Your score is now " + str((score + 1)) + "\n\n")
        return 1
    else:
        print(f"\n\nIncorrect. Your score is still {score}\n\n-------------------------------------------------------------------------\n\n")
        return 0


game()
