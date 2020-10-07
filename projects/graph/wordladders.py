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


# Read words in from the file, add to set of words

word_set = set()

with open("words.txt") as f:
    for word in f: # For each line of the file
        word_set.add(word.strip().lower()) # strip off the white sprace and make it lowercased

import string

def get_neighbors(word):
    neighbors = []
    word_letters = list(word)

    for i in range(len(word_letters)):
        for letter in list(string.ascii_lowercase): # ["a", "b", "c"..."z"]
            # Make a copy of the word
            temp_word = list(word_letters)
            # Substitute the letter into the word copy
            temp_word[i] = letter
            # Make it string
            temp_word_str = "".join(temp_word)
            # IF it's a real word, add it to the return set
            if temp_word_str != word and temp_word_str in word_set:
                neighbors.append(temp_word_str)

    return neighbors

def find_word_ladder(begin_word, end_word): # BFS across the graph
    visted = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visted:
            visted.add(v)

            if v == end_word:
                return path
            
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
        # IF we get here, didnt find it
        return None 


