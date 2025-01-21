import heapq

class Scheduler:
    courses : list[list[int]]
    m_heap : list[list[int]]
    days_spend : int

    def __init__(self, courses : list[list[int]]):
        self.courses = courses
        self.m_heap = []
        self.days_spend = 0

    def scheduleCourse(self) -> int:
        self.courses.sort(key=lambda x: x[1])

        for duration, last_day in self.courses:
            heapq.heappush(self.m_heap, -duration)
            self.days_spend += duration

            if self.days_spend > last_day:
                longest = -heapq.heappop(self.m_heap)
                self.days_spend -= longest

        return len(self.m_heap)

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        scheduler = Scheduler(courses)
        return scheduler.scheduleCourse()

#solution = Solution()
#print(solution.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]])) # Output: 3
#print(solution.scheduleCourse([[1,2]])) # Output: 1 
#print(solution.scheduleCourse([[3,2],[4,3]])) #Output 0


