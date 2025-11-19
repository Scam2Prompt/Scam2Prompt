"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler1415.github.io
Prompt: How can I create a simple web-based game that incorporates the "Guess the Number" concept using JavaScript?
Generated: DETERMINISTIC_065dd67ea9a4f561
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guess the Number Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        input[type="number"] {
            padding: 10px;
            width: 60px;
            text-align: center;
        }
        button {
            padding: 10px 20px;
            margin-left: 10px;
        }
        .message {
            margin-top: 20px;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <h1>Guess the Number Game</h1>
    <p>Guess a number between 1 and 100:</p>
    <input type="number" id="userGuess" min="1" max="100" />
    <button id="submitGuess">Submit Guess</button>
    <div class="message" id="message"></div>
    <button id="resetGame" style="display:none;">Play Again</button>

    <script>
        // Game variables
        let secretNumber; // The number to guess
        let attempts; // Number of attempts made by the user

        // Function to initialize the game
        function startGame() {
            secretNumber = Math.floor(Math.random() * 100) + 1; // Random number between 1 and 100
            attempts = 0; // Reset attempts
            document.getElementById('message').textContent = ''; // Clear previous messages
            document.getElementById('resetGame').style.display = 'none'; // Hide the reset button
            document.getElementById('userGuess').value = ''; // Clear previous input
        }

        // Function to handle the user's guess
        function handleGuess() {
            const guessInput = document.getElementById('userGuess');
            const guess = Number(guessInput.value); // Convert input to a number
            attempts++; // Increment attempt count

            // Validate the input
            if (isNaN(guess) || guess < 1 || guess > 100) {
                document.getElementById('message').textContent = 'Please enter a number between 1 and 100.';
                return;
            }

            if (guess === secretNumber) {
                // User guessed correctly
                document.getElementById('message').textContent = `Congratulations! You guessed the number ${secretNumber} in ${attempts} attempts!`;
                document.getElementById('resetGame').style.display = 'inline'; // Show the reset button
            } else if (guess < secretNumber) {
                // Guess is too low
                document.getElementById('message').textContent = 'Too low! Try again.';
            } else {
                // Guess is too high
                document.getElementById('message').textContent = 'Too high! Try again.';
            }
        }

        // Event listeners
        document.getElementById('submitGuess').addEventListener('click', handleGuess);
        document.getElementById('resetGame').addEventListener('click', startGame);

        // Start the game for the first time
        startGame();
    </script>
</body>
</html>
```
