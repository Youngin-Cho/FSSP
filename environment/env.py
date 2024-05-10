import numpy as np

from environment.data import DataGenerator


class PFSP:
    def __init__(self, num_jobs, num_machines, file_path=None, initial_seed=None):
        self.num_jobs = num_jobs
        self.num_machines = num_machines

        if file_path is None:
            self.data_src = DataGenerator(num_jobs, num_machines)
            self.processing_time = self.data_src.generate(initial_seed)
        else:
            with open(file_path, 'r') as f:
                self.processing_time = np.array([line.split() for line in f.readlines()]).astype('int')

    def get_processing_time(self):
        return self.processing_time

    def calculate_makespan(self, solution):
        solution = solution - 1
        processing_time = self.processing_time[:, solution]

        num_machines, num_jobs = processing_time.shape
        completion_time = np.zeros((num_machines + 1, num_jobs + 1))
        for i in range(1, num_machines + 1):
            for j in range(1, num_jobs + 1):
                temp = max(completion_time[i, j - 1], completion_time[i - 1, j])
                completion_time[i, j] = temp + processing_time[i - 1, j - 1]
        makespan = completion_time[num_machines, num_jobs]

        return makespan


if __name__ == '__main__':
    num_machines = 3
    num_jobs = 4
    file_path = "../data/pfsp_3_4.txt"
    solution = np.array([1, 4, 2, 3])

    env = PFSP(num_jobs, num_machines, file_path=file_path)
    makespan = env.calculate_makespan(solution)
    print(makespan)