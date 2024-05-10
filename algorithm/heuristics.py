import numpy as np


def NEH(env):
    processing_time = env.get_processing_time()
    processing_time_sum = np.sum(processing_time, axis=0)
    # print(processing_time_sum)
    initial_sequence = np.argsort(processing_time_sum)[::-1] + 1
    # print(initial_sequence)

    solution = []
    for i in range(len(initial_sequence)):
        if len(solution) == 0:
            solution.insert(0, initial_sequence[i])
        else:
            # print("====%d====" % i)
            makespan_lst = []
            for idx in range(len(solution) + 1):
                # print(idx)
                temp_solution = solution[:]
                temp_solution.insert(idx, initial_sequence[i])
                # print(temp_solution)
                makespan = env.calculate_makespan(np.array(temp_solution))
                # print(makespan)
                makespan_lst.append(makespan)

            best_idx = np.random.choice(np.where(makespan_lst == min(makespan_lst))[0])
            solution.insert(best_idx, initial_sequence[i])
            # print("partial_sequence: " + str(solution))

    solution = np.array(solution)
    makespan = env.calculate_makespan(solution)
    return solution, makespan


def Palmer(env):
    processing_time = env.get_processing_time()

    slope_index = np.zeros(env.num_jobs)
    for j in range(env.num_jobs):
        temp = processing_time[:, j]
        for i in range(1, env.num_machines + 1):
            slope_index[j] += (2 * i - env.num_machines - 1) * temp[i - 1] / 2

    solution = slope_index.argsort()[::-1] + 1
    makespan = env.calculate_makespan(solution)
    return solution, makespan