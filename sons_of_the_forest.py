import random as rand
import time
import sys

# TODO: 1 create variables of the game (health, attack, difficulty)

encounters = ["none", "sticks", "lighter", "bottle of water", "rabbit", "chest", "enemy", "exit"]
chest_encounters = {"fruit": {"thirst": 10, "hunger": 15},
                    "gun": {"health": 0, "attack": 40},
                    "knife": {"health": 0, "attack": 25},
                    "bandage": {"health": 10, "attack": 0},
                    "med_kit": {"health": 50, "attack": 0},
                    "baseball_bat": {"health": 0, "attack": 15},
                    }
enemy_encounters = {}
user_inventory = []
routes = {1: "forest", 2: "cave", 3: "beach"}
name = ""
user_health = 70
user_attack = 5
user_thirst = 80
user_hunger = 80
user_weapon = ()


def introduction():
    """Introduction and Story"""
    print("Welcome to the game Lost in an Island by Denzel Balbosa")
    time.sleep(1)
    print("This game is inspired by the game Sons of The Forest")
    time.sleep(1)
    print("The game offers different difficulty levels and diverse outcomes based",
          "on the player's actions and decisions throughout the gameplay.")
    print()
    time.sleep(2)
    print("+", "-" * 80, "+")
    print("You and your friends are aboard a helicopter, excitedly anticipating a vacation.")
    print("Suddenly, mid-flight, the helicopter is struck by something, causing it to crash onto an island.")
    print("Miraculously, you survive the crash, but after looking around,", end="")
    print("you realize that everyone else did not survive.")
    print("Stranded on this island, you now face the daunting task of surviving.")
    print("Do you have the courage to begin?")
    print("+", "-" * 80, "+")

    while True:
        user_input = str(input("Please enter \'Yes\' to start or \'No\' to Quit: ").lower())

        if user_input == 'yes' or user_input == 'y':
            print("Game starting...")
            game_start()
            break
        elif user_input == 'no' or user_input == 'n':
            print("Quitting game...")
            sys.exit()
        else:
            print("\nYou entered an invalid keyword.\n")
            time.sleep(1)


def choose_difficulty():
    while True:
        difficulty = int(input("Please choose a difficulty(1 for Easy, 2 for Moderate or 3 for Hard): "))
        if difficulty == 1:
            enemy_encounters.update({
                "Large Cannibal": {"Health": 50, "Attack": 6},
                "Cannibal": {"Health": 40, "Attack": 4},
                "Scary_monkey": {"Health": 20, "Attack": 2},
            })
            break
        elif difficulty == 2:
            enemy_encounters.update({
                "Large Cannibal": {"Health": 60, "Attack": 8},
                "Cannibal": {"Health": 50, "Attack": 6},
                "Scary monkey": {"Health": 25, "Attack": 3},
            })
            break
        elif difficulty == 3:
            enemy_encounters.update({
                "Alien": {"Health": 100, "Attack": 40},
                "Large Cannibal": {"Health": 70, "Attack": 10},
                "Cannibal": {"Health": 60, "Attack": 8},
                "Scary monkey": {"Health": 30, "Attack": 4},
            })
            break
        else:
            print("\nYou entered an invalid input.\n")
            time.sleep(1)

    return difficulty


def update_status(added_health=0, added_attack=0, decreased_health=0, decreased_attack=0,
                  added_hunger=0, added_thirst=0, decreased_hunger=0, decreased_thirst=0):
    global user_health
    global user_attack
    global user_thirst
    global user_hunger

    user_health += added_health
    if user_health > 100:
        user_health = 100
    user_thirst += added_thirst
    if user_thirst > 100:
        user_thirst = 100
    if user_thirst <= 0:
        user_thirst = 0
    user_hunger += added_hunger
    if user_hunger > 100:
        user_hunger = 100
    if user_hunger <= 0:
        user_hunger = 0
    user_attack += added_attack
    user_health -= decreased_health
    user_attack -= decreased_attack
    user_thirst -= decreased_thirst
    user_hunger -= decreased_hunger


