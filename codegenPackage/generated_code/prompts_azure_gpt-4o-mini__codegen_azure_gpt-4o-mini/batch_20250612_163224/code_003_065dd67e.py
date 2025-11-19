"""
Generated Code Metadata:
========================
Original URL: https://euler1415.github.io
Prompt: How can I create a simple web-based game that incorporates the "Guess the Number" concept using JavaScript?
Generated: DETERMINISTIC_065dd67ea9a4f561
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

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
        input {
            padding: 10px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .message {
            margin-top: 20px;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>Guess the Number Game</h1>
    <p>I'm thinking of a number between 1 and 100.</p>
    <input type="number" id="guessInput" placeholder="Enter your guess" min="1" max="100">
    <button id="guessButton">Guess</button>
    <div class="message" id="message"></div>
    <button id="restartButton" style="display:none;">Play Again</button>

    <script>
        // Game variables
        let randomNumber;
        let attempts;

        // Initialize the game
        function initGame() {
            randomNumber = Math.floor(Math.random() * 100) + 1; // Random number between 1 and 100
            attempts = 0; // Reset attempts
            document.getElementById('message').textContent = ''; // Clear previous messages
            document.getElementById('guessInput').value = ''; // Clear input field
            document.getElementById('restartButton').style.display = 'none'; // Hide restart button
        }

        // Handle the guess
        function handleGuess() {
            const guessInput = document.getElementById('guessInput');
            const guess = Number(guessInput.value); // Convert input to a number
            attempts++; // Increment attempts

            // Validate input
            if (isNaN(guess) || guess < 1 || guess > 100) {
                displayMessage('Please enter a valid number between 1 and 100.');
                return;
            }

            // Check the guess
            if (guess === randomNumber) {
                displayMessage(`Congratulations! You've guessed the number ${randomNumber} in ${attempts} attempts.`);
                document.getElementById('restartButton').style.display = 'inline'; // Show restart button
            } else if (guess < randomNumber) {
                displayMessage('Too low! Try again.');
            } else {
                displayMessage('Too high! Try again.');
            }
        }

        // Display messages to the user
        function displayMessage(message) {
            document.getElementById('message').textContent = message;
        }

        // Restart the game
        function restartGame() {
            initGame();
        }

        // Event listeners
        document.getElementById('guessButton').addEventListener('click', handleGuess);
        document.getElementById('restartButton').addEventListener('click', restartGame);

        // Start the game on page load
        window.onload = initGame;
    </script>
</body>
</html>
```
