import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs) -> None:
        self.contents = []
        for key,value in kwargs.items():
            i = 0
            while i < value:
                self.contents.append(key)
                i += 1
    
    def draw(self, n: int) -> list:
        if n > len(self.contents):
            return self.contents
        string = []
        i = 0
        while i < n:
            popIndex = random.randint(0,len(self.contents)-1)
            popped = self.contents[popIndex]
            string.append(popped)
            self.contents.pop(popIndex)
            i += 1
        return string


def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> float:
    M = 0
    for i in range(num_experiments):
        original = copy.deepcopy(hat)
        excpected = copy.deepcopy(expected_balls)
        obtained = original.draw(num_balls_drawn)

        for ball in obtained:
            if ball in excpected:
                excpected[ball] -= 1
        
        if all(count <= 0 for count in excpected.values()):
            M += 1
    
    return M/num_experiments