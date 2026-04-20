import random


def random_numbers(count):
    return [random.randint(0, 100) for _ in range(count)]


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


def bubble_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


def main():
    test_list = [5, 1, 4, 2, 8]

    print("povodny:", test_list)
    print("Selection Sort:", selection_sort(test_list))
    print("Bubble Sort:", bubble_sort(test_list))

    random_list = random_numbers(20)
    print("\nnahodny zoznam:", random_list)
    print("Selection Sort:", selection_sort(random_list))
    print("Bubble Sort:", bubble_sort(random_list))


if __name__ == "__main__":
    main()