from sys import exit
from random import randint
from textwrap import dedent

class scene(object):

    def enter(self):
        print("this scene is not yet configured.")
        print("subclass it and implement enter().")
        exit(1)

class engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class death(scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud....if she were smarter.",
        "Such a looser.",
        "I have a left over bowl of rice that's better at this.",
        "You are worse than your Dad's jokes."
    ]

    def enter(self):
        print(death.quips[randint(0, len(self.quips)-1)])
        return 'great_hall'

class GreatHall(scene):
    def enter(self):
        print(dedent("""
            ....................................................
            The Goblins of gvbufbux have attacked Hogwarts and
            killed everyone. You are the only survivor and 
            you have decided to get the egg of death from the
            Potions Lab, put it in the Gryffins Roost, and curse the 
            Castle after escaping through a portkey.

            You are running down the Great Hall to the Potions Lab
            when a Goblin jumps out, white paint covering his
            dark scaly skin, his grimy pointed teeth beard at you as
            he jumped up and down in his evil clown costume. He's
            blocking the door to the inner sanctum and about to pull
            out a wand to blast you.
            """))
        
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                .....................................................
                Quick on the draw you yank out your wand and blast at
                the Goblin. His clown costume is flowing and moving 
                around his body, which throws off your aim. Your spell
                hits his costume but misses him entirely. This completely
                ruins his brand new costume his mother bought him, which
                makes him fly into an insane rage and blast you repeatedly
                in the face until you are dead.  Then he eats you.
                """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                .........................................................
                Like a world class boxer you dodge, weave, slip and slide
                right as the Goblin's wand cranks a spell past your head.
                In the middle of your artful dodge, your foot slips and you
                bang your head on the stone wall and pass out. You wake 
                shortly after, only to die as the Goblin stomps on your head
                and eats you.
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                ................................................................
                Lucky for you, they made you learn Gobledegook insults in history
                of magic. You tell the one Goblin Joke you know: hgdij or vjf mo
                khg ggggki grbit ngrgbdzx. The Goblin stops, tries not to laugh,
                then bursts out laughing and can't move. While he's laughing you
                run up and blast him square in the head putting him down, then
                jump into the potions lab.
                """))
            return 'potions_lab'

        else:
            print("DOES NOT COMPUTE!")
            return 'great_hall' 

class PotionsLab(scene):

    def enter(self):
        print(dedent("""
            ..................................................................
             You do a dive roll into the potions lab, crouch and scan the room
             for more Goblins that might be hiding. It's dead quit, too quite.
             You stand up and run to the far side of the of the room and find
             the egg of death in its container. A wrinkled old face appears on
             the container and says "Hay you, the potion in this box is really
             dangerous and can't just let any lughead get it, so if it isn't
             too inconvenient for you, I'll recite a riddle and you have 5 
             guesses to get it right. If you do, you can have the potion and 
             wreak as much havoc as you see fit and if you don't, you die...
             good? Here goes."

             First think of something that lives in disguise, deals in secrests
             and tells nothing but lies.

             Next tell me what is the last thing to mend, the middle of middle
             and the end of end.

             Finally think of a sound often heard when thinking of a hard to
             find word.

             Put it all together and tell me this, what creature would you be 
             unwilling to kiss?   
             """))
        
        answer = "spider"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != answer and guesses < 5:
            print ("WRONG ANSWER")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == answer:
            print(dedent("""
                ............................................................
                The container clicks open and the seal breaks, letting misty 
                gas out. You grab the egg of death and run as fast as you can 
                to the Gryffins Roost where you must place it in the right 
                spot.
                """))
            return 'gryffins_roost'
        else:
            print(dedent("""
                ..............................................................
                The lock buzzes as an argent dark cloud rises from the box and
                slowly drains the life out of you.
                """))
            return 'death'

        
class GryffinsRoost(scene):

    def enter(self):
        print(dedent("""
             ..............................................................   
             You burst into the Gryffins Roost with the egg of death under
             your arm and surprise five Goblins who are in the middle of a game
             of chess. Each with an even uglier clown costume than 
             the last. They haven't pulled their weapons out yet, as they 
             see the egg of death under your arm and don't want to set it 
             off        
            """))
        
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                ..............................................................
                In a panic you throw the egg of death at the group of Goblins
                and make a leap for the door. Right as you drop it, a Goblin
                blasts you right in the back killing you. As you die you see
                the Goblins frantically trying to disarm the egg. You die knowing
                they will all die when the egg activates.
                """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                .............................................................
                You point your wand at the egg under your arm and the Goblins
                put their hands up and start to sweat. You inch backward to the
                door, open it, and then carefully place the bomb on the floor,
                pointing your wand at it. You then jump back through the door,
                slam the door close and blast the lock so the Goblins can get out.
                Now that the egg of death is placed, your run the Exit room to
                get off this castle.
                """))
            return 'exit_room'

        else:
            print("DOES NOT COMPUTE")
            return "gryffins_roost"

class ExitRoom(scene):

    def enter(self):
        print(dedent("""
            .................................................................
             You rush through the castle desperately trying to make it to the 
             exit room before the egg of death destroys the whole castle. The 
             way is clear of Goblins as you run into the exit room, you find 
             three portkeys. Some of them could be damaged but you don't have 
             time to look, which one do you take?  
            """))
        
        good_portkey = randint(1,3)
        guess = input("[portkey #]> ")

        if int(guess) != good_portkey:
            print(dedent("""
                ..........................................................
                You grab portkey number {guess} and it starts spinning.
                The portkey starts emitting static electricity and implodes,
                crushing your body into jam jelly.
                """))
            return 'death'
        else:
            print(dedent("""
                ............................................................
                You grab portkey number {guess} and it starts spinning.
                It drags your body to its epicenter and you suddenly find
                find yourself on a hill top close to the castle. You watch 
                as the green arm of death covers the castle killing everything
                within. You won!
                """))
            return 'finished'

class finished(scene):

    def enter(self):
        print("You won! Good Job.")
        return 'finished'

class Map(object):

    scenes = {
        'great_hall': GreatHall(),
        'potions_lab': PotionsLab(),
        'gryffins_roost': GryffinsRoost(),
        'exit_room': ExitRoom(),
        'death': death(),
        'finished': finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('great_hall')
a_game = engine(a_map)
a_game.play()
