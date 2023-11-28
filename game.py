# Import the random module to generate random numbers
import random

# Define a class for the player
class Player:
    def __init__(self, name):
        self.name = name # The player's name
        self.health = 100 # The player's health
        self.inventory = [] # The player's inventory

    def add_item(self, item):
        # Add an item to the inventory
        self.inventory.append(item)

    def remove_item(self, item):
        # Remove an item from the inventory
        self.inventory.remove(item)

    def has_item(self, item):
        # Check if the inventory has an item
        return item in self.inventory

    def is_alive(self):
        # Check if the player is alive
        return self.health > 0

# Define a class for the game
class Game:
    def __init__(self):
        self.player = None # The player object
        self.story = None # The story object
        self.running = False # The game state

    def start(self):
        # Start the game
        self.running = True # Set the game state to running
        self.create_player() # Create the player object
        self.create_story() # Create the story object
        self.story.intro() # Show the intro of the story

    def create_player(self):
        # Create the player object
        name = input("Enter your name: ") # Ask the user for their name
        self.player = Player(name) # Create a new player object with the given name
        print(f"Welcome, {self.player.name}!") # Greet the player

    def create_story(self):
        # Create the story object
        self.story = Story(self.player) # Create a new story object with the player object

    def end(self):
        # End the game
        self.running = False # Set the game state to not running
        print("Game over.") # Print a message

