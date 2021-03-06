class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices ={}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1) # automatically bidirectional, undirected 
        else:
            raise IndexError("nonexistent vertex")

    def is_connected(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            return v2 in self.vertices[v1]
        else:
            raise IndexError("nonexistent vertex")
    
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    
    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Add starting vertex id
        q.enqueue(starting_vertex_id)
        # Create a set for visited verts
        visited = set()
        # While queue is not empty
        while q.size() > 0:
            # Dequeue a vert
            v = q.dequeue()
            # If not visited
            if v not in visited:
                # Visit it!
                print(v)
                # Mark as visited
                visited.add(v)
                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
    
    # breadth first search
    def bfs(self, starting_vertex_id, target_vertext_id):
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
                # CHECK IF IT'S THE TARGET
                    # IF SO, RETURN PATH
                # Mark it as visited...
                # Then add A PATH TO its neighbors to the back of the queue
                    # COPY THE PATH
                    # APPEND THE NEIGHBOR TO THE BACK
        pass


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)

g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(4,3)
g.add_edge(3,6)
g.add_edge(6,5)
g.add_edge(5,4)

print(g.vertices)
g.bft(1)
print("")
g.bft(3)

##########
# g.add_edge(1,2) # directed graph if just this direction
# g.add_edge(2,1) # undirected graph bc it goes back from 2 to 1 and above it's going 1 to 2