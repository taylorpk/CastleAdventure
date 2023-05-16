import random

monster = ['ghost', 'vampire', 'zombie', 'witch']
location = ['kitchen', 'bedroom', 'attic', 'basement']
item = ['bow', 'staff', 'sword', 'knife']

newMonster = ['clown', 'werewolf', 'basilisk', 'mummy']

compNewMonster = (random.choice(newMonster))

comp_monster = (random.choice(monster))
comp_location = (random.choice(location))
comp_item = (random.choice(item))

comp_weapon = random.randint(0,10)
player_weapon = random.randint(0,10)

player_weapon2 = random.randint(0,15)
comp_weapon2 = random.randint(0,15)

player_no_weapon = random.randint(0,20)
comp_no_weapon = random.randint(0,20)

player_no_weapon2 = random.randint(0,30)
comp_no_weapon2 = random.randint(0,30)

#items
def bedroomScene():
    q10 = input(f'You find a {comp_item}. Do you want to pick it up? (yes/no) ')
    match q10:
        case 'yes':
            globals()[comp_location + '3Scene']()
            quit()

        case 'no':
            globals()[comp_location + '2Scene']()

def basementScene():
    q11 = input(f'You find a {comp_item}. Do you want to pick it up? (yes/no) ')
    match q11:
        case 'yes':
            globals()[comp_location + '3Scene']()
            quit()

        case 'no':
            globals()[comp_location + '2Scene']()

def kitchenScene():
    q12 = input(f'You find a {comp_item}. Do you want to pick it up? (yes/no) ')
    match q12:
        case 'yes':
            globals()[comp_location + '3Scene']()
            quit()

        case 'no':
            globals()[comp_location + '2Scene']()

def atticScene():
    q13 = input(f'You find a {comp_item}. Do you want to pick it up? (yes/no) ')
    match q13:
        case 'yes':
            globals()[comp_location + '3Scene']()
            quit()

        case 'no':
            globals()[comp_location + '2Scene']()

#weapons
def bedroom3Scene():
    q30 = input(f'Hopefully this will come in handy. \nYou turn around and see a {compNewMonster}! Do you want to fight? (yes/no) ')
    match q30:
        #weapon #fight
        case 'yes':
            if player_weapon >= comp_weapon:
                print('You break out the weapon you just found.\nYou defeat him and escape into the woods!')
                quit()

            if player_weapon < comp_weapon:
                print("You break out your new weapon.\nYou give it your all, but that doesn't seem to be enough.\nHe kills you and waits for his next victim.")
                quit()
        #weapon #no fight
        case 'no':
            if player_weapon2 >= comp_weapon2:
                print('You outrun him. You finally make it out of the castle!\nYou run into the woods without looking back. ')

            if player_weapon2 < comp_weapon2:
                print("You try to outrun him, but he's too fast.\nHe kills you and waits for his next victim.")
                quit()

def basement3Scene():
    q31 = input(f"You pick it up and dust it off. It may be old, but it's better than nothing.\nYou turn around and see a {compNewMonster}! Do you want to fight? (yes/no) ")
    match q31:
        case 'yes':
        #weapons #fight
            if player_weapon >= comp_weapon:
                print('Looks like you found that weapon just in time!\nYou defeat him and get out as fast as you can. ')
                quit()
            
            if player_weapon < comp_weapon:
                print("Your old weapon isn't enough. He kills you and waits for his next victim.")
                quit()
        #weapons #no fight
        case 'no':
            if player_weapon2 >= comp_weapon2:
                print('You outrun him and finally make it out of the castle!\nYou run into the woods without looking back. ')

            if player_weapon2 < comp_weapon2:
                print("You try to outrun him, but he's too fast.\nHe kills you and waits for his next victim.")
                quit()

def kitchen3Scene():
    q32 = input(f"Great! Hopefully you won't have to use it.\nYou turn around and see a {compNewMonster}! Do you want to fight? (yes/no) ")
    match q32:
        #weapons #fight
        case 'yes':
            if player_weapon >= comp_weapon:
                print('Looks like you found that weapon just in time!\nYou defeat him and get out as fast as you can. ')
                quit()
            
            if player_weapon < comp_weapon:
                print("You break out your new weapon.\nYou give it your all, but it's not enough.\nYou are killed and he waits for his next victim.")
                quit()
        #weapons #no fight
        case 'no':
            if player_weapon2 >= comp_weapon2:
                print('You make a run for it. Finally, you make it out of the castle! \nYou run into the woods without looking back. ')
            
            if player_weapon2 < comp_weapon2:
                print("You try to outrun him, but hes's too fast.\nHe kills you and waits for his next victim.")
                quit()