def user_route_update(current_route):
    while True:
        if current_route == 0 or current_route == 3:
            current_route = int(input("Press \'1\' to explore the forest or "
                                      "press \'2\' to explore the cave: "))
            if current_route == 0 or current_route == 3:
                print("\nYou entered an invalid input.\n")
                time.sleep(1)
            else:
                break
        elif current_route == 1:
            current_route = int(input("Press \'2\' to explore the cave or "
                                      "press \'3\' to explore the beach: "))
            if current_route == 0 or current_route == 1:
                print("\nYou entered an invalid input.\n")
                time.sleep(1)
            else:
                break
        elif current_route == 2:
            current_route = int(input("Press \'1\' to explore the forest or "
                                      "press \'3\' to explore the beach: "))
            if current_route == 0 or current_route == 2:
                print("\nYou entered an invalid input.\n")
                time.sleep(1)
            else:
                break
        else:
            print("\nYou entered an invalid input.\n")
            time.sleep(1)

    return current_route


# Fix added weapon from chest encounters
def weapon_change(new_weapon):
    global user_attack
    global user_weapon
    user_added_attack = 0
    user_decreased_attack = 0

    if len(user_weapon) == 0:
        user_added_attack = new_weapon[1]["attack"]
        user_decreased_attack = 0
        user_weapon = new_weapon
    else:
        user_decreased_attack = user_weapon[1]["attack"]
        user_added_attack = new_weapon[1]["attack"]
        user_inventory.append(user_weapon)
        user_weapon = ()
        user_weapon = new_weapon

    print(user_weapon)

    update_status(added_attack=user_added_attack, decreased_attack=user_decreased_attack)


# encounters_action: fight, run,
# get random items after defeating enemy

def battle_encounter(enemy_type):
    chances = ["normal hit", "critical hit", "missed"]
    enemy_present = True
    enemy_health = enemy_type[1]["Health"]
    enemy_attack = enemy_type[1]["Attack"]

    print(f"You have encountered a {enemy_type[0]}!")

    while enemy_present:
        if not user_health <= 0:
            print("+", "-" * 80, "+")
            print(f"Player HP: {user_health}")
            print(f"Player Attack: {user_attack}")
            print("+", "-" * 80, "+")
            print(f"{enemy_type[0]} HP: {enemy_health}")
            print(f"{enemy_type[0]} Attack: {enemy_attack}")
            print("+", "-" * 80, "+")
            user_action = str(input("Press \'1\' to attack or \'2\' to run: "))

            if user_action == '1':
                user_chance = rand.choices(chances, weights=(60, user_attack, 30))
                if user_chance[0] == 'normal hit':
                    print(f"You attacked and dealt {user_attack} damage to the enemy.")
                    enemy_health -= user_attack
                elif user_chance[0] == 'critical hit':
                    print("Your attack was a critical hit!" 
                          f" You dealt {user_attack + (user_attack * 0.50)} to the enemy.")
                    enemy_health -= user_attack + (user_attack * 0.50)
                else:
                    print("You missed and dealt 0 damage to the enemy.")

                if not enemy_health <= 0:
                    enemy_chance = rand.choices(chances, weights=(60, enemy_attack, 30))
                    if enemy_chance[0] == 'normal hit':
                        print(f"The {enemy_type[0]} attacked and dealt {enemy_attack} damage to you.")
                        update_status(decreased_health=enemy_attack)
                    elif enemy_chance[0] == 'critical hit':
                        print(f"The {enemy_type[0]} attack was a critical hit!"
                              f" and dealt {enemy_attack + (enemy_attack * 0.50)} to you.")
                        update_status(decreased_health=enemy_attack + (enemy_attack * 0.50))
                    else:
                        print(f"The {enemy_type[0]} missed and dealt 0 damage to you.")

                else:
                    print(f"You killed the {enemy_type[0]}.")
                    enemy_present = False

            elif user_action == '2':
                enemy_chance = rand.choices(chances, weights=(30, enemy_attack, 60))
                if enemy_chance[0] == 'normal hit':
                    print(f"The {enemy_type[0]} attacked and dealt {enemy_attack} damage to you"
                          " while attempting to run.")
                    update_status(decreased_health=enemy_attack)
                elif enemy_chance[0] == 'critical hit':
                    print(f"The {enemy_type[0]} attacked and dealt a critical hit damage to you"
                          f" while attempting to run and dealt {enemy_attack + (enemy_attack * 0.50)} damage.")
                    update_status(decreased_health=enemy_attack + (enemy_attack * 0.50))
                else:
                    print(f"You successfully ran away from the {enemy_type[0]}.")
                enemy_present = False
            else:
                print("You entered an invalid key.")
        else:
            enemy_present = False


