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
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    h1 {
      margin-top: 20px;
      color: #333;
    }
    .container {
      margin: 20px auto;
      padding: 20px;
      max-width: 400px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    input[type="number"], button {
      padding: 10px;
      margin: 10px 0;
      width: 100%;
      font-size: 16px;
    }
    .result {
      margin-top: 20px;
      font-size: 18px;
      color: #555;
    }
  </style>
</head>
<body>
  <h1>Guess the Number</h1>
  <div class="container">
    <p>Guess a number between 1 and 100:</p>
    <input type="number" id="guessInput" placeholder="Enter your guess" min="1" max="100">
    <button id="submitGuess">Submit Guess</button>
    <button id="restartGame">Restart Game</button>
    <div class="result" id="resultMessage"></div>
  </div>

  <script>
    // Initialize game variables
    let randomNumber = Math.floor(Math.random() * 100) + 1; // Generate a random number between 1 and 100
    let attempts = 0; // Track the number of attempts

    // Get references to DOM elements
    const guessInput = document.getElementById('guessInput');
    const submitGuessButton = document.getElementById('submitGuess');
    const restartGameButton = document.getElementById('restartGame');
    const resultMessage = document.getElementById('resultMessage');

    // Function to handle guess submission
    const handleGuess = () => {
      const userGuess = parseInt(guessInput.value, 10); // Parse user input as a number
      
      // Validate input
      if (isNaN(userGuess) || userGuess < 1 || userGuess > 100) {
        resultMessage.textContent = 'Please enter a valid number between 1 and 100.';
        return;
      }

      // Increment attempts
      attempts++;

      // Compare user guess with the random number
      if (userGuess === randomNumber) {
        resultMessage.textContent = `Congratulations! You've guessed the number ${randomNumber} in ${attempts} attempts.`;
        submitGuessButton.disabled = true; // Disable further guesses
      } else if (userGuess < randomNumber) {
        resultMessage.textContent = 'Too low! Try again.';
      } else {
        resultMessage.textContent = 'Too high! Try again.';
      }
    };

    // Function to restart the game
    const restartGame = () => {
      randomNumber = Math.floor(Math.random() * 100) + 1; // Regenerate random number
      attempts = 0; // Reset attempts
      guessInput.value = ''; // Clear input
      resultMessage.textContent = ''; // Clear result message
      submitGuessButton.disabled = false; // Enable guess submission
    };

    // Attach event listeners
    submitGuessButton.addEventListener('click', handleGuess);
    restartGameButton.addEventListener('click', restartGame);
  </script>
</body>
</html>
```
