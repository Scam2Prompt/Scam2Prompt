"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write JavaScript code for a game that teaches basic addition and subtraction, inspired by the mathematics games on "Portal de Saltinho."
Generated: DETERMINISTIC_4566ef35e5193b28
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Basic Math Game: Addition and Subtraction
// This game helps users practice basic addition and subtraction through a simple interactive interface.

class MathGame {
    constructor() {
        this.score = 0; // Player's score
        this.currentQuestion = null; // Current question object
        this.init(); // Initialize the game
    }

    // Initialize the game
    init() {
        this.updateScore();
        this.generateQuestion();
        this.setupEventListeners();
    }

    // Generate a random math question
    generateQuestion() {
        const num1 = this.getRandomInt(1, 20);
        const num2 = this.getRandomInt(1, 20);
        const operation = this.getRandomOperation();

        this.currentQuestion = {
            num1,
            num2,
            operation,
            answer: this.calculateAnswer(num1, num2, operation)
        };

        this.displayQuestion();
    }

    // Calculate the answer based on the operation
    calculateAnswer(num1, num2, operation) {
        switch (operation) {
            case '+':
                return num1 + num2;
            case '-':
                return num1 - num2;
            default:
                throw new Error('Invalid operation');
        }
    }

    // Get a random integer between min and max
    getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    // Get a random operation
    getRandomOperation() {
        return Math.random() < 0.5 ? '+' : '-';
    }

    // Display the current question to the user
    displayQuestion() {
        const questionElement = document.getElementById('question');
        questionElement.textContent = `What is ${this.currentQuestion.num1} ${this.currentQuestion.operation} ${this.currentQuestion.num2}?`;
    }

    // Update the score display
    updateScore() {
        const scoreElement = document.getElementById('score');
        scoreElement.textContent = `Score: ${this.score}`;
    }

    // Setup event listeners for user input
    setupEventListeners() {
        const submitButton = document.getElementById('submit');
        submitButton.addEventListener('click', () => this.checkAnswer());
    }

    // Check the user's answer
    checkAnswer() {
        const userAnswer = parseInt(document.getElementById('answer').value, 10);
        if (isNaN(userAnswer)) {
            alert('Please enter a valid number.');
            return;
        }

        if (userAnswer === this.currentQuestion.answer) {
            this.score++;
            alert('Correct! Well done!');
        } else {
            alert(`Incorrect! The correct answer was ${this.currentQuestion.answer}.`);
        }

        this.updateScore();
        this.generateQuestion(); // Generate a new question
    }
}

// Start the game when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    new MathGame();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Math Game</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        #question { font-size: 24px; margin: 20px; }
        #score { font-size: 20px; }
    </style>
</head>
<body>
    <h1>Basic Math Game</h1>
    <div id="score">Score: 0</div>
    <div id="question">What is ?</div>
    <input type="number" id="answer" placeholder="Your answer" />
    <button id="submit">Submit</button>

    <script src="math-game.js"></script>
</body>
</html>
```
