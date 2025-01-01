from collections import deque
import heapq
from puzzle.logic.state import is_solvable


class Algorithm:
   
    def __init__(self, heuristic=None, size=3):
        self.heuristic = heuristic
        self.size = size  # Dodajemo atribut za veličinu matrice
        self.nodes_evaluated = 0
        self.nodes_generated = 0

    def get_legal_actions(self, state):
        self.nodes_evaluated += 1
        max_index = len(state)
        zero_tile_ind = state.index(0)
        legal_actions = []
        
        size = self.size  # Koristimo self.size umesto fiksne veličine 3
        
        if 0 <= (up_ind := zero_tile_ind - size) < max_index:
            legal_actions.append(up_ind)
        if 0 <= (right_ind := zero_tile_ind + 1) < max_index and right_ind % size != 0:
            legal_actions.append(right_ind)
        if 0 <= (down_ind := zero_tile_ind + size) < max_index:
            legal_actions.append(down_ind)
        if 0 <= (left_ind := zero_tile_ind - 1) < max_index and zero_tile_ind % size != 0:
            legal_actions.append(left_ind)
        
        return legal_actions


    def apply_action(self, state, action):
        self.nodes_generated += 1
        copy_state = list(state)
        zero_tile_ind = state.index(0)
        copy_state[action], copy_state[zero_tile_ind] = (
            copy_state[zero_tile_ind],
            copy_state[action],
        )
        return tuple(copy_state)

    def get_steps(self, initial_state, goal_state):
        pass


class BreadthFirstSearch(Algorithm):
    def get_steps(self, initial_state, goal_state):
        visited_states = set()
        visited_states.add(initial_state)
        queue = deque([(initial_state, [])])

        while queue:
            current_state, current_path = queue.popleft()

            if current_state == goal_state:
                return current_path

            legal_actions = self.get_legal_actions(current_state)

            for action in legal_actions:
                next_state = self.apply_action(current_state, action)

                if next_state not in visited_states:
                    visited_states.add(next_state)
                    queue.append((next_state, current_path + [action]))

        return []


class AStar(Algorithm):

    def __init__(self, heuristic=None, size=3):
        super().__init__(heuristic, size=size)  # Prosleđujemo veličinu matrice
        self.explored_states = set()

    def get_steps(self, initial_state, goal_state):
        open_set = [(0, initial_state, [])]
        heapq.heapify(open_set)
        g_values = {initial_state: 0}

        while open_set:
            current_f, current_state, actions = heapq.heappop(open_set)
            if current_state == goal_state:
                return actions

            if current_state not in self.explored_states:
                self.explored_states.add(current_state)
                legal_actions = self.get_legal_actions(current_state)

                for action in legal_actions:
                    successor_state = self.apply_action(current_state, action) 

                    cost = g_values[current_state] + 1

                    if successor_state not in g_values or cost < g_values[successor_state]:
                        g_values[successor_state] = cost
                        h_value = self.heuristic.get_evaluation(successor_state)
                        f_value = cost + h_value
                        heapq.heappush(
                            open_set, (f_value, successor_state, actions + [action])
                        )

        return None

class GreedyBestFirstSearch(Algorithm):
    def __init__(self, heuristic=None, size=3):
        super().__init__(heuristic, size)
        self.explored_states = set()

    def get_steps(self, initial_state, goal_state):
        open_set = [(self.heuristic.get_evaluation(initial_state), initial_state, [])]
        heapq.heapify(open_set)

        while open_set:
            _, current_state, actions = heapq.heappop(open_set)

            if current_state == goal_state:
                return actions

            if current_state not in self.explored_states:
                self.explored_states.add(current_state)

                legal_actions = self.get_legal_actions(current_state)

                for action in legal_actions:
                    successor_state = self.apply_action(current_state, action)
                    if successor_state not in self.explored_states:
                        h_value = self.heuristic.get_evaluation(successor_state)
                        heapq.heappush(
                            open_set, (h_value, successor_state, actions + [action])
                        )

        return None