def attic3Scene():
    q33 = input(f"You pick it up and dust it off. Looks like it's been here a while.\nYou turn around and see a {compNewMonster}! Do you want to fight? (yes/no) ")
    #weapon #fight
    match q33:
        case 'yes':
            if player_weapon >= comp_weapon:
                print('Looks like you found that weapon just in time!\nYou defeat him and get out as fast as you can. ')
                quit()

            if player_weapon < comp_weapon:
                print("You break out your dusty weapon.\nBut, it's not enough.\nYou are killed and he waits for his next victim.")
                quit()

        case 'no':
            #weapon #no fight
            if player_weapon2 >= comp_weapon2:
                print('You smash the window open and climb down.\nYou run into the woods without looking back. ')

            if player_weapon2 < comp_weapon2:
                print("You try to outrun him, but he's too fast.\nHe kills you and waits for his next victim.")
                quit()

#no weapons
def bedroom2Scene():
    q20 = input(f'You see a {compNewMonster}! Do you want to fight? (yes/no) ')
    match q20:
        #no weapons #fight
        case 'yes':
            if player_no_weapon >= comp_no_weapon:
                print('You fight as hard as you can and you are victorious!\nYou escape into the woods and never look back. ')
                quit()

            if player_no_weapon < comp_no_weapon:
                print("No matter how hard you fight, he's too strong.\nHe kills you and waits for his next victim. ")
                quit()
        #no weapons #no fight
        case 'no':
            if player_no_weapon2 >= comp_no_weapon2:
                print('You outrun him and climb out the nearest window. \nYou run into the woods without looking back. ')
                quit()
            
            if player_no_weapon2 < comp_no_weapon2:
                print("You try to outrun him, but he's too fast.\nHe kills you and waits for its next victim.")
                quit()

def basement2Scene():
    q21 = input(f'You see a {compNewMonster}! Do you want to fight? (yes/no) ')
    match q21:
        #no weapons #fight
        case 'yes':
            if player_no_weapon >= comp_no_weapon:
                print('You fight as hard as you can and you are victorious!\nYou escape into the woods and never look back. ')
                quit()
            
            if player_no_weapon < comp_no_weapon:
                print("No matter how hard you fight, he's too strong.\nHe kills you and waits for his next victim. ")
                quit()
        #no weapons #no fight
        case 'no':
            if player_no_weapon2 >= comp_no_weapon2:
                print("You run up the stairs as fast as you can. Finally, !\nYou run into the woods without looking back. ")
                quit()
            
            if player_no_weapon2 < comp_no_weapon2:
                print("You try to outrun him, but he's too fast.\nHe kills you and waits for his next victim.")
                quit()

def kitchen2Scene():
    q22 = input(f'You see a {compNewMonster}! Do you want to fight? (yes/no) ')
    match q22:
        #no weapons #fight
        case 'yes':
            if player_no_weapon >= comp_no_weapon:
                print('You fight as hard as you can and you are victorious!\nYou escape into the woods and never look back. ')
                quit()
            
            if player_no_weapon < comp_no_weapon:
                print("No matter how hard you fight, he's too strong.\nHe kills you and waits for his next victim. ")
                quit()
        #no weapons #no fight
        case 'no':
            if player_no_weapon2 >= comp_no_weapon2:
                print('You smash open a window and jump through. \nYou run into the woods without looking back. ')
                quit()
            
            if player_no_weapon2 < comp_no_weapon2:
                print("You try to outrun him, but he's too fast.\nHe kills you and waits for his next victim.")
                quit()

def attic2Scene():
    q23 = input(f'You see a {compNewMonster}! Do you want to fight? (yes/no) ')
    match q23:
        #no weapons #fight
        case 'yes':
            if player_no_weapon >= comp_no_weapon:
                print('You fight as hard as you can and you are victorious!\nYou escape into the woods and never look back. ')
                quit()
            
            if player_no_weapon < comp_no_weapon:
                print("No matter how hard you fight, he's too strong.\nHe kill you and waits for his next victim. ")
                quit()
        #no weapons #no fight
        case 'no':
            if player_no_weapon2 >= comp_no_weapon2:
                print('You quickly find a ladder and climb down. By some miracle, you make it out alive!\nYou run into the woods without looking back. ')
                quit()
            
            if player_no_weapon < comp_no_weapon2:
                print("You try to outrun him, but he's too fast.\nHe kills you and waits for his next victim.")
                quit()

#fight
def ghostFightScene():
    q5 = input(f'You scare it off and go to the {comp_location}. \nDo you want to look around? (yes/no) ')
    match q5:
        case 'yes':
            if comp_location == 'attic':
                print('You found an old baseball bat! \nYou smash the window open and climb down the roof.')
                quit()
            globals()[comp_location + 'Scene']()
        case 'no':
            if comp_location == 'attic':
                print('You see the night sky through the window.\nAfter some time, you manage to wedge it open.\nYou climb down the roof and run into the woods.')
                quit()
            globals()[comp_location + '2Scene']()

