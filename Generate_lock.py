from random import randrange

# generating the springs that will be inside of lock
springs = []
fake_clicks_positions = []
lock_unlock_order = []
lock_durability = 100
# each spring makes up the entire life of the padlock 


def generate_lock(quantity_spring: int = 3, lock_number_amplitude: int = 10, quantity_fake_clicks: int = 0,
                  lock_has_order: bool = False):

    # Control the limit of lock_number_amplitude
    if lock_number_amplitude > 25:
        return print("The lock number amplitude have a limit of 25")
    else:
        for i in range(0, quantity_spring):
            springs.append(randrange(lock_number_amplitude))

    # generate where are the fake clicks be
    for j in range(0, quantity_fake_clicks):
        fake_click_position = randrange(0, len(springs))
        while fake_click_position in fake_clicks_positions:
            fake_click_position = randrange(0, len(springs))
        fake_clicks_positions.append(fake_click_position)

    # define the order that the lock have to be unlocked
    if lock_has_order:
        while len(lock_unlock_order) != len(springs):
            lock_unlock_number = randrange(0, len(springs))
            while lock_unlock_number in lock_unlock_order:
                lock_unlock_number = randrange(0, len(springs))
            lock_unlock_order.append(lock_unlock_number)


numbers_already_hitted = []
