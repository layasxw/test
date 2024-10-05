1)
Тебе нужно узнать размер первой коробки с игрушками из списка коробок. У тебя есть 100 коробок, но интересует только первая. Сколько шагов тебе нужно сделать?
Ответ: константное время, О(1)

def get_first_element(arr):
  return arr[0]
Ответ: константное время, О(1)

2)
def find_max(arr):
  max_value = arr[0]
  for i in arr:
    if i > max_value:
      max_value = i
  return max_value
Ответ: линейное время, О(n)

3)
def print_all_pairs(arr):
  for i in arr:
    for j in arr:
      print(i, j)
Ответ: медленный алгоритм, О(n^2)

4)
def sum_of_triplets(arr):
  total_sum = 0
  for i in arr:
    for j in arr:
      for k in arr:
        total_sum += i + j + k
  return total_sum
Ответ: ?? О(n!)

5)
def binary_search(arr, target):
  low = 0
  high = len(arr) - 1       
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1
Ответ: логарифмическое время, О(log n)
