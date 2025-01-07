import numpy as np
import logging




def get_pos_2d(index, size):
    """Konvertuje 1D indeks u 2D koordinate."""
    row = index // size
    col = index % size
    return row, col
logging.basicConfig(level=logging.DEBUG)

def get_inversion_count(state):
    inversion_count = 0
    last_tile_val = len(state)
    for i in range(last_tile_val - 1):
        for j in range(i + 1, last_tile_val):
            if state[i] and state[j] and state[i] > state[j]:
                inversion_count += 1
    return inversion_count

def is_solvable(state):
    inversion_count = get_inversion_count(state)
    size = int(len(state) ** 0.5)

    if size % 2 == 1: 
        return inversion_count % 2 == 0
    elif size == 2:  
     
        
        return inversion_count % 2 == 0
    else: 
        
        zero_row = state.index(0) // size
        return (inversion_count + zero_row) % 2 == 0


def get_init_and_goal_states(size, seed=None):
    """Generiše početno i ciljno stanje za zadatu veličinu matrice."""
    if seed is not None:
        np.random.seed(seed)  # Postavljanje semena ako je prosleđeno

    # Ciljno stanje
    goal_state = tuple(list(range(1, size ** 2)) + [0])  # Poslednji element je 0

    # Generisanje nasumičnog početnog stanja
    while True:
        initial_state = np.random.permutation(size ** 2).tolist()  # Nasumično stanje
        if is_solvable(initial_state) and tuple(initial_state) != goal_state:
            break

    initial_state = tuple(initial_state)
    return initial_state, goal_state