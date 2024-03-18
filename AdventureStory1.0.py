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
        action = input("Do you want to take the artifact? (yes/no): ").lower()
        if action == "yes":
            inventory.append("Alien Artifact")
            print("You've added 'Alien Artifact' to your inventory.")
    elif direction == "right":
        print("You chose to go right.")
        print("You come across a dark cave entrance.")
        action = input("Do you want to enter the cave, search the ship, or pick up the ray gun? (cave/search/pick up/ray gun/inventory): ").lower()
        if action == "cave":
            explore_cave()
        elif action == "search":
            search_ship()
        elif action == "pick up":
            pick_up_ray_gun()
        elif action == "ray gun":
            check_inventory()
            explore("right")
    elif direction == "straight":
        print("You chose to go straight ahead.")
        print("You walk for a while and reach a futuristic city.")
        action = input("Do you want to explore the city, fix the ship, or enter the ship? (explore/fix ship/enter ship/inventory): ").lower()
        if action == "explore":
            explore_city()
        elif action == "fix ship":
            fix_ship()
        elif action == "enter ship":
            enter_ship()

def explore_cave():
    print("You enter the dark cave.")
    print("As you venture deeper into the cave, you encounter a giant space spider!")
    action = input("Do you want to fight the spider or flee? (fight/flee/inventory): ").lower()
    if action == "fight":
        fight_spider()
    elif action == "flee":
        print("You run away from the spider, narrowly escaping its grasp.")
        start_game()
    elif action == "inventory":
        check_inventory()
        explore_cave()
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

def search_ship():
    print("You found an abandoned spaceship.")
    print("The spaceship looks old and missing parts to fly.")
    action = input("Do you want to enter the spaceship? (yes/no): ").lower()
    if action == "yes":
        explore_ship()

def explore_ship():
    print("You enter the spaceship.")
    print("The spaceship is missing essential parts to fly.")
    action = input("Do you want to try and start the ship? (yes/no): ").lower()
    if action == "yes":
        print("You attempt to start the ship without the missing parts.")
        print("The ship's systems overload and it explodes.")
        print("Game Over. You lost!")

def enter_ship():
    print("You enter the spaceship.")
    print("The spaceship is missing essential parts to fly.")
    action = input("Do you want to try and start the ship or fix it? (start/fix/inventory): ").lower()
    if action == "start":
        print("You attempt to start the ship without the missing parts.")
        print("The ship's systems overload and it explodes.")
        print("Game Over. You lost!")
    elif action == "fix":
        fix_ship()
    elif action == "inventory":
        check_inventory()
        enter_ship()
    else:
        print("Invalid choice. Please try again.")
        enter_ship()

def fix_ship():
    print("You examine the spaceship and notice that it can be repaired.")
    action = input("Do you want to fix the ship? (yes/no): ").lower()
    if action == "yes":
        print("You repair the ship and successfully fly away.")
        print("Congratulations! You've escaped and won the game!")
        exit()
    elif action == "no":
        print("You decide not to fix the ship.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        fix_ship()

def pick_up_ray_gun():
    print("You find a ray gun lying on the ground.")
    action = input("Do you want to pick up the ray gun? (yes/no): ").lower()
    if action == "yes":
        inventory.append("Ray Gun")
        print("You've added 'Ray Gun' to your inventory.")
        start_game()
    elif action == "no":
        print("You decide not to pick up the ray gun.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        pick_up_ray_gun()

def explore_city():
    print("You explore the futuristic city and meet friendly cyborgs.")
    if "Alien Artifact" in inventory:
        action = input("Do you want to interact with the cyborgs? (yes/no): ").lower()
        if action == "yes":
            interact_with_cyborgs()
    else:
        print("You don't have the necessary item to interact with the cyborgs.")

def interact_with_cyborgs():
    print("The cyborgs are interested in your Alien Artifact.")
    action = input("Do you want to trade the Alien Artifact for ship parts or threaten them with the ray gun? (trade/threaten/inventory): ").lower()
    if action == "trade":
        inventory.remove("Alien Artifact")
        inventory.append("Ship Parts")
        print("You've added 'Ship Parts' to your inventory.")
    elif action == "threaten":
        if "Ray Gun" in inventory:
            print("You threaten the cyborgs with the ray gun.")
            print("The cyborgs, intimidated, offer you ship parts as a bribe.")
            inventory.append("Ship Parts")
            print("You've added 'Ship Parts' to your inventory.")
        else:
            print("You don't have the necessary item to threaten the cyborgs.")
    elif action == "inventory":
        check_inventory()
        interact_with_cyborgs()
    else:
        print("Invalid choice. Please try again.")
        interact_with_cyborgs()

def check_inventory():
    if inventory:
        print("Your Inventory:")
        for item in inventory:
            print("- " + item)
    else:
        print("Your inventory is empty.")

start_game()
