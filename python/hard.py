from colorama import Fore, init, deinit
from random import randint
from os import system
import python.Generate_lock as Generate_lock

# Junin's Sheet
lockpicking_skill = 5

Generate_lock.generate_lock(5, 10, 1, True)

# pointer coordinates
point_text_position = 3  # 3 represents the initial number position in text
point_array_position = 0
pointer = Fore.YELLOW + '^'


lock_key = 0


def interface(on=True):
    if on:
        init()
        visible_springs_interface = []
        # put the springs visible in another array
        for i in range(0, lockpicking_skill):
            visible_springs_interface.append(Generate_lock.springs[i])
        counter = -1
        for _ in visible_springs_interface:
            counter += 1
            # verify if the point is in the same number and if this number already was hit
            if (point_array_position == counter) and (counter in Generate_lock.numbers_already_hitted):
                print(f"{Fore.YELLOW + '['} {Fore.GREEN + 'X'} {Fore.YELLOW + ']'}", end='')
            # verify is the number already was hit
            elif counter in Generate_lock.numbers_already_hitted:
                print(f"{Fore.RESET + '['} {Fore.GREEN + 'X'} {Fore.RESET + ']'}", end='')
            # Simply transform the parentheses in the same colo of the point if it is in the number
            elif point_array_position == counter:
                print(f"{Fore.YELLOW + '['} {Fore.RESET + 'X'} {Fore.YELLOW + ']'}", end='')
            # Just print the number in the normal form
            else:
                print(f"{Fore.RESET + f'[ X ]' + Fore.YELLOW}", end='')
            # Put the point below ant move it
            if (counter == len(visible_springs_interface) - 1) and point_text_position <= (
                    lockpicking_skill - 1) * 5 + 3:
                print(f"\n{'^':>{point_text_position}}")
                print(f"{Fore.RESET}")
            # if the circumstances have not reached, so it will reset color, and skip the line
            elif counter >= len(visible_springs_interface) - 1:
                print(f"\n{Fore.RESET}")
        deinit()


while True:
    interface()
    user_input = input("waiting...\n>")
    system('cls')
    try:  # Lockpicking.
        if len(Generate_lock.lock_unlock_order) > 0:  # verify if the lock has order 
            # verify if the order is correct
            if (int(user_input) == Generate_lock.springs[point_array_position]) and \
                    (point_array_position == Generate_lock.lock_unlock_order[lock_key]):
                print('*click*')
                lock_key += 1
                Generate_lock.numbers_already_hitted.append(point_array_position)
                already_printed = True
            elif lock_key >= 1:  # reset the hitted springs
                print("*clenk*")
                lock_key = 0
                already_printed = False
                Generate_lock.numbers_already_hitted.clear()
        elif int(user_input) == Generate_lock.springs[point_array_position]:  # locker w/out order
            print('*click*')
            Generate_lock.numbers_already_hitted.append(point_array_position)
        else:
            already_printed = False
        # fake clicks system
        if len(Generate_lock.fake_clicks_positions) > 0 and lockpicking_skill < len(Generate_lock.springs):
            false_click_chance = ((len(Generate_lock.springs) - lockpicking_skill + 1) / len(
                Generate_lock.springs)) * 100
            if point_array_position in Generate_lock.fake_clicks_positions:
                RNG = randint(1, 100)
                if RNG > false_click_chance and not already_printed:
                    print("*click*")
    except ValueError:
        pass
    if user_input == "next":
        if point_text_position + 5 <= (len(Generate_lock.springs) - 1) * 5 + 3:
            point_text_position += 5
            point_array_position += 1
        else:
            print("You are in the last spring")
    elif user_input == "previous":
        if point_text_position - 5 >= 3:
            point_text_position -= 5
            point_array_position += -1
        else:
            print("You are in the first spring")
    elif user_input == "open":
        if len(Generate_lock.numbers_already_hitted) == len(Generate_lock.springs):
            print("You opened the lock")
            break
        else:
            Generate_lock.lock_durability - (Generate_lock.lock_durability / Generate_lock.springs) * \
                len(Generate_lock.springs) - len(Generate_lock.numbers_already_hitted)
    elif user_input == "help":
        print('>put a number until this match of the number of spring\n'
              '>"Open" you will try to open\n'
              '>"next" to go to next spring\n'
              '>"previous" to go to previous spring\n'
              '>"Exit" to exit\n')
    elif user_input == "exit" or Generate_lock.lock_durability <= 0:
        break
    else:
        print("You can type print, to see the commands.")
