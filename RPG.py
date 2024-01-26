import time

def introduction():
    # Display the game introductions
    print("Welcome to the Text-Based RPG Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("Your goal is to navigate through the challenges and reach the treasure at the end.")
    time.sleep(1)
    print("Let the adventure begin!\n")

def make_choice(options):
    # Function to present choices to the player and get their input
    print("Choose your action:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = input("Enter the number of your choice: ")
    return int(choice) - 1

def forest_path():
    # Scenario for the forest path
    print("You start walking through the forest.")
    time.sleep(1)
    print("Suddenly, you encounter a fork in the path.")
    time.sleep(1)

    options = ["Take the left path.", "Take the right path."]
    choice = make_choice(options)

    if choice == 0:
        print("You chose to take the left path.")
        time.sleep(1)
        print("You find a hidden bridge and safely cross the river.")
        return True
    else:
        print("You chose to take the right path.")
        time.sleep(1)
        print("You encounter a group of wild animals. They chase you away.")
        return False

def dark_cave():
    # Scenario for the dark cave
    print("You enter a dark cave.")
    time.sleep(1)
    print("Inside, you see two tunnels.")
    time.sleep(1)

    options = ["Go through the left tunnel.", "Go through the right tunnel."]
    choice = make_choice(options)

    if choice == 0:
        print("You chose to go through the left tunnel.")
        time.sleep(1)
        print("You find a shortcut and reach the other side of the cave.")
        return True
    else:
        print("You chose to go through the right tunnel.")
        time.sleep(1)
        print("You encounter a giant spider. It blocks your way.")
        return False

def treasure_chamber():
    # Final scenario for reaching the treasure chamber
    print("Congratulations! You reached the treasure chamber.")
    time.sleep(1)
    print("You found the hidden treasure.")
    time.sleep(1)
    print("You are victorious!")

def main():
    # Main game function
    introduction()

    if forest_path():
        if dark_cave():
            treasure_chamber()
        else:
            print("Unfortunately, you couldn't make it through the dark cave. Game over.")
    else:
        print("Unfortunately, you couldn't navigate through the forest. Game over.")

if __name__ == "__main__":
    main()