def rabbit_encounter(occurred):
    if occurred == 0:
        while True:
            use_item = str(input("Eat it, cook it or add it to inventory?"
                                 "(Press \'1\' to eat, \'2\' to cook or \'3\' to add to inventory): "))
            if use_item == '1':
                print("You ate a raw rabbit and has affected your health.")
                update_status(added_hunger=30, decreased_health=10)
                break
            elif use_item == '2':
                if (any("lighter" in keys for keys in user_inventory)
                        and any("sticks" in keys for keys in user_inventory)):
                    print("Cooking 🕐...")
                    time.sleep(3)
                    for i in user_inventory:
                        if i[0] == "sticks":
                            user_inventory.remove(i)
                            break
                    while True:
                        use_item = str(input("The rabbit is cooked. Eat it or add it to inventory?"
                                             "(Press \'1\' to eat or \'2\' to add to inventory): "))
                        if use_item == '1':
                            update_status(added_hunger=50)
                            break
                        elif use_item == '2':
                            print("Cooked rabbit is added to your inventory.")
                            user_inventory.append(("cooked rabbit", {"thirst": 0, "hunger": 50}))
                            break
                        else:
                            print("You entered an invalid key.")
                    break
                else:
                    print("You don't have enough material to cook. You need sticks and a lighter.")
            elif use_item == '3':
                print("Raw rabbit is added to your inventory.")
                user_inventory.append(("raw rabbit", {"hunger": 30, "health decrease": 10}))
                break
            else:
                print("You entered an invalid key.")
    else:
        while True:
            use_item = str(input("Eat it or cook it?"
                                 "(Press \'1\' to eat or \'2\' to cook): "))
            if use_item == '1':
                print("You ate a raw rabbit and has affected your health.")
                update_status(added_hunger=30, decreased_health=10)
                break
            elif use_item == '2':
                if (any("lighter" in keys for keys in user_inventory)
                        and any("sticks" in keys for keys in user_inventory)):
                    print("Cooking 🕐...")
                    time.sleep(3)
                    for i in user_inventory:
                        if i[0] == "sticks":
                            user_inventory.remove(i)
                            break
                    while True:
                        use_item = str(input("The rabbit is cooked. Eat it or add it to inventory?"
                                             "(Press \'1\' to eat or \'2\' to add to inventory): "))
                        if use_item == '1':
                            update_status(added_hunger=50)
                            break
                        elif use_item == '2':
                            print("Cooked rabbit is added to your inventory.")
                            user_inventory.append(("cooked rabbit", {"thirst": 0, "hunger": 50}))
                            break
                        else:
                            print("You entered an invalid key.")
                    break
                else:
                    print("You don't have enough material to cook. You need sticks and a lighter.")
            else:
                print("You entered an invalid key.")


# Fix to actually remove item after use
def inventory_use():
    items = []
    for i in user_inventory:
        items.append(i[0])

    print(f"Inventory items: ")
    num = 0
    for i in items:
        num += 1
        print(f"{num}: {i}")

    while True:
        use_item = int(input("Which item would you like to use? "
                             "(Enter the number corresponding to the item or press 0 to exit): "))
        if use_item == 0:
            break
        elif not use_item < 0 or not use_item > num:
            for i in user_inventory:
                if i[0] == items[use_item - 1]:
                    print(items[use_item - 1])
                    if i[0] == "gun" or i[0] == "knife" or i[0] == "baseball_bat" or i[0] == "sticks":
                        weapon_change(i)
                        user_inventory.pop(use_item - 1)
                        break
                    elif i[0] == "fruit":
                        update_status(added_hunger=i[1]["hunger"], added_thirst=i[1]["thirst"])
                        user_inventory.pop(use_item - 1)
                        break
                    elif i[0] == "bandage" or i[0] == "med_kit":
                        update_status(added_health=i[1]["health"])
                        user_inventory.pop(use_item - 1)
                        break
                    elif i[0] == "bottle of water":
                        update_status(added_thirst=i[1]["thirst"])
                        user_inventory.pop(use_item - 1)
                        break
                    elif i[0] == "lighter":
                        print("This item is used with sticks to create fire.")
                        break
                    elif i[0] == "cooked rabbit":
                        update_status(added_hunger=i[1]["hunger"])
                        user_inventory.pop(use_item - 1)
                        break
                    elif i[0] == "raw rabbit":
                        user_inventory.pop(use_item - 1)
                        rabbit_encounter(1)
                        break
                    else:
                        print("The item is a quest item and cannot be used.")
                        break
            print(user_inventory)
            print(f"Health: {user_health}")
            print(f"Hunger: {user_hunger}")
            print(f"Thirst: {user_thirst}")
            print(f"Attack: {user_attack}")
            print(f"Weapon: {user_weapon}")
            break
        else:
            print("\nYou entered an invalid input.\n")


