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
        print("You find an abandoned spaceship.")
        action = input("Do you want to search the ship? (yes/no): ").lower()
        if action == "yes":
            search_ship()
    elif direction == "straight":
        print("You chose to go straight ahead.")
        print("You walk for a while and reach a futuristic city.")
        action = input("Do you want to explore the city? (yes/no): ").lower()
        if action == "yes":
            explore_city()

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

def explore_city():
    print("You explore the futuristic city and meet friendly cyborgs.")
    action = input("Do you want to interact with the cyborgs? (yes/no): ").lower()
    if action == "yes":
        interact_with_cyborgs()

def interact_with_cyborgs():
    print("The cyborgs are interested in your Alien Artifact.")
    action = input("Do you want to trade the Alien Artifact for ship parts? (yes/no): ").lower()
    if action == "yes":
        inventory.remove("Alien Artifact")
        inventory.append("Ship Parts")
        print("You've added 'Ship Parts' to your inventory.")

def check_inventory():
    print("Inventory:", inventory)

start_game()
