line1 = [[5, 3, 7, 0], [2, 4, 6, 9], [1, 3, 6, 8]]
line2 = [[1, 2, 3, 6], [4, 5, 6, 7], [1, 1, 1, 1]]

class Matrix():
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return "\n".join(map(str, self.lists))

    def __add__(self, other):
        a = []
        for i in range(len(self.lists)):
            a.append([])
            for j in range((len(self.lists[0]))):
                a[i].append(self.lists[i][j] + other.lists[i][j])
                return "\n".join(map(str, a))

matrix1 = Matrix(line1)
matrix2 = Matrix(line2)
print(f"Matrix 1\n{matrix1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix2}\n{'-' * 20}")
print(f"matrix 1 + matrix 2:\n{matrix1 + matrix2}")