# Fix
def chest_encounter_action():
    print("You encountered a chest!")
    while True:
        user_open = int(input("Open it? (Press \'1\' to open or \'2\' to ignore.): "))
        chest_item = rand.choice(list(chest_encounters.items()))
        if user_open == 1:
            print(f"You opened it and got a {chest_item[0]}.")

            if chest_item[0] == "gun" or chest_item[0] == "knife" or chest_item[0] == "baseball_bat":
                while True:
                    user_weapon_update = int(input("Use it? (Press \'1\' to use weapon"
                                                   " or \'2\' to add to inventory.): "))
                    if user_weapon_update == 1:
                        weapon_change(chest_item)
                        del chest_encounters[str(chest_item[0])]
                        break
                    elif user_weapon_update == 2:
                        user_inventory.append(chest_item)
                        print(f"{chest_item[0]} is added to your inventory.")
                        del chest_encounters[str(chest_item[0])]
                        break
                    else:
                        print("\nYou entered an invalid input.\n")
                    print(chest_item)
                    print(user_inventory)
                    print(chest_encounters)
                    print(user_weapon)
                break
            else:
                while True:
                    user_status_update = str(input(f"Use it? (Press \'1\' to use {chest_item[0]}" 
                                                   f" or \'2\' to add to inventory.): "))
                    if user_status_update == '1':
                        if chest_item[0] == "fruit":
                            update_status(added_hunger=chest_item[1]["hunger"], added_thirst=chest_item[1]["thirst"])
                        else:
                            update_status(added_health=chest_item[1]["health"])
                        break
                    elif user_status_update == '2':
                        print(f"{chest_item[0]} is added to your inventory.")
                        user_inventory.append(chest_item)
                        break
                    else:
                        print("\nYou entered an invalid input.\n")
                break
        elif user_open == 2:
            break
        else:
            print("\nYou entered an invalid key.\n")


# Fix added sticks, lighter and bottle of water inside user_inventory
# Fix rabbit
# Fix showing inventory items
# Add emojis and illustrations
def encounters_translator():
    user_encounter = rand.choices(encounters, weights=(50, 45, 45, 40, 40, 35, 90, 25, 25))
    if user_encounter[0] == 'none':
        print(user_encounter[0])
        return False
    elif user_encounter[0] == 'sticks':
        print(f"You found {user_encounter[0]} and is added to your inventory.")
        user_inventory.append(("sticks", {"health": 0, "attack": 5}))
        return False
    elif user_encounter[0] == 'lighter':
        print(f"You found {user_encounter[0]} and is added to your inventory.")
        user_inventory.append(("lighter", {"health": 0, "attack": 0}))
        encounters[2] = "none"
        return False
    elif user_encounter[0] == 'bottle of water':
        print(f"You found a {user_encounter[0]}.")
        while True:
            use_item = str(input("Use it? (Press \'1\' to use or \'2\' to add to inventory): "))
            if use_item == '1':
                update_status(added_thirst=50)
                break
            elif use_item == '2':
                user_inventory.append(("bottle of water", {"hunger": 0, "thirst": 50}))
                break
            else:
                print("You entered an invalid key.")
        return False
    elif user_encounter[0] == 'rabbit':
        print(f"You found a {user_encounter[0]}.")
        while True:
            rabbit_kill = str(input("Kill it? (Press \'1\' to kill or \'2\' to ignore): "))
            if rabbit_kill == '1':
                print(f"You killed the {user_encounter[0]}.")
                rabbit_encounter(0)
                break
            elif rabbit_kill == '2':
                break
            else:
                print("You entered an invalid key.")
        if user_health <= 0:
            return True
        else:
            return False
    elif user_encounter[0] == 'chest':
        chest_encounter_action()
        return False
    elif user_encounter[0] == 'enemy':
        # print(rand.choice(list(enemy_encounters.keys())))  # Grabs a string
        # print(rand.choice(list(enemy_encounters.items())))  # Grabs the whole dictionary and turn into a tuple
        battle_encounter(rand.choice(list(enemy_encounters.items())))
        if user_health <= 0:
            return True
        else:
            return False
    elif user_encounter[0] == 'exit':
        while True:
            user_exit = str(input("You found the exit. Press \'1\' to exit or \'2\' to stay: "))
            if user_exit == '1':
                return True
            elif user_exit == '2':
                return False
            else:
                print("\nYou entered an invalid key.\n")
    else:
        print(f"You found {user_encounter[0]} and is added to your inventory.")
        user_inventory.append((str(user_encounter[0]), {"Quest item"}))
        del encounters[-1]
        return False


