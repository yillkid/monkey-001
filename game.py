import random

list_players = [{"name":"蕃薯", "balance":0}, {"name":"芋頭", "balance":0}, {"name":"南瓜", "balance":0}]

list_chance = []
list_destiny = []

def set_balance(description):
    list_command = description.split("本金")

    for obj in list_players:
        if list_command[0] == obj["name"]:
            obj["balance"] = list_command[1]

def dice():
    return random.randint(1, 6)

def increase(description):
    list_command = description.split("增加")
    for obj in list_players:
        if list_command[0] == obj["name"]:
            if list_command[1].isdigit():
                obj["balance"] = int(obj["balance"]) + int(list_command[1])

def decrease(description):
    list_command = description.split("減少")
    for obj in list_players:
        if list_command[0] == obj["name"]:
            if list_command[1].isdigit():
                obj["balance"] = int(obj["balance"]) - int(list_command[1])
