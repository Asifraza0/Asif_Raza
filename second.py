def sort(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

user_input = input(" ")
input_array = list(map(int, user_input.split()))

sorted_array = sort(input_array)
print(sorted_array)
