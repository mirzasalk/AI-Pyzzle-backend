from puzzle.logic.state import get_pos_2d


class Heuristic:
    def get_evaluation(self, state):
        pass


class HammingHeuristic(Heuristic):
    def get_evaluation(self, state):
        h = 0
        for ident in range(len(state)):
            goal_place_1d = ident - 1 if ident else len(state) - 1
            current_place_1d = state.index(ident)
            if current_place_1d != goal_place_1d:
                h += 1
        return h




class ManhattanHeuristic(Heuristic):
    def get_evaluation(self, state):
        h_value = 0
        size = int(len(state) ** 0.5)  # Računanje veličine matrice

        for i in range(size):
            for j in range(size):
                value = state[i * size + j]
                if value != 0:
                    goal_row, goal_col = get_pos_2d(value - 1, size)  # Prosleđivanje size
                    h_value += abs(i - goal_row) + abs(j - goal_col)

        return h_value