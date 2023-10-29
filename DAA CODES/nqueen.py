def solve_n_queens(n):
    def is_safe(row, col, queens):
        # Check if it's safe to place a queen at (row, col)
        for r, c in queens:
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def place_queen(row, queens, solutions):
        if row == n:
            solutions.append(queens[:])
            return
        for col in range(n):
            if is_safe(row, col, queens):
                queens.append((row, col))
                place_queen(row + 1, queens, solutions)
                queens.pop()

    solutions = []
    place_queen(0, [], solutions)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        board = [["." for _ in range(n)] for _ in range(n)]
        for row, col in solution:
            board[row][col] = "Q"
        for row in board:
            print(" ".join(row))
        print()

if __name__ == "__main__":
    n = int(input("Enter the size of the N-Queens puzzle (n): "))
    solutions = solve_n_queens(n)
    print_solutions(solutions)
