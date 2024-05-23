# In this example, the NumberIterator provides a simple way to access each element in the list sequentially without needing to know anything about the list's structure or how it is stored. 
# This encapsulation makes the code more flexible and easier to use.


class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def has_next(self):
        return self.index < len(self.numbers)

    def next(self):
        if self.has_next():
            number = self.numbers[self.index]
            self.index += 1
            return number
        else:
            raise StopIteration("No more elements")

# Client code
numbers = [1, 2, 3, 4, 5]
iterator = NumberIterator(numbers)

while iterator.has_next():
    print(iterator.next())


# Explanation:
# NumberIterator Class: This class takes a list of numbers and helps you iterate through them.

# __init__: Initializes the iterator with the list and starts at the first element.
# has_next: Checks if there are more elements to iterate over.
# next: Returns the next element and moves the iterator to the following element.
# Client Code:

# Creates a list of numbers.
# Initializes an iterator for the list.
# Uses a while loop to go through the list and print each number.
