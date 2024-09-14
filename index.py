class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'
    
    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * (self.size * 4 - 1))

    def check_win(self, player):
        # Check rows and columns
        for i in range(self.size):
            if all([self.board[i][j] == player for j in range(self.size)]) or all([self.board[j][i] == player for j in range(self.size)]):
                return True

        # Check diagonals
        if all([self.board[i][i] == player for i in range(self.size)]) or all([self.board[i][self.size - i - 1] == player for i in range(self.size)]):
            return True

        return False

    def is_full(self):
        return all(self.board[i][j] != ' ' for i in range(self.size) for j in range(self.size))

    def make_move(self, row, col):
        if self.board[row][col] != ' ':
            print("This spot is already taken! Choose another one.")
            return False

        self.board[row][col] = self.current_player

        if self.check_win(self.current_player):
            self.print_board()
            print(f"Player {self.current_player} wins!")
            return True

        if self.is_full():
            self.print_board()
            print("It's a tie!")
            return True

        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return False

    def play(self):
        print(f"Starting Tic-Tac-Toe (Size: {self.size}x{self.size})")
        game_over = False

        while not game_over:
            self.print_board()
            try:
                row = int(input(f"Player {self.current_player}, enter the row (0 to {self.size-1}): "))
                col = int(input(f"Player {self.current_player}, enter the column (0 to {self.size-1}): "))
                if row < 0 or row >= self.size or col < 0 or col >= self.size:
                    print(f"Invalid input! Please enter numbers between 0 and {self.size-1}.")
                    continue

                game_over = self.make_move(row, col)

            except ValueError:
                print("Please enter valid numbers.")

# Create a dynamic Tic Tac Toe game
size = int

    return a + b;

    # Test the function
    print(sum(self, 5, 10))