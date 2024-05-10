import math
import numpy as np


class DataGenerator:
    def __init__(self, num_jobs, num_machines):
        self.num_jobs = num_jobs
        self.num_machines = num_machines

        self.low = 1
        self.high = 99

        self.a = 16807
        self.b = 127773
        self.c = 2836
        self.m = pow(2, 31) - 1

    def get_random_number(self, seed):
        k = seed // self.b
        seed = self.a * (seed % self.b) - k * self.c
        if seed < 0:
            seed = seed + self.m

        value = seed / self.m
        value = math.floor(self.low + value * (self.high - self.low + 1))

        return value, seed

    def generate(self, initial_seed):
        seed = initial_seed
        processing_time = np.zeros((self.num_machines, self.num_jobs))

        for i in range(self.num_machines):
            for j in range(self.num_jobs):
                value, seed = self.get_random_number(seed)
                processing_time[i, j] = value
        return processing_time


if __name__ == '__main__':
    num_jobs = 20
    num_machines = 5
    initial_seed = 873654221

    data_generator = DataGenerator(num_machines, num_jobs)
    processing_time = data_generator.generate(initial_seed)
    print(processing_time)

