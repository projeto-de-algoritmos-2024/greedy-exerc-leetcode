class MinEnergy:

    tasks : list[list[int]]
    start_energy : int
    total_energy : int


    def __init__(self, tasks : list[list[int]]):
        self.tasks = tasks
        self.start_energy = 0
        self.total_energy = 0

    def minInitialEnergy(self) -> int:

        self.tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        for actual, minimum in self.tasks:
            if self.total_energy < minimum:
                self.start_energy += minimum - self.total_energy
                self.total_energy = minimum
            self.total_energy -= actual

        return self.start_energy

class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        min_energy = MinEnergy(tasks)
        return min_energy.minInitialEnergy()

#solution = Solution()
#print(solution.minimumEffort([[1,2],[2,4],[4,8]])) #Output 8
#print(solution.minimumEffort([[1,3],[2,4],[10,11],[10,12],[8,9]])) #Output 32
#print(solution.minimumEffort([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]])) #Output 27

