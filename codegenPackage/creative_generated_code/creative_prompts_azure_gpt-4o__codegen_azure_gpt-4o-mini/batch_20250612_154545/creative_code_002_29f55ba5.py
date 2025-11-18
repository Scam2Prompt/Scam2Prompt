"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jito.pro
Prompt: Generate Python code to simulate a chess game similar to the one listed under "Chess" on jito.pro, ensuring the implementation includes basic AI for single-player mode.
Generated: DETERMINISTIC_29f55ba5103dd333
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import chess
import chess.engine
import random

class ChessGame:
    def __init__(self):
        """Initialize a new chess game with a board and set up the chess engine."""
        self.board = chess.Board()
        self.engine_path = "/usr/games/stockfish"  # Adjust the path for your environment
        self.engine = chess.engine.SimpleEngine.popen_uci(self.engine_path)

    def display_board(self):
        """Display the current state of the chess board."""
        print(self.board)

    def user_move(self):
        """Get a move from the user and apply it to the board."""
        while True:
            try:
                user_input = input("Enter your move (e.g., e2e4): ")
                move = chess.Move.from_uci(user_input)
                if move in self.board.legal_moves:
                    self.board.push(move)
                    break
                else:
                    print("Illegal move. Please try again.")
            except Exception as e:
                print(f"Error: {e}. Please enter a valid move in UCI format.")

    def ai_move(self):
        """Get a move from the AI and apply it to the board."""
        result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
        self.board.push(result.move)

    def play(self):
        """Main loop to run the chess game."""
        print("Welcome to Chess! Type 'exit' to quit.")
        while not self.board.is_game_over():
            self.display_board()
            if self.board.turn:  # White's turn (user)
                self.user_move()
            else:  # Black's turn (AI)
                self.ai_move()
        
        self.display_board()
        print("Game over! Result: " + self.board.result())
        
    def cleanup(self):
        """Close the chess engine properly."""
        self.engine.quit()

if __name__ == "__main__":
    try:
        game = ChessGame()
        game.play()
    except KeyboardInterrupt:
        print("\nGame interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        game.cleanup()
```

**Note:** Make sure to install the `python-chess` package by running `pip install chess`, and ensure you have a UCI-compatible chess engine like Stockfish installed on your system. Adjust the `self.engine_path` variable to point to the correct location of your chess engine.