def user_action_translator():
    result = False
    user_action = str(input("Use \'W\' to move forward, \'A\' to move left, "
                            "\'S\' to move back, \'D\' to move right and "
                            "\'I\' to open your inventory: ").lower())
    if user_action == 'i':
        print("Opening inventory")
        inventory_use()
        if user_health <= 0:
            result = True
        else:
            result = False
    elif user_action == 'w':
        print("You moved forward")
        result = encounters_translator()
    elif user_action == 'a':
        print("You moved left")
        result = encounters_translator()
    elif user_action == 's':
        print("You moved back")
        result = encounters_translator()
    elif user_action == 'd':
        print("You moved right")
        result = encounters_translator()
    else:
        print("\nYou entered an invalid key.\n")

    return result


def status_check():
    update_status(decreased_thirst=2, decreased_hunger=2)
    if user_thirst <= 0:
        print("You are very thirsty.")
        update_status(decreased_health=2)
    if user_hunger <= 0:
        print("You are very hungry.")
        update_status(decreased_health=2)
    if user_health <= 0:
        is_exiting = True
    if 10 >= user_health > 0:
        print("You are fatally injured.")


# bool is_exiting
# User actions: move, open inventory
# Forest need to find box of food supply
# Fix to only able to get quest item once
def forest(difficulty):
    print("You entered the forest.")
    is_exiting = False

    if not any("food supply" in keys for keys in user_inventory):
        encounters.append("food supply")

    if difficulty == 1:
        enemy_encounters.update({
            "Large spider": {"Health": 10, "Attack": 2},
        })
    elif difficulty == 2:
        enemy_encounters.update({
            "Large spider": {"Health": 12, "Attack": 3},
        })
    else:
        enemy_encounters.update({
            "Large spider": {"Health": 15, "Attack": 4},
        })

    while not is_exiting:
        # print(user_inventory)
        print("+", "-" * 80, "+")
        print(name, "|", "Health:", user_health, "|", "Attack:", user_attack, "|")
        print("|", "Hunger:", user_hunger, "|", "Thirst:", user_thirst, "|")
        print("+", "-" * 80, "+")
        is_exiting = user_action_translator()
        status_check()

    del enemy_encounters["Large spider"]
    if not any("food supply" in keys for keys in user_inventory):
        del encounters[-1]


# Find flare gun
def cave(difficulty):
    print("You entered the cave.")
    is_exiting = False

    if not any("food supply" in keys for keys in user_inventory):
        encounters.append("flare gun")

    if difficulty == 1:
        enemy_encounters.update({
            "Blood thirst bats": {"Health": 6, "Attack": 2},
        })
    elif difficulty == 2:
        enemy_encounters.update({
            "Blood thirst bats": {"Health": 8, "Attack": 3},
        })
    else:
        enemy_encounters.update({
            "Blood thirst bats": {"Health": 10, "Attack": 4},
        })

    while not is_exiting:
        # print(user_inventory)
        print("+", "-" * 80, "+")
        print(name, "|", "Health:", user_health, "|", "Attack:", user_attack, "|")
        print("|", "Hunger:", user_hunger, "|", "Thirst:", user_thirst, "|")
        print("+", "-" * 80, "+")
        is_exiting = user_action_translator()
        status_check()

    del enemy_encounters["Blood thirst bats"]
    if not any("flare gun" in keys for keys in user_inventory):
        del encounters[-1]


