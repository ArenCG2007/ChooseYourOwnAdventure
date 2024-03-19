inventory = []

def start_game():
    print("Welcome to SpaceQuest - The Sci-Fi Adventure Game!")
    print("You find yourself on a distant planet, standing at a crossroad, you have been tasked with finding and killing a beastly monster on this planet.")
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
        print("You decided to venture left, curious about what lies ahead.")
        print("After walking for a while, you stumble upon a mysterious glowing artifact resting on the ground.")
        take_artifact()
    elif direction == "right":
        print("You chose to go right, drawn by the allure of the unknown.")
        print("As you proceed, the path leads you to a dark cave entrance.")
        explore_cave()
    elif direction == "straight":
        print("You opt to move straight ahead, driven by an instinct to explore.")
        print("After a brisk walk, you find yourself in a futuristic city, bustling with activity.")
        explore_city()

def take_artifact():
    action = input("Do you want to take the artifact, or kick it away in frustration? (take/kick): ").lower()
    if action == "take":
        inventory.append("Alien Artifact")
        print("You carefully pick up the strange artifact, intrigued by its otherworldly appearance.")
        print("You've added 'Alien Artifact' to your inventory.")
    elif action == "kick":
        print("You kick the alien artifact out of frustration, expecting it to be worthless junk.")
        print("To your horror, it explodes upon impact, engulfing you in a blinding flash of light.")
        print("Game Over. You lost!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        take_artifact()

def explore_cave():
    print("You summon your courage and venture into the ominous darkness of the cave.")
    print("As you delve deeper, a sense of foreboding washes over you.")
    print("Suddenly, you encounter a monstrous creature lurking in the shadows - a giant space spider!")
    action = input("Do you bravely face the spider in combat, or flee in terror? (fight/flee): ").lower()
    if action == "fight":
        fight_spider()
    elif action == "flee":
        print("Your survival instincts kick in, urging you to retreat from the menacing spider.")
        print("You manage to escape its clutches and make your way back to the crossroad.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        explore_cave()

def fight_spider():
    if "Ray Gun" in inventory:
        print("You boldly brandish your ray gun and unleash a barrage of energy blasts at the spider.")
        print("With each shot, the spider weakens until it collapses, defeated.")
        print("Congratulations! You've triumphed over the giant space spider and secured your path forward!")
        exit()
    else:
        print("You valiantly attempt to combat the spider with your bare hands, but it proves to be futile.")
        print("Overwhelmed by its ferocity, you succumb to its venomous bite.")
        print("Game Over. You lost!")
        exit()

def explore_city():
    print("Intrigued by the bustling activity of the futuristic city, you decide to explore further.")
    print("As you wander through the streets, you encounter friendly cyborgs.")
    action = input("Do you wish to engage with the cyborgs and learn more about this alien civilization? (yes/no): ").lower()
    if action == "yes":
        interact_with_cyborgs()

def interact_with_cyborgs():
    print("The cyborgs express interest in the strange artifact you carry.")
    action = input("Would you consider trading the Alien Artifact for a powerful weapon? (yes/no): ").lower()
    if action == "yes":
        if "Alien Artifact" in inventory:
            inventory.remove("Alien Artifact")
            inventory.append("Ray Gun")
            print("Impressed by your willingness to cooperate, the cyborgs exchange the artifact for a powerful ray gun.")
            print("You've acquired the 'Ray Gun' and added it to your inventory.")
        else:
            print("You don't possess the Alien Artifact to trade.")
    elif action == "no":
        print("Respecting your decision, the cyborgs bid you farewell and return to their activities.")
    else:
        print("The cyborgs seem perplexed by your indecisiveness but maintain a polite demeanor.")

def check_inventory():
    if inventory:
        print("Your Inventory:")
        for item in inventory:
            print("- " + item)
    else:
        print("Your inventory is empty.")

start_game()