# Define a class for the story
class Story:
    def __init__(self, player):
        self.player = player # The player object
        self.scenes = {} # A dictionary of scenes
        self.current_scene = None # The current scene
        self.create_scenes() # Create the scenes

    def create_scenes(self):
        # Create the scenes
        # Each scene is a tuple of (description, choices, outcomes)
        # Description is a string that describes the scene
        # Choices is a list of strings that represent the possible choices
        # Outcomes is a list of functions that handle the outcomes of the choices
        self.scenes["intro"] = (
            "You wake up in a dark and damp dungeon. You don't remember how you got here or why. You only have a torch and a dagger with you. You see a wooden door in front of you and a metal grate on the floor.",
            ["Open the door", "Lift the grate"],
            [self.open_door, self.lift_grate]
        )
        self.scenes["door"] = (
            "You open the door and enter a dimly lit corridor. You hear footsteps and voices coming from the other end. You quickly hide behind a barrel and peek out. You see two guards patrolling the area. They seem to be looking for something or someone.",
            ["Attack the guards", "Sneak past the guards"],
            [self.attack_guards, self.sneak_past_guards]
        )
        self.scenes["grate"] = (
            "You lift the grate and climb down a ladder. You find yourself in a sewer. The smell is unbearable and the water is filthy. You see a rat scurrying away from you. You also notice a small tunnel on the wall.",
            ["Follow the rat", "Enter the tunnel"],
            [self.follow_rat, self.enter_tunnel]
        )
        self.scenes["guards"] = (
            "You decide to attack the guards. You grab your dagger and charge at them. They are caught off guard and you manage to stab one of them in the chest. The other one swings his sword at you and you barely dodge it. You fight back and forth until you finally kill him too. You search their bodies and find a key and a map.",
            ["Take the key and the map", "Leave them alone"],
            [self.take_key_and_map, self.leave_them_alone]
        )
        self.scenes["sneak"] = (
            "You decide to sneak past the guards. You wait for the right moment and then run across the corridor. You are almost there when you step on a loose tile and make a loud noise. The guards hear you and turn around. They see you and shout. They draw their swords and run after you.",
            ["Fight the guards", "Run away"],
            [self.fight_guards, self.run_away]
        )
        self.scenes["rat"] = (
            "You decide to follow the rat. You think it might lead you to an exit. You chase the rat through the sewer until you reach a dead end. The rat disappears into a hole in the wall. You try to follow it but the hole is too small for you. You hear a hissing sound behind you. You turn around and see a giant snake blocking your way.",
            ["Fight the snake", "Beg for mercy"],
            [self.fight_snake, self.beg_for_mercy]
        )
        self.scenes["tunnel"] = (
            "You decide to enter the tunnel. You hope it will lead you to freedom. You crawl through the narrow passage until you see a faint light at the end. You reach the exit and find yourself in a forest. You breathe a sigh of relief. You have escaped the dungeon.",
            ["Celebrate", "Keep going"],
            [self.celebrate, self.keep_going]
        )
        self.scenes["key"] = (
            "You decide to take the key and the map. You think they might be useful. You look at the map and see that it shows the layout of the dungeon. You also see a red X marked on a room. You wonder what it means. You look at the key and see that it has a number on it. It matches the number of the room with the red X.",
            ["Go to the room", "Ignore the room"],
            [self.go_to_room, self.ignore_room]
        )
        self.scenes["room"] = (
            "You decide to go to the room. You follow the map and find the door with the matching number. You use the key and open it. You enter the room and see a large chest in the center. You approach it and lift the lid. You see a pile of gold and jewels. You have found the treasure.",
            ["Take the treasure", "Leave the treasure"],
            [self.take_treasure, self.leave_treasure]
        )
        self.scenes["treasure"] = (
            "You decide to take the treasure. You think you deserve it after all you have been through. You fill your pockets and bags with as much as you can carry. You feel rich and happy. You leave the room and head for the exit. You have completed the adventure.",
            ["The end", "Play again"],
            [self.the_end, self.play_again]
        )

    def intro(self):
        # Show the intro of the story
        print("Welcome to the text-based adventure game!")
        print("In this game, you will explore a dungeon and try to escape.")
        print("You will be presented with different choices at each scene.")
        print("Your choices will affect the outcome of the game.")
        print("Good luck and have fun!")
        print()
        self.change_scene("intro") # Change the scene to the intro

    def change_scene(self, scene):
        # Change the scene
        self.current_scene = scene # Set the current scene to the given scene
        self.show_scene() # Show the scene

    def show_scene(self):
        # Show the scene
        scene = self.scenes[self.current_scene] # Get the scene from the dictionary
        description = scene[0] # Get the description
        choices = scene[1] # Get the choices
        print(description) # Print the description
        print()
        self.show_choices(choices) # Show the choices

    def show_choices(self, choices):
        # Show the choices
        for i, choice in enumerate(choices): # Loop through the choices
            print(f"{i+1}. {choice}") # Print the choice number and text
        print()
        self.get_choice(choices) # Get the choice from the user

    def get_choice(self, choices):
        # Get the choice from the user
        valid = False # A flag to indicate if the choice is valid
        while not valid: # Loop until the choice is valid
            try: # Try to get the choice
                choice = int(input("Enter your choice: ")) # Get the choice as an integer
                if 1 <= choice <= len(choices): # Check if the choice is within the range
                    valid = True # Set the flag to true
                else: # If the choice is out of range
                    print("Invalid choice. Try again.") # Print an error message
            except: # If the choice is not an integer
                print("Invalid choice. Try again.") # Print an error message
        print()
        self.handle_choice(choice, choices) # Handle the choice

    def handle_choice(self, choice, choices):
        # Handle the choice
        scene = self.scenes[self.current_scene] # Get the scene from the dictionary
        outcomes = scene[2] # Get the outcomes
        outcome = outcomes[choice-1] # Get the outcome based on the choice
        outcome() # Call the outcome function

    # Define the outcome functions for each choice
    def open_door(self):
        # The outcome of opening the door
        print("You open the door and enter the corridor.")
        self.change_scene("door") # Change the scene to the door

    def lift_grate(self):
        # The outcome of lifting the grate
        print("You lift the grate and climb down the ladder.")
        self.change_scene("grate") # Change the scene to the grate

    def attack_guards(self):
        # The outcome of attacking the guards
        print("You attack the guards and kill them.")
        self.change_scene("guards") # Change the scene to the guards

    def sneak_past_guards(self):
        # The outcome of sneaking past the guards
        print("You sneak past the guards and reach the other end of the corridor.")
        self.change_scene("sneak") # Change the scene to the sneak

    def follow_rat(self):
        # The outcome of following the rat
        print("You follow the rat and reach a dead end.")
        self.change_scene("rat") # Change the scene to the rat

    def enter_tunnel(self):
        # The outcome of entering the tunnel
        print("You enter the tunnel and reach the forest.")
        self.change_scene("tunnel") # Change the scene to the tunnel

    def take_key_and_map(self):
        # The outcome of taking the key and the map
        print("You take the key and the map.")
        self.change_scene("key") # Change the scene to the key

    def leave_them_alone(self):
        # The outcome of leaving them alone
        print("You leave them alone and continue your way.")
        self.change_scene("leave") # Change the scene to the leave

    def go_to_room(self):
        # The outcome of going to the room
        print("You go to the room and find the treasure.")
        self.change_scene("room") # Change the scene to the room

    def ignore_room(self):
        # The outcome of ignoring the room
        print("You ignore the room and look for another way out.")
        self.change_scene("ignore") # Change the scene to the ignore

    def take_treasure(self):
        # The outcome of taking the treasure
        print("You take the treasure and escape the dungeon.")
        self.change_scene("treasure") # Change the scene to the treasure

    def leave_treasure(self):
        # The outcome of leaving the treasure
        print("You leave the treasure and escape the dungeon.")
        self.change_scene("leave") # Change the scene to the leave

    def fight_guards(self):
        # The outcome of fighting the guards
        print("You fight the guards and try to escape.")
        chance = random.randint(1, 10) # Generate a random number between 1 and 10
        if chance <= 3: # 30% chance of success
            print("You manage to defeat the guards and run away.")
            self.change_scene("run") # Change the scene to the run
        else: # 70% chance of failure
            print("You are overpowered by the guards and captured.")
            self.change_scene("capture") # Change the scene to the capture

    def run_away(self):
        # The outcome of running away
        print("You run away and try to escape.")
        chance = random.randint(1, 10) # Generate a random number between 1 and 10
        if chance <= 5: # 50% chance of success
            print("You manage to outrun the guards and find an exit.")
            self.change_scene("exit") # Change the scene to the exit
        else: # 50% chance of failure
            print("You are caught by the guards and captured.")
            self.change_scene("capture") # Change the scene to the capture

    def fight_snake(self):
        # The outcome of fighting the snake
        print("You fight the snake and try to survive.")
        chance = random.randint(1, 10) # Generate a random number between 1 and 10
        if chance <= 2: # 20% chance of success
            print("You manage to kill the snake and find a way out.")
            self.change_scene("out") # Change the scene to the out
        else: # 80% chance of failure
            print("You are bitten by the snake and die.")
            self.change_scene("die") # Change the scene to the die

    def beg_for_mercy(self):
        # The outcome of begging for mercy
        print("You beg for mercy and hope for a miracle.")
        chance = random.randint(1, 10) # Generate a random number between 1 and 10
        if chance == 1: # 10% chance of success
            print("The snake spares your life and lets you go.")
            self.change_scene("go") # Change the scene to the go
        else: # 90% chance of failure
            print("The snake ignores your pleas and eats you.")
            self.change_scene("eat") # Change the scene to the eat

    def celebrate(self):
        # The outcome of celebrating
        print("You celebrate your escape and enjoy the fresh air.")
        self.change_scene("celebrate") # Change the scene to the celebrate

    def keep_going(self):
        # The outcome of keeping going
        print("You keep going and look for civilization.")
        self.change_scene("civilization") # Change the scene to the civilization

    def the_end(self):
        # The outcome of the end
        print("The end. Thank you for playing!")
        game.end() # End the game

    def play_again(self):
        # The outcome of playing again
        print("Do you want to play again?")
        choice = input("Enter yes or no: ") # Get the choice from the user
        if choice.lower() == "yes": # If the choice is yes
            print("Starting a new game...")
            game.start() # Start a new game
        elif choice.lower() == "no": # If the choice is no
            print("Goodbye!")
            game.end() # End the game
        else: # If the choice is invalid
            print("Invalid choice. Try again.")
            self.play_again() # Ask again

    # Define the scenes for the endings
    def create_scenes(self):
        self.scenes["intro"] = (
            "You wake up in a dark and damp dungeon. You don't remember how you got here or why. You only have a torch and a dagger with you. You see a wooden door in front of you and a metal grate on the floor.",
            ["Open the door", "Lift the grate"],
            [self.open_door, self.lift_grate]
        )
        self.scenes["door"] = (
            "You open the door and enter a dimly lit corridor. You hear footsteps and voices coming from the other end. You quickly hide behind a barrel and peek out. You see two guards patrolling the area. They seem to be looking for something or someone.",
            ["Attack the guards", "Sneak past the guards"],
            [self.attack_guards, self.sneak_past_guards]
        )
        self.scenes["grate"] = (
            "You lift the grate and climb down a ladder. You find yourself in a sewer. The smell is unbearable and the water is filthy. You see a rat scurrying away from you. You also notice a small tunnel on the wall.",
            ["Follow the rat", "Enter the tunnel"],
            [self.follow_rat, self.enter_tunnel]
        )
        self.scenes["guards"] = (
            "You decide to attack the guards. You grab your dagger and charge at them. They are caught off guard and you manage to stab one of them in the chest. The other one swings his sword at you and you barely dodge it. You fight back and forth until you finally kill him too. You search their bodies and find a key and a map.",
            ["Take the key and the map", "Leave them alone"],
            [self.take_key_and_map, self.leave_them_alone]
        )
        self.scenes["key"] = (
            "You decide to take the key and the map. You think they might be useful. You look at the map and see that it shows the layout of the dungeon. You also see a red X marked on a room. You wonder what it means. You look at the key and see that it has a number on it. It matches the number of the room with the red X.",
            ["Go to the room", "Ignore the room"],
            [self.go_to_room, self.ignore_room]
        )
        self.scenes["capture"] = (
            "You have been captured by the guards. They take you to a dark cell and lock you up. You have failed to escape the dungeon.",
            ["The end", "Play again"],
            [self.the_end, self.play_again]
        )
        self.scenes["die"] = (
            "You have died from the snake bite. Your body lies on the sewer floor. You have failed to escape the dungeon.",
            ["The end", "Play again"],
            [self.the_end, self.play_again]
        )
        self.scenes["eat"] = (
            "You have been eaten by the snake. Your bones are left in the sewer. You have failed to escape the dungeon.",
            ["The end", "Play again"],
            [self.the_end, self.play_again]
        )
        self.scenes["run"] = (
            "You have escaped the guards and run away. You find a hidden passage that leads you to the outside. You have escaped the dungeon.",
            ["Celebrate", "Keep going"],
            [self.celebrate, self.keep_going]
        )
        self.scenes["exit"] = (
            "You have outrun the guards and found an exit. You open the door and see the sunlight. You have escaped the dungeon.",
            ["Celebrate", "Keep going"],
            [self.celebrate, self.keep_going]
        )
        self.scenes["out"] = (
            "You have killed the snake and found a way out. You climb a ladder and reach the surface. You have escaped the dungeon.",
            ["Celebrate", "Keep going"],
            [self.celebrate, self.keep_going]
        )
        self.scenes["go"] = (
            "You have been spared by the snake and let go. You find a small boat and paddle your way out. You have escaped the dungeon.",
            ["Celebrate", "Keep going"],
            [self.celebrate, self.keep_going]
        )
        self.scenes["celebrate"] = (
            "You have escaped the dungeon and celebrated your freedom. You feel proud and happy. You have completed the adventure.",
            ["The end", "Play again"],
            [self.the_end, self.play_again]
        )
        self.scenes["civilization"] = (
            "You have escaped the dungeon and found civilization. You meet some friendly people who help you. You have completed the adventure.",
            ["The end", "Play again"],
            [self.the_end, self.play_again]
        )

# Create a game object
game = Game()

# Start the game
game.start()