def vampireFightScene():
    q6 = input(f'You barely make it and run to the {comp_location}. \nDo you want to take a look around? (yes/no) ')
    match q6: 
        case 'yes':
            if comp_location == 'basement':
                print('You look over to see an open window. \nYou squeeze your way out of the window and into the forest. ')
                quit()
            globals()[comp_location + 'Scene']()

        case 'no':
            if comp_location == 'basement':
                print('You can feel a slight breeze through an open window. \nYou squeeze your way out and run back into the forest. You win!')
                quit()
            globals()[comp_location + '2Scene']()        
        
def zombieFightScene():
    q7 = input(f'You manage to kill the zombie and run into the {comp_location}. \nDo you want to go look around? (yes/no) ')
    match q7:
        case 'yes':
            if comp_location == 'bedroom':
                print('You sneak out of the window and run into the woods. ')
                quit()
            globals()[comp_location + 'Scene']()
        case 'no':
            if comp_location == 'bedroom':
                print('You find a way out through an open window. ')
                quit()
            globals()[comp_location + '2Scene']()

def witchFightScene():
    q8 = input(f'You pick up a rock and throw it at her.\nYou find yourself in the {comp_location}. \nDo you want to take a look around? (yes/no) ')
    match q8:
        case 'yes':
            if comp_location == 'kitchen':
                print('As you look around you find a knife! \nYou manage wedge the window open. \nYou quickly jump out the window.')
                quit()
            globals()[comp_location + 'Scene']()        

        case'no':
            if comp_location == 'kitchen':
                print('You look up and see the window is slightly opened. \nYou manage to squeeze through and escape outside.')
                quit()
            globals()[comp_location + '2Scene']()               

#run
def witchScene():
    q2 = input(f'You outrun her and escape to the {comp_location}. \nDo you want to look around? (yes/no) ')
    match q2:
        case 'yes':
            if comp_location == 'kitchen':
                print('Her again! As you turn to run, she casts a spell and turns you into a frog.')
                quit()
            globals()[comp_location + 'Scene']()
        
        case 'no':
            if comp_location == 'kitchen':
                print('She casts a spell and turned you into a frog.')
                quit()
            globals()[comp_location + '2Scene']()
            
def ghostScene():
    q3 = input(f'You are able to escape to the {comp_location} unnoticed. \nDo you want to look around? (yes/no) ')
    match q3:
        case 'yes':
            if comp_location == 'attic':
                print('The TV in the corner turns on. \nYou try to get out, but you turn around to see the ghost. \nThe ghost traps you and you are forced to haunt the castle forever.')
                quit()
            globals()[comp_location + 'Scene']()    
            
        case 'no':
            if comp_location == 'attic':
                print('The ghost sneaks up behind you. He traps you, forcing you to haunt the castle forever.')
                quit()
            globals()[comp_location + '2Scene']()
                
def vampireScene():
    q4 = input(f'You run as fast as you can! \nTerrified, you find yourself in the {comp_location}. \nDo you take a look around? (yes/no) ')
    match q4:
        case 'yes':
            if comp_location == 'basement':
                print("You're in his lair! He traps you and you become a vampire.")
                quit()
            globals()[comp_location + 'Scene']()        
            
        case 'no':
            if comp_location == 'basement':
                print('You see beautiful mirror. \nAs you look into it, you sense that something is behind you. \nThe vampire bites you and you become a vampire. ')
                quit()
            globals()[comp_location + '2Scene']()

def zombieScene():
    print ('The zombie is too fast! He catches up to you and eats your brains.')
    quit()

welcome = """
                                            
                                *                    *
                              *   *                *   *     ***   ***
                            *       *            *       *     ** **    
            ***    ***     ***********          ***********      **     
              **  **         *     *              *     *
                **           *     *              *     *
                             *     **********************
                             *     *                     *                  *
                             *     *   *      *      *   *                *   *  
                             *     *  * *    * *    * *  *       *       *     *     *      
                             *     *   *      *      *   *     *   *    *       *  *   *
                             *     *                     *   *       * *         *      *     
                             *     *                     * *          *           *      *     
                             **************************************************************

"""                                          
print(welcome)

q1 = input(f'As you wander around the woods, you encounter a castle that is rumored to be haunted. \nYour curiosity gets the better of you, so you enter anyway. \nYou see a {comp_monster} in the castle. What do you do? (run/fight) ')
match q1: 
    case 'run':
        globals()[comp_monster + 'Scene']()
    case 'fight':
        globals()[comp_monster + 'FightScene']()
