inventory = []

def start_game():
    print("Welcome to SpaceQuest - The Sci-Fi Adventure Game!")
    print("You find yourself on a distant planet, standing at a crossroad.")
    print("You can go left, right, or straight ahead.")

    choice = input("Which direction do you want to go? (left/right/straight): ").lower()

    if choice == "left":
        go_left()
    elif choice == "right":
        go_right()
    elif choice == "straight":
        go_straight()
    elif choice == "inventory":
        check_inventory()
        start_game()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def go_left():
    print("You chose to go left.")
    print("You come across a mysterious alien artifact.")
    print("Do you want to touch it, shoot it, smash it, take it, or drop something from your inventory?")

    choice = input("Enter 'touch' to touch the artifact, 'shoot' to shoot it with the ray gun, 'smash' to destroy it, 'take' to store it in your inventory, 'drop' to remove an item from your inventory, or 'inventory' to check your inventory: ").lower()

    if choice == "touch":
        investigate_artifact()
    elif choice == "shoot":
        if "Ray Gun" in inventory:
            print("You shoot the alien artifact with your ray gun.")
            print("The artifact reacts violently and explodes.")
            print("Game Over. You lost!")
        else:
            print("You don't have a ray gun to shoot the artifact.")
            go_left()
    elif choice == "smash":
        print("You decided to smash the artifact.")
        print("It suddenly explodes, killing you instantly.")
        print("Game Over. You lost!")
    elif choice == "take":
        inventory.append("Alien Artifact")
        print("You've added 'Alien Artifact' to your inventory.")
        print("You see paths leading left and right.")
        choice = input("Which path will you take? (left/right): ").lower()
        if choice == "left":
            explore_city()
        elif choice == "right":
            giant_space_spider()
        else:
            print("Invalid choice. Please try again.")
            go_left()
    elif choice == "drop":
        drop_item()
        go_left()
    elif choice == "inventory":
        check_inventory()
        go_left()
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
    elif choice == "inventory":
        check_inventory()
        go_right()
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
    elif choice == "inventory":
        check_inventory()
        go_straight()
    else:
        print("Invalid choice. Please try again.")
        go_straight()

def investigate_artifact():
    print("You cautiously touch the alien artifact and activate a teleportation device!")
    print("Congratulations! You are teleported to safety.")

def search_ship():
    print("You found an abandoned spaceship.")
    print("The spaceship looks old and missing parts to fly.")
    print("Do you want to enter the spaceship or leave it?")

    choice = input("Enter 'enter' to explore the spaceship or 'leave' to continue: ").lower()

    if choice == "enter":
        explore_ship()
    elif choice == "leave":
        print("You decide to leave the spaceship untouched.")
        start_game()
    elif choice == "inventory":
        check_inventory
