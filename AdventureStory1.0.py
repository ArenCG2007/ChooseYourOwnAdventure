inventory = []

def start_game():
    print("Welcome to SpaceQuest - The Sci-Fi Adventure Game!")
    print("You find yourself on a distant planet, standing at a crossroad.")
    print("You can go left, right, or straight ahead.")

    while True:
        choice = input("Which direction do you want to go? (left/right/straight/inventory): ").lower()

        if choice in ["left", "right", "straight"]:
            explore(choice)
        elif choice == "inventory":
            check_inventory()
        else:
            print("Invalid choice. Please try again.")

def explore(direction):
    if direction == "left":
        print("You chose to go left.")
        print("You come across a mysterious alien artifact.")
        take_artifact()
    elif direction == "right":
        print("You chose to go right.")
        print("You come across a dark cave entrance.")
        explore_cave()
    elif direction == "straight":
        print("You chose to go straight ahead.")
        print("You walk for a while and reach a futuristic city.")
        explore_city()

def take_artifact():
    action = input("Do you want to take the artifact? (yes/no): ").lower()
    if action == "yes":
        inventory.append("Alien Artifact")
        print("You've added 'Alien Artifact' to your inventory.")

def explore_cave():
    print("You enter the dark cave.")
    print("As you venture deeper, you encounter a giant space spider!")
    action = input("Do you want to fight the spider or flee? (fight/flee): ").lower()
    if action == "fight":
        fight_spider()
    elif action == "flee":
        print("You run away from the spider, narrowly escaping its grasp.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        explore_cave()

def fight_spider():
    if "Ray Gun" in inventory:
        print("You use your ray gun to blast the spider, defeating it.")
        print("Congratulations! You've defeated the giant space spider and won the game!")
        exit()
    else:
        print("You attempt to fight the spider bare-handed, but it overwhelms you.")
        print("Game Over. You lost!")

def explore_city():
    print("You explore the futuristic city and meet friendly cyborgs.")
    action = input("Do you want to interact with the cyborgs? (yes/no): ").lower()
    if action == "yes":
        interact_with_cyborgs()

def interact_with_cyborgs():
    print("The cyborgs are interested in your Alien Artifact.")
    action = input("Do you want to trade the Alien Artifact for ship parts or threaten them with the ray gun? (trade/threaten): ").lower()
    if action == "trade":
        if "Alien Artifact" in inventory:
            inventory.remove("Alien Artifact")
            inventory.append("Ship Parts")
            print("You've added 'Ship Parts' to your inventory.")
        else:
            print("You don't have the Alien Artifact to trade.")
    elif action == "threaten":
        if "Ray Gun" in inventory:
            print("You threaten the cyborgs with the ray gun.")
            print("The cyborgs, intimidated, offer you ship parts as a bribe.")
            inventory.append("Ship Parts")
        else:
            print("You don't have the ray gun to threaten the cyborgs.")

def check_inventory():
    if inventory:
        print("Your Inventory:")
        for item in inventory:
            print("- " + item)
    else:
        print("Your inventory is empty.")

start_game()
