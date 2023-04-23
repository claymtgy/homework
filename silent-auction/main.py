from art import art
import os


print(art)
print("Welcome to the silent auction!")

taking_bids = True

bids_dict = {}

highest_bid = 0
highest_bidder = ""
highest_bidder_dict = {}

def find_highest_bid(dictionary):
    global highest_bid
    global highest_bidder
    global highest_bidder_dict
    for key in dictionary:
        if dictionary[key] > highest_bid:
            highest_bid = dictionary[key]
            highest_bidder_dict = {f"{key}": dictionary[key]}
            highest_bidder = key
    
while taking_bids:
    key = input("Enter the name of the bidder: ")
    bid = int(input("Enter the bid amount: $"))
    bids_dict[key] = bid
    os.system('clear')
    new_bidder = input("Is there another bidder? y/n\n")
    os.system('clear')
    if new_bidder.lower() == "n":
        taking_bids = False

find_highest_bid(bids_dict)
print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}") 
