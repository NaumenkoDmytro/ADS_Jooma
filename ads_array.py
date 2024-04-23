class Array:
    def __init__(self):
        self.data = []
        self.length = 0

    def __str__(self):
        return str(self.data)

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def push(self, item):
        self.data.append(item)
        self.length += 1

    def insert(self, index, item):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        self.data.insert(index, item)
        self.length += 1

    def delete(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        self.data.pop(index)
        self.length -= 1

    def insert_at_front(self, item):
        self.insert(0, item)  # Insert the item at the index 0

# Creating an instance of Array
arr = Array()

# Adding elements normally
arr.push(10)
arr.push(20)
arr.push(30)
print("After pushing elements:", arr)

# Inserting element at the front
arr.insert_at_front(5)
print("After inserting at front:", arr)

# Inserting another element at the front
arr.insert_at_front([2,3,4,5,6,7,89])
print("After inserting another at front:", arr)