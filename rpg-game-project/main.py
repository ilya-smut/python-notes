from classes.game import Person, Colors
from classes.magic import Spell
from classes.inventory import Item
from colorama import just_fix_windows_console


just_fix_windows_console()


# Black Magic
fire = Spell('Fire', 45, 150, 'black')
shock = Spell('Shock', 55, 180, 'black')

# White Magic
cure = Spell('Cure', 50, 200, 'white')

#Creating some items
heal_potion = Item('Healing potion', 'potion', 'Heals 100 HP', 100)
throwing_knife = Item('Throwing knife', 'weapon', 'Deals 200 DMG', 200)

inventory = {'items':[heal_potion, throwing_knife], 'ammo':{0: 1, 1: 1}}


player_magic = [fire, shock, cure]

player = Person(500, 100, 90, 40, player_magic, inventory)
enemy = Person(500, 100, 90, 40, player_magic, inventory)

running = True

while running:
    print('====================')
    player.choose_action()
    choice = input('Choose action: ')
    choice = int(choice) - 1
    if player.has_action(choice):
        print('You have choisen ' + Colors.BOLD + player.actions[choice] + Colors.ENDC)
    
    # Choosing manual attack
    if choice == 0:     
        dmg = player.generate_dmg()
        enemy.take_dmg(dmg)
        print('You attacked the enemy on ' + Colors.OKGREEN + str(dmg), Colors.ENDC + ". Enenemy's hp is " + str(enemy.get_hp()))    
        
    # Choosing magic
    elif choice == 1:           
        player.choose_magic()
        magic_choice = input('Choose the spell: ')
        magic_choice = int(magic_choice) - 1

        if magic_choice not in range(1, len(player.magic)):
            continue

        # Check on mp's
        if player.get_mp() < player.magic[magic_choice].cost:
            print(Colors.FAIL + 'You could not cast the spell' + Colors.ENDC)
            continue
        
        #Reducing mp and genrating dmg points
        player.reduce_mp(player.magic[magic_choice].cost)
        dmg = player.magic[magic_choice].generate_spell()

        if player.magic[magic_choice].type == 'black':
            enemy.take_dmg(dmg)
            print('You attacked the enemy on ' + Colors.OKGREEN + str(dmg), Colors.ENDC + ". Enenemy's hp is " + str(enemy.get_hp()))  

        elif player.magic[magic_choice].type == 'white':
            player.heal(dmg)
            print('You healed ' + Colors.OKGREEN + str(dmg), Colors.ENDC + ". Yours hp is " + str(player.get_hp()))    


    elif choice == 2:
        player.choose_item()
        item_choice = int(input('Choose an item: ')) - 1
        
        if item_choice not in range(1, len(player.items['items'])):
            continue

        if not player.has_item(item_choice):
            print(Colors.FAIL + 'You do not have that Item' + Colors.ENDC)
            continue
        else:
            item = player.items['items'][item_choice]
            dmg = item.prop
            if item.type == 'potion':
                player.heal(dmg)
                player.items['ammo'][item_choice] -= 1
                print('You healed ' + Colors.OKGREEN + str(dmg), Colors.ENDC + ". Yours hp is " + str(player.get_hp()))

            if item.type == 'weapon':
                enemy.take_dmg(dmg)
                player.items['ammo'][item_choice] -= 1
                print('You attacked the enemy on ' + Colors.OKGREEN + str(dmg), Colors.ENDC + ". Enenemy's hp is " + str(enemy.get_hp()))  

    else:
        continue

    # Enemy's Move
    enemy_choice = 0
    enemy_dmg = enemy.generate_dmg()
    player.take_dmg(enemy_dmg)
    print('Enemy attacks on ' + Colors.WARNING + str(enemy_dmg) + Colors.ENDC + ". Player's hp: " + str(player.get_hp()))
    # End of Enemy's move

    # Status Bar after every move
    print('------------------')
    print("Enemy's HP: " + Colors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp())+ Colors.ENDC + ", MP: " + Colors.OKBLUE +
                                         str(enemy.get_mp()) + "/" + str(enemy.get_maxmp()) + Colors.ENDC)

    print("Player's HP: " + Colors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp())+ Colors.ENDC + ", MP: " + Colors.OKBLUE +
                                         str(player.get_mp()) + "/" + str(player.get_maxmp()) + Colors.ENDC)
    print('------------------')
    # End of Status Bar

    # Checking hp in case someone's died
    if enemy.get_hp() == 0:
        print(Colors.OKGREEN + " YOU WIN!" + Colors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Colors.FAIL + " YOU LOSE!" + Colors.ENDC)
        running = False