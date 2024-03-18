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
        check_inventory()
        search_ship()
    else:
        print("Invalid choice. Please try again.")
        search_ship()

def explore_ship():
    print("You enter the spaceship.")
    print("The spaceship is missing essential parts to fly.")
    print("Do you want to try and start the ship or leave it?")

    choice = input("Enter 'start' to try and start the ship or 'leave' to continue: ").lower()

    if choice == "start":
        print("You attempt to start the ship without the missing parts.")
        print("The ship's systems overload and it explodes.")
        print("Game Over. You lost!")
    elif choice == "leave":
        print("You decide to leave the spaceship alone.")
        start_game()
    elif choice == "inventory":
        check_inventory()
        explore_ship()
    else:
        print("Invalid choice. Please try again.")
        explore_ship()

def explore_city():
    print("You explore the futuristic city and meet friendly cyborgs.")
    if "Ray Gun" in inventory:
        print("You have a ray gun.")
        print("You can choose to threaten the cyborgs with the ray gun.")
        choice = input("Enter 'threaten' to threaten the cyborgs or 'explore' to continue exploring: ").lower()
        if choice == "threaten":
            print("You threaten the cyborgs with your ray gun.")
            print("The cyborgs overpower you and lock you up in a futuristic jail cell.")
            print("Game Over. You lost!")
            return
    if "Alien Artifact" in inventory:
        print("The cyborgs are interested in your Alien Artifact.")
        print("They offer you ship parts in exchange for the artifact.")
        choice = input("Do you want to trade the Alien Artifact for ship parts? (yes/no): ").lower()
        if choice == "yes":
            print("You trade the Alien Artifact for ship parts.")
            inventory.remove("Alien Artifact")
            inventory.append("Ship Parts")
            print("You've added 'Ship Parts' to your inventory.")
            stay_or_leave_city()
        elif choice == "no":
            print("You decide not to trade the Alien Artifact.")
            stay_or_leave_city()
        else:
            print("Invalid choice. Please try again.")
            explore_city()
    else:
        stay_or_leave_city()

def stay_or_leave_city():
    print("You can choose to stay and live in the city, or continue your journey.")
    choice = input("Enter 'stay' to stay in the city or 'leave' to continue on your journey:
