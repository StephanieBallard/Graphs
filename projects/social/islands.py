# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An island consists of 1s that are connected to the north, south, east or west.

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

def island_counter(islands):
    # Create a way to keep track of visited nodes
    visited = []
    for _ in range(len(islands)):
        new_row = [False] * len(islands[0])
        visited.append(new_row)

        print(visited)

        island_count = 0
    # Walk through each cell in the grid
    
    for row in range(len(islands)):
        for col in range(len(islands[0])):
            
    # If it's not visited
        # If it's a 1:
            # Do a traversal
            # increment the counter

    island_counter(islands) # returns 4