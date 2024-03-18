inventory = []

def start_game():
    print("Welcome to the Sci-Fi Adventure Game!")
    print("You find yourself on a distant planet, standing at a crossroad.")
    print("You can go left, right, or straight ahead.")

    choice = input("Which direction do you want to go? (left/right/straight): ").lower()

    if choice == "left":
        go_left()
    elif choice == "right":
        go_right()
    elif choice == "straight":
        go_straight()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def go_left():
    print("You chose to go left.")
    print("You come across a mysterious alien artifact.")
    print("Do you want to touch it, smash it, or take it?")

    choice = input("Enter 'touch' to touch the artifact, 'smash' to destroy it, or 'take' to store it in your inventory: ").lower()

    if choice == "touch":
        investigate_artifact()
    elif choice == "smash":
        print("You decided to smash the artifact.")
        print("It suddenly explodes, killing you instantly.")
        print("Game Over. You lost!")
    elif choice == "take":
        inventory.append("Alien Artifact")
        print("You've added 'Alien Artifact' to your inventory.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        go_left()

def go_right():
    print("You chose to go right.")
    print("You find an abandoned spaceship.")
    print("Do you want to search the ship or leave it?")

    choice = input("Enter 'search' to explore the ship or 'leave' to continue: ").lower()

    if choice == "search":
        search_ship()
    elif choice == "leave":
        print("You decide to leave the ship untouched.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        go_right()

def go_straight():
    print("You chose to go straight ahead.")
    print("You walk for a while and reach a futuristic city.")
    print("Do you want to explore the city or leave?")

    choice = input("Enter 'explore' to explore the city or 'leave' to continue on your journey: ").lower()

    if choice == "explore":
        explore_city()
    elif choice == "leave":
        print("You decide to continue your journey.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        go_straight()

def investigate_artifact():
    print("You cautiously touch the alien artifact and activate a teleportation device!")
    print("Congratulations! You are teleported to safety.")

def search_ship():
    print("You search the abandoned spaceship and find advanced technology.")
    inventory.append("Advanced Technology")
    print("You've added 'Advanced Technology' to your inventory.")
    start_game()

def explore_city():
    print("You explore the futuristic city and meet friendly cyborgs.")
    print("You spend some time gathering information and resources before continuing your adventure.")
    start_game()

def check_inventory():
    if inventory:
        print("Inventory:")
        for item in inventory:
            print("-", item)
    else:
        print("Inventory is empty.")

def main():
    while True:
        action = input("What would you like to do? Type 'inventory' to check your inventory or 'start' to begin the game: ").lower()
        if action == "inventory":
            check_inventory()
        elif action == "start":
            start_game()
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