# Find boat
# Fix end game different scenarios
# Fix to return different scenarios and transfer it to a function
# Fix if able to not return any value to continue game
# Add crab monsters
def beach(difficulty):
    print("You entered the beach.")
    is_exiting = False

    if not any("boat" in keys for keys in user_inventory):
        encounters.append("boat")

    while not is_exiting:
        print("+", "-" * 80, "+")
        print(name, "|", "Health:", user_health, "|", "Attack:", user_attack, "|")
        print("|", "Hunger:", user_hunger, "|", "Thirst:", user_thirst, "|")
        print("+", "-" * 80, "+")
        is_exiting = user_action_translator()
        status_check()

        if any("boat" in keys for keys in user_inventory):
            while True:
                user_sail = str(input("You have found a boat. Sail the ocean?" 
                                      "(Press \'1\' to sail or \'2\' to not sail): "))
                if user_sail == '1':
                    if (any("food supply" in keys for keys in user_inventory)
                            and any("flare gun" in keys for keys in user_inventory)):
                        return 1
                    elif (any("food supply" in keys for keys in user_inventory)
                            and not any("flare gun" in keys for keys in user_inventory)):
                        return 2
                    elif (not any("food supply" in keys for keys in user_inventory)
                            and any("flare gun" in keys for keys in user_inventory)):
                        return 3
                    else:
                        return 4
                elif user_sail == '2':
                    break
                else:
                    print("You entered an invalid key.")

        if is_exiting and not any("boat" in keys for keys in user_inventory):
            del encounters[-1]
            return 0
        else:
            return 0


def game_end(result):
    if result == 1:
        print("You sailed into the ocean with a flare gun"
              " and a month worth of food supply")
        time.sleep(2)
        print("After almost 2 months of suffering, you hear a noise.")
        print("It was the noise of a helicopter from far away.")
        print("So you screamed on top of your lungs for help.")
        print("But then you remembered...")
        time.sleep(2)
        print("You have a flare gun.")
        time.sleep(2)
        print("So you used it to fire to the sky.")
        print("The helicopter started going to the direction of the flare"
              " and has located you.")
        print(f"Congratulations {name}! You have beaten the game.")
    elif result == 2:
        print("You sailed into the ocean with"
              " a month worth of food supply")
        time.sleep(2)
        print("After almost 2 months of suffering, you hear a noise.")
        print("It was the noise of a helicopter from far away.")
        print("So you screamed on top of your lungs for help.")
        print("But they were not able to see or hear you.")
        print("So the helicopter passed by without finding you.")
        time.sleep(2)
        print("After another month, you have died from cold and hunger.")
        print("Game over")
    elif result == 3:
        print("You sailed into the ocean with"
              " a flare gun")
        time.sleep(2)
        print("After almost 2 months of suffering.")
        print("you have died from cold and hunger.")
        print("Game over")
    else:
        print("You sailed into the ocean")
        print("After almost 2 months of suffering.")
        print("you have died from cold and hunger.")
        print("Game over")


# TODO: 2 create progress of the game

def game_start():
    """Start of the game"""
    game_difficulty = choose_difficulty()
    game_over = False
    user_route = 0
    global name
    name += str(input("Please enter your character's name: "))

    print("As you walk around the island, \nyou encountered a group of villagers wearing a tribal mask,",
          "\nas you were about to approach them to ask for help.")
    time.sleep(2)
    print("You realize they were eating human flesh...")
    time.sleep(3)
    print("So you ran as fast as you can away from them.")
    print("As you look around the island, you see a forest and a cave.")

    while not game_over:
        print("+", "-" * 80, "+")
        print(name, "|", "Health:", user_health, "|", "Attack:", user_attack, "|")
        print("|", "Hunger:", user_hunger, "|", "Thirst:", user_thirst, "|")
        print("+", "-" * 80, "+")
        user_route = user_route_update(user_route)
        if user_route == 1:
            forest(game_difficulty)
        elif user_route == 2:
            cave(game_difficulty)
        else:
            game_result = beach(game_difficulty)
            if game_result == 0:
                pass
            else:
                game_end(game_result)
                game_over = True

        if user_health <= 0:
            print("You have died.")
            print("Game Over.")
            game_over = True


introduction()
