def bubble_sort(arr):
    n = len(arr)
    print('hello1')
    for i in range(n):
        #внутренний цикл для сравнения соседних элементов
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print('hello')
arr = [4, 1, 5, 6, 2, 3, 9]
print(bubble_sort(arr))
print(arr)