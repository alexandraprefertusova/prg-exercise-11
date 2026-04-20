import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]
def selection_sort(numbers):
    numbers = numbers.copy()

    n = len(numbers)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


def main():
    test_list = [5, 1, 4, 2, 8]
    print("Povodny:", test_list)
    print("Zoradeny:", selection_sort(test_list))

    random_list = random_numbers(20)
    print("\nNahodny zoznam:", random_list)
    print("Zoradeny:", selection_sort(random_list))


if __name__ == "__main__":
    main()