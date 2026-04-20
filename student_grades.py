import matplotlib.pyplot as plt


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None  # cache

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, score):
        result = []
        for i in range(len(self.scores)):
            if self.scores[i] == score:
                result.append(i)
        return result

    def get_sorted(self):
        scores = self.scores.copy()

        n = len(scores)
        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores

    def find_sorted(self, score):
        if self._sorted_scores is None:
            print("sorting…")
            self._sorted_scores = self.get_sorted()

        scores = self._sorted_scores
        left = 0
        right = len(scores) - 1

        while left <= right:
            mid = (left + right) // 2

            if scores[mid] == score:
                return mid
            elif scores[mid] < score:
                left = mid + 1
            else:
                right = mid - 1

        return None


    def average(self):
        return sum(self.scores) / len(self.scores)

    def best(self):
        return max(self.scores)

    def worst(self):
        return min(self.scores)

    def pass_rate(self):
        passed = 0
        for s in self.scores:
            if s >= 50:
                passed += 1
        return passed / len(self.scores)

    def __str__(self):
        return f"StudentsGrades: {self.count()} studentů, průměr {self.average():.1f}"


    def plot_histogram(self):
        plt.hist(self.scores, bins=range(0, 101, 10), edgecolor='black')

        plt.title("Histogram vysledkov studentov")
        plt.xlabel("Body")
        plt.ylabel("Pocet studentov")

        plt.show()



from sorting import random_numbers


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print("Pocet studentov:", results.count())
    print()

    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points – {results.get_grade(i)}")

    print()
    print("Indexy so 100 bodmi:", results.find(100))

    print("Zoradene vysledky:", results.get_sorted())
    print("Povodne data:", results.scores)

    print()
    print(results)

    print()
    print("Test cache:")
    print(results.find_sorted(91))
    print(results.find_sorted(50))
    print(results.find_sorted(77))

    print()

    random_results = StudentsGrades(random_numbers(30, 0, 100))

    print("Random count:", random_results.count())
    print("Random sorted:", random_results.get_sorted())

    random_results.plot_histogram()


if __name__ == "__main__":
    main()



