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

Here's a clean, production-ready implementation of a "Guess the Number" web game using HTML, CSS, and JavaScript:

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
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
            background-color: #f5f5f5;
        }
        .game-container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
        }
        .input-group {
            margin: 20px 0;
        }
        input[type="number"] {
            padding: 10px;
            width: 100px;
            font-size: 18px;
            border: 2px solid #3498db;
            border-radius: 5px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        #message {
            margin: 20px 0;
            font-size: 18px;
            min-height: 24px;
        }
        #attempts {
            font-weight: bold;
            color: #e74c3c;
        }
        .restart-btn {
            display: none;
            background-color: #2ecc71;
        }
        .restart-btn:hover {
            background-color: #27ae60;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>Guess the Number Game</h1>
        <p>I'm thinking of a number between 1 and 100. Can you guess it?</p>
        
        <div class="input-group">
            <input type="number" id="guessInput" min="1" max="100" placeholder="Enter your guess">
            <button id="guessBtn">Submit Guess</button>
            <button id="restartBtn" class="restart-btn">Play Again</button>
        </div>
        
        <div id="message"></div>
        <p>Attempts remaining: <span id="attempts">10</span></p>
    </div>

    <script>
        // Game state variables
        let targetNumber;
        let remainingAttempts;
        const maxAttempts = 10;
        const minNumber = 1;
        const maxNumber = 100;

        // DOM elements
        const guessInput = document.getElementById('guessInput');
        const guessBtn = document.getElementById('guessBtn');
        const restartBtn = document.getElementById('restartBtn');
        const messageEl = document.getElementById('message');
        const attemptsEl = document.getElementById('attempts');

        /**
         * Initializes a new game
         */
        function initGame() {
            targetNumber = Math.floor(Math.random() * maxNumber) + minNumber;
            remainingAttempts = maxAttempts;
            attemptsEl.textContent = remainingAttempts;
            messageEl.textContent = '';
            guessInput.value = '';
            guessInput.disabled = false;
            guessBtn.style.display = 'inline-block';
            restartBtn.style.display = 'none';
            guessInput.focus();
        }

        /**
         * Handles the guess submission
         */
        function handleGuess() {
            const userGuess = parseInt(guessInput.value);
            
            // Validate input
            if (isNaN(userGuess) || userGuess < minNumber || userGuess > maxNumber) {
                messageEl.textContent = `Please enter a valid number between ${minNumber} and ${maxNumber}.`;
                messageEl.style.color = '#e74c3c';
                return;
            }

            remainingAttempts--;
            attemptsEl.textContent = remainingAttempts;

            // Check guess against target number
            if (userGuess === targetNumber) {
                endGame(true);
            } else if (remainingAttempts === 0) {
                endGame(false);
            } else {
                giveHint(userGuess);
            }
        }

        /**
         * Provides hint to the player based on their guess
         * @param {number} guess - The player's guess
         */
        function giveHint(guess) {
            if (guess < targetNumber) {
                messageEl.textContent = 'Too low! Try a higher number.';
                messageEl.style.color = '#3498db';
            } else {
                messageEl.textContent = 'Too high! Try a lower number.';
                messageEl.style.color = '#3498db';
            }
            guessInput.value = '';
            guessInput.focus();
        }

        /**
         * Ends the game and displays the result
         * @param {boolean} isWin - Whether the player won
         */
        function endGame(isWin) {
            guessInput.disabled = true;
            guessBtn.style.display = 'none';
            restartBtn.style.display = 'inline-block';

            if (isWin) {
                messageEl.textContent = `Congratulations! You guessed the number ${targetNumber} correctly!`;
                messageEl.style.color = '#2ecc71';
            } else {
                messageEl.textContent = `Game over! The number was ${targetNumber}. Better luck next time!`;
                messageEl.style.color = '#e74c3c';
            }
        }

        // Event listeners
        guessBtn.addEventListener('click', handleGuess);
        restartBtn.addEventListener('click', initGame);
        guessInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                handleGuess();
            }
        });

        // Initialize the game on page load
        document.addEventListener('DOMContentLoaded', initGame);
    </script>
</body>
</html>
```
