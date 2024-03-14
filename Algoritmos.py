def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    start_index = 0
    end_index = 0
    temp_start_index = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start_index = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i

    return arr[start_index:end_index+1]

arr = [-2, 1, 3, 4, -1, 2, 1, -5, 4]
print("Maximum sub-array:", max_subarray(arr))
