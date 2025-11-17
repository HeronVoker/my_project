def find_nearest_neighbour(numbers):
    n = len(numbers)
    if n == 1:
        return numbers[0]

    sorted_array = sorted(numbers)
    sorted_result = [0] * n

    sorted_result[0] = sorted_array[1]
    sorted_result[-1] = sorted_array[-2]

    for i in range(1, n - 1):
        if (
            sorted_array[i] - sorted_array[i - 1]
            <= sorted_array[i + 1] - sorted_array[i]
        ):
            sorted_result[i] = sorted_array[i - 1]
        else:
            sorted_result[i] = sorted_array[i + 1]

    sorted_dict = {
        number: nearest for number, nearest in zip(sorted_array, sorted_result)
    }
    print(" ".join(map(str, [sorted_dict[number] for number in numbers])))


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    find_nearest_neighbour(numbers)
