# puzzle/logic/config.py

# Podrazumevana veličina matrice (default: 3x3)
DEFAULT_MATRIX_SIZE = 3

# Minimalna dozvoljena veličina matrice
MIN_MATRIX_SIZE = 2

# Lista podržanih algoritama sa opisima
SUPPORTED_ALGORITHMS = {
    "breadth_first_search": "Breadth First Search Algorithm",
    "a_star": "A* Algorithm",
    "greedy_best_first_search": "Greedy Best First Search Algorithm",  # Dodato za GBFS
}

# Lista podržanih heuristika sa opisima
SUPPORTED_HEURISTICS = {
    "hamming": "Hamming Distance",
    "manhattan": "Manhattan Distance",
}

# Podešavanja simulacije
SIMULATION_SETTINGS = {
    "step_delay": 0.5,  # Kašnjenje u prikazu koraka (u sekundama)
}
