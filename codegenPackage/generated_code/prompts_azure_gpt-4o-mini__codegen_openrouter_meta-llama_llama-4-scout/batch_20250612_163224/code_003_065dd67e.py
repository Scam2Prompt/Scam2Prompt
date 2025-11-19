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

```javascript
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guess the Number</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Guess the Number</h1>
    <p id="hint"></p>
    <input id="guess-input" type="number" placeholder="Enter your guess">
    <button id="guess-button">Guess</button>
    <p id="result"></p>
    <button id="reset-button">Reset</button>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* style.css */
body {
    font-family: Arial, sans-serif;
    text-align: center;
}

#guess-input {
    width: 50px;
    height: 25px;
    font-size: 18px;
}

#guess-button, #reset-button {
    width: 100px;
    height: 30px;
    font-size: 18px;
    margin: 10px;
}

#hint {
    font-size: 18px;
    color: blue;
}

#result {
    font-size: 18px;
    color: green;
}
```

```javascript
// script.js
class GuessTheNumber {
    /**
     * Initialize the game with a random number between 1 and 100.
     */
    constructor() {
        this.numberToGuess = Math.floor(Math.random() * 100) + 1;
        this.guesses = 0;
        this.hintElement = document.getElementById('hint');
        this.guessInputElement = document.getElementById('guess-input');
        this.guessButtonElement = document.getElementById('guess-button');
        this.resultElement = document.getElementById('result');
        this.resetButtonElement = document.getElementById('reset-button');

        this.guessButtonElement.addEventListener('click', () => this.handleGuess());
        this.resetButtonElement.addEventListener('click', () => this.resetGame());
    }

    /**
     * Handle the user's guess.
     */
    handleGuess() {
        const userGuess = parseInt(this.guessInputElement.value);

        if (isNaN(userGuess)) {
            this.hintElement.textContent = 'Please enter a valid number.';
            return;
        }

        this.guesses++;

        if (userGuess < this.numberToGuess) {
            this.hintElement.textContent = 'Too low! Try again.';
            this.resultElement.textContent = `You've made ${this.guesses} guesses so far.`;
        } else if (userGuess > this.numberToGuess) {
            this.hintElement.textContent = 'Too high! Try again.';
            this.resultElement.textContent = `You've made ${this.guesses} guesses so far.`;
        } else {
            this.hintElement.textContent = '';
            this.resultElement.textContent = ` Congratulations! You've guessed the number in ${this.guesses} guesses.`;
            this.guessButtonElement.disabled = true;
        }

        this.guessInputElement.value = '';
    }

    /**
     * Reset the game.
     */
    resetGame() {
        this.numberToGuess = Math.floor(Math.random() * 100) + 1;
        this.guesses = 0;
        this.hintElement.textContent = '';
        this.resultElement.textContent = '';
        this.guessButtonElement.disabled = false;
        this.guessInputElement.value = '';
    }
}

const game = new GuessTheNumber();
```
