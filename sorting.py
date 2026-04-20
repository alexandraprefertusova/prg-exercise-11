import random
import matplotlib.pyplot as plt


def random_numbers(count):
    return [random.randint(0, 100) for _ in range(count)]


def selection_sort(numbers, visualize=False):
    numbers = numbers.copy()
    n = len(numbers)

    if visualize:
        plt.ion()
        plt.show()

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

            if visualize:
                colors = ["steelblue"] * len(numbers)

                colors[i] = "orange"

                colors[j] = "tomato"

                colors[min_index] = "green"

                plt.clf()
                plt.bar(range(len(numbers)), numbers, color=colors)
                plt.title("Selection Sort")
                plt.pause(0.1)

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    if visualize:
        plt.ioff()
        plt.show()

    return numbers


def bubble_sort(numbers, visualize=False):
    numbers = numbers.copy()
    n = len(numbers)

    if visualize:
        plt.ion()
        plt.show()

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

            if visualize:
                colors = ["steelblue"] * len(numbers)
                colors[j] = "tomato"
                colors[j + 1] = "tomato"

                plt.clf()
                plt.bar(range(len(numbers)), numbers, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)

        if not swapped:
            break

    if visualize:
        plt.ioff()
        plt.show()

    return numbers


def main():
    test_list = random_numbers(15)

    print("Původní:", test_list)

    print("\nSelection Sort (vizualizace)")
    selection_sort(test_list, visualize=True)

    print("\nBubble Sort (vizualizace)")
    bubble_sort(test_list, visualize=True)


if __name__ == "__main__":
    main()