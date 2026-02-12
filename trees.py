class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = Node(data)

#     def display(self):
#         if self.root:
#             lines, *_ = self._display_aux(self.root)
#             for line in lines:
#                 print(line)
#         else:
#             print("Tree is empty")

#     def _display_aux(self, node):
#         """Helper function that returns list of strings for printing tree"""
#         if node.right is None and node.left is None:
#             line = str(node.data)
#             width = len(line)
#             height = 1
#             middle = width // 2
#             return [line], width, height, middle

#         if node.right is None:
#             lines, n, p, x = self._display_aux(node.left)
#             s = str(node.data)
#             u = len(s)
#             first_line = (x + 1) * " " + (n - x - 1) * "_" + s
#             second_line = x * " " + "/" + (n - x - 1 + u) * " "
#             shifted_lines = [line + u * " " for line in lines]
#             return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

#         if node.left is None:
#             lines, n, p, x = self._display_aux(node.right)
#             s = str(node.data)
#             u = len(s)
#             first_line = s + x * "_" + (n - x) * " "
#             second_line = (u + x) * " " + "\\"
#             shifted_lines = [u * " " + line for line in lines]
#             return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

#         left, n, p, x = self._display_aux(node.left)
#         right, m, q, y = self._display_aux(node.right)
#         s = str(node.data)
#         u = len(s)
#         first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
#         second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\"
#         if p < q:
#             left += [" " * n] * (q - p)
#         elif q < p:
#             right += [" " * m] * (p - q)
#         zipped_lines = zip(left, right)
#         lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
#         return lines, n + m + u, max(p, q) + 2, n + u // 2

bst = BST()
for things in [20, 10, 30, 5, 15, 25, 35]:
    bst.insert(things)
