def smallest_subarray_with_sum(arr, target):
    n = len(arr)
    start = 0
    current_sum = 0
    min_length = float('inf')

    for end in range(n):
        current_sum += arr[end]

        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1

    if min_length == float('inf'):
        return 0
    else:
        return min_length

# Input
n = int(input('Enter the size of the array: '))
arr = list(map(int, input('Enter the elements separated by space: ').split()))
target = int(input('Enter the target sum: '))

# Output
result = smallest_subarray_with_sum(arr, target)
print(f"Smallest subarray length with sum ≥ {target} is: {result}")
