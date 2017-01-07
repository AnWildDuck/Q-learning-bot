import random, math


def warning_message():
        print()
        print('--------------------------------')
        print()
        print('WARNING! the wall generation order is off. This may end up making the game impossible... You have been warned')
        print()
        print('PS. If you really want this to work I suggest turning the spawn chance down')
        print()
        print('--------------------------------')
        print()


def single(grid_size, ordered = True, spawn_chance = 0.5):
    blocks = []
    chance = 1 / spawn_chance

    if ordered:
        for column in range(grid_size):
            for row in range(grid_size):
                
                if row % chance == 0 and column % chance == 0:

                    # Make sure finish is still accessible
                    if column < grid_size - 2 or row > 2:
                        blocks.append((column, row))

    else:
        warning_message()
        for column in range(grid_size):
            for row in range(grid_size):

                if random.random() < spawn_chance:

                    # Make sure finish is still accessible
                    if column < grid_size - 2 or row > 1:
                        blocks.append((column, row))
    return blocks




# Not working yet

def chunks(grid_size, radius, chunks, ordered = True):
    blocks = []
    centers = []
    
    if ordered:
        chunks_side_value = int(math.sqrt(chunks))

        # Make centers
        for xchunk in range(chunks_side_value):
            for ychunk in range(chunks_side_value):

                x = (grid_size // chunks_side_value)
                y = (grid_size // chunks_side_value)
            
                centers.append((x, y))

    else:
        warning_message()

        #Make centers
        for chunk in range(chunks):
            centers.append((random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)))

        
    blocks = list(centers)

    print(centers)

    # Make blocks around center
    for cx, cy in centers:

        # Positions are relative to center
        for x in range(-radius, radius):
            for y in range(-radius, radius):

                blocks.append((x + cx, y + cy))

    return blocks

















                




    
