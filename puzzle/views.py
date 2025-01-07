from rest_framework.views import APIView
from rest_framework.response import Response
from puzzle.logic.algorithms import BreadthFirstSearch, AStar, GreedyBestFirstSearch  # Dodaj GreedyBestFirstSearch
from puzzle.logic.heuristics import HammingHeuristic, ManhattanHeuristic
from puzzle.logic.state import get_init_and_goal_states
from puzzle.logic import config
from PIL import Image
import os


# Pokretanje simulacije
class RunSimulationView(APIView):
    def post(self, request):
        # Preuzmi parametre
        algorithm = request.data.get('algorithm')
        heuristic = request.data.get('heuristic')
        size = int(request.data.get('size', 3))
        
        # Postavi veličinu matrice
        config.N = size

        # Generiši početno i ciljno stanje
        initial_state, goal_state = get_init_and_goal_states(size)

        # Kreiraj heuristiku
        heuristic_instance = None
        if heuristic == "hamming":
            heuristic_instance = HammingHeuristic()
        elif heuristic == "manhattan":
            heuristic_instance = ManhattanHeuristic()

        if not heuristic_instance:
            return Response({"error": "Invalid heuristic"}, status=400)

        # Kreiraj algoritam
        solver = None
        if algorithm == "breadth_first_search":
            solver = BreadthFirstSearch(size=size)  # Prosleđivanje veličine matrice
        elif algorithm == "a_star":
            solver = AStar(heuristic_instance, size=size)
        elif algorithm == "greedy_best_first_search":  # Dodaj ovu opciju
            solver = GreedyBestFirstSearch(heuristic_instance, size=size)  # Prosleđivanje veličine matrice i heuristike



        # Pokreni algoritam
        if not solver:
            return Response({"error": "Invalid algorithm"}, status=400)

        steps = solver.get_steps(initial_state, goal_state)

        return Response({
            "initial_state": initial_state,
            "goal_state": goal_state,
            "steps": steps
        })

