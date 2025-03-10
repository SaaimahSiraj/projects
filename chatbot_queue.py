class ChatbotQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self): 
        # Remove and return the first item from the queue
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self): 
        # Return the number of items in the queue
        return len(self.items)

    def peek(self): 
        # Return the first item without removing it
        if not self.is_empty():
            return self.items[0]
        return None

    def get_history(self):
        return self.items.copy()  # Return a copy of the current items in the queue
