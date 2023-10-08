class Stack:
    
    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
    
    def isEmpty(self):
        return len(self.items) == 0
    
    # adding an item to the top of the stack
    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise OverflowError("Stack is full")
        
    # removing an item from the top of the stack
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    
    # getting the top item without removing it
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit
    
    # returning the index of the first occurrence of the target element in the stack
    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return i
        return -1
