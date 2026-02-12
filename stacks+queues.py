class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if self.isEmpty():
            return "stack empty"
        return self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        self.stack.append(element)
     
    def size(self, stack):
        return len(self.stack)

def reverse(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reverse_s = ""

    while not stack.isEmpty():
        reverse_s += stack.pop()

    return reverse_s

def isBalanced(string):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in string:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":      # closing bracket → check top
            if stack.isEmpty():  # nothing to match → unbalanced
                return False
            if stack.pop() != pairs[char]:
                return False

    return stack.isEmpty()
    
    
    
print(isBalanced("()")) 
print(reverse("hello"))