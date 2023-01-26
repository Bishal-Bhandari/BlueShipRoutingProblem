import random
import numpy as np


# Two point mutation
def TwoPointMutation(x_value, y_value):
    for mut_i in range(len(x_value)):
        index_v = range(len(x_value[mut_i]))
        print(index_v)
        ix1, ix2 = random.sample(index_v, 2)
        print(ix1, ix2)
        x_value[mut_i][ix1], x_value[mut_i][ix2] = x_value[mut_i][ix2], x_value[mut_i][ix1]
        y_value[mut_i][ix1], y_value[mut_i][ix2] = y_value[mut_i][ix2], y_value[mut_i][ix1]
    return x_value, y_value


class CrossoverMutation:
    def __init__(self, selected_chromosome):
        self.selected_chromosome = selected_chromosome
        self.dict_value = 0
        self.min_range_Crossover = 5  # Range for crossover
        self.crossover_max_len = []
        self.temp_x = []
        self.temp_y = []
        self.child_x = []
        self.child_y = []
        self.crossover_int = []

    def crossover(self):
        dict_value = list(self.selected_chromosome.values())
        for i in range(len(self.selected_chromosome)):
            self.temp_x.append(dict_value[i][0])
            self.temp_y.append(dict_value[i][1])
            self.crossover_max_len.append(len(self.temp_x[i]))

        for x_index in range(len(self.selected_chromosome)):
            self.crossover_int.append(np.random.uniform(
                self.min_range_Crossover,
                self.crossover_max_len[x_index],
                size=1))

        i_index = 0
        while i_index < (len(self.temp_x) - 1):
            temp_child_x = []
            temp_child_y = []
            for j_index in range(min(len(self.temp_x[i_index]), len(self.temp_x[i_index + 1]))):
                if self.crossover_int[i_index] <= j_index <= self.crossover_max_len[i_index]:
                    temp_child_x.insert(j_index, self.temp_x[i_index + 1][j_index])
                    temp_child_y.insert(j_index, self.temp_y[i_index + 1][j_index])
                else:
                    temp_child_x.insert(j_index, self.temp_x[i_index][j_index])
                    temp_child_y.insert(j_index, self.temp_y[i_index][j_index])
            self.child_x.append(temp_child_x)
            self.child_y.append(temp_child_y)
            i_index += 1
        mutant_child_x, mutant_child_y = TwoPointMutation(self.child_x, self.child_y)
        self.child_x.extend(mutant_child_x)
        self.child_y.extend(mutant_child_y)
        return self.child_x, self.child_y
