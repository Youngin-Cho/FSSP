from environment.env import PFSP
from algorithm.heuristics import *


if __name__ == '__main__':
    num_jobs = 20
    num_machines = 5
    initial_seed = 873654221
    # file_path = "./data/pfsp_3_4.txt"

    env = PFSP(num_jobs, num_machines, initial_seed=initial_seed)
    # env = PFSP(num_jobs, num_machines, file_path=file_path)
    solution, makespan = NEH(env)

    print(solution)
    print(makespan)