import random
import math

# Function to evaluate the board (number of conflicts)
def evaluate_board(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Check for conflicts: same row or same diagonal
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

# Function to generate a random board (initial solution)
def generate_random_board(n):
    return [random.randint(0, n-1) for _ in range(n)]

# Function to generate a neighbor by moving a queen to a random row in its column
def generate_neighbor(board):
    neighbor = board[:]
    col = random.randint(0, len(board) - 1)  # Pick a random column
    row = random.randint(0, len(board) - 1)  # Pick a random row for the queen
    neighbor[col] = row  # Move the queen to the new row in its column
    return neighbor

# Simulated Annealing Algorithm to solve N-Queens problem
def simulated_annealing(n, initial_temperature=1000, cooling_rate=0.99, max_iterations=1000):
    # Step 1: Generate an initial board (start state)
    current_board = generate_random_board(n)
    current_conflicts = evaluate_board(current_board)

    # Step 2: Set the temperature and initialize the best solution
    temperature = initial_temperature
    best_board = current_board
    best_conflicts = current_conflicts

    print("Initial Board State:")
    print_solution(current_board)
    print(f"Initial conflicts: {current_conflicts}\n")

    # Step 3: Run the simulated annealing process
    for iteration in range(max_iterations):
        # Step 3.1: Generate a neighbor of the current board
        neighbor = generate_neighbor(current_board)
        neighbor_conflicts = evaluate_board(neighbor)

        # Step 3.2: Calculate the change in conflicts (energy difference)
        delta_conflicts = current_conflicts - neighbor_conflicts

        # Step 3.3: If the neighbor is better, accept it
        if delta_conflicts > 0:
            current_board = neighbor
            current_conflicts = neighbor_conflicts
        else:
            # Step 3.4: If the neighbor is worse, accept it with a probability
            probability = math.exp(delta_conflicts / temperature)
            if random.random() < probability:
                current_board = neighbor
                current_conflicts = neighbor_conflicts

        # Step 3.5: Update the best solution found so far
        if current_conflicts < best_conflicts:
            best_board = current_board
            best_conflicts = current_conflicts

        # Step 3.6: Cool down the temperature
        temperature *= cooling_rate

        # Step 3.7: If no conflicts, return the solution (goal state)
        if current_conflicts == 0:
            print(f"Solution found at iteration {iteration + 1}!")
            print_solution(current_board)
            print(f"Total conflicts: {current_conflicts}\n")
            return current_board

        # Print the board and the number of conflicts at each iteration for tracking
        if iteration % 100 == 0:  # Print the board at every 100th iteration
            print(f"Iteration {iteration + 1}:")
            print_solution(current_board)
            print(f"Conflicts: {current_conflicts}\n")

    # Step 4: If a solution is not found, return the best board found
    print(f"No solution found after {max_iterations} iterations.")
    print_solution(best_board)
    print(f"Best conflicts: {best_conflicts}")
    return best_board

# Function to print the board in a user-friendly format
def print_solution(board):
    n = len(board)
    for row in range(n):
        row_str = ['Q' if col == board[row] else '.' for col in range(n)]
        print(' '.join(row_str))

# Main function to solve the N-Queens problem using Simulated Annealing
if __name__ == "__main__":
    n = int(input("Enter the number of queens (n): "))  # User input for n
    solution = simulated_annealing(n)

    if solution:
        print("\nSolution found:")
        print_solution(solution)
    else:
        print("No solution found.")
