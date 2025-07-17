def selection_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Sorted array in ascending order:", arr)


def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    print("Sorted array in descending order:", arr)


# --- INPUT & DRIVER CODE ---
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
choice = input("Enter your choice (1 for ascending, 2 for descending): ")

if choice == '1':
    selection_sort_ascending(arr)
elif choice == '2':
    selection_sort_descending(arr)
else:
    print("Invalid choice entered.")
