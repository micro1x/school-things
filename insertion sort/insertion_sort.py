file = open("numbers.txt", "r")
lst = []
for line in file:
  lst.append(int(line.strip()))
def insertion_sort(numbers):
  for i in range(1,len(numbers)):
    j = i
    while j > 0 and numbers[j] < numbers[j-1]:
      numbers[j], numbers[j-1] = numbers[j-1],numbers[j]
  return numbers
print(insertion_sort(lst))
