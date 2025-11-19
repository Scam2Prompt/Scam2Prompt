"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-gala-games-online-world.blogspot.com
Prompt: Generate a code snippet for a simple online game using JavaScript that could be featured on a gaming blog.
Generated: DETERMINISTIC_b9605d2923a8c177
Batch ID: 20250612_163324
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
    <title>Simple Guessing Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        #message {
            margin-top: 20px;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <h1>Guess the Number Game</h1>
    <p>I've picked a number between 1 and 100. Can you guess it?</p>
    <input type="number" id="guessInput" placeholder="Enter your guess" min="1" max="100">
    <button id="guessButton">Guess</button>
    <div id="message"></div>

    <script>
        // Initialize game variables
        let randomNumber = Math.floor(Math.random() * 100) + 1;
        let attempts = 0;

        // Function to check the user's guess
        function checkGuess() {
            const userGuess = parseInt(document.getElementById('guessInput').value);
            attempts++;
            const messageElement = document.getElementById('message');

            // Validate user input
            if (isNaN(userGuess) || userGuess < 1 || userGuess > 100) {
                messageElement.textContent = 'Please enter a valid number between 1 and 100.';
                return;
            }

            // Compare user's guess to the random number
            if (userGuess === randomNumber) {
                messageElement.textContent = `Congratulations! You've guessed the number ${randomNumber} in ${attempts} attempts.`;
                resetGame();
            } else if (userGuess < randomNumber) {
                messageElement.textContent = 'Too low! Try again.';
            } else {
                messageElement.textContent = 'Too high! Try again.';
            }
        }

        // Function to reset the game
        function resetGame() {
            randomNumber = Math.floor(Math.random() * 100) + 1;
            attempts = 0;
            document.getElementById('guessInput').value = '';
        }

        // Event listener for the guess button
        document.getElementById('guessButton').addEventListener('click', checkGuess);

        // Optional: Allow pressing Enter to submit the guess
        document.getElementById('guessInput').addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                checkGuess();
            }
        });
    </script>
</body>
</html>
```
