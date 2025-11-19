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
// mathGame.js

/**
 * Math Game: Basic Addition and Subtraction
 * Inspired by Portal de Saltinho
 */

// Game class
class MathGame {
  /**
   * Constructor
   * @param {Object} options - Game options
   * @param {Number} options.difficulty - Difficulty level (1-3)
   * @param {Number} options.timeLimit - Time limit in seconds
   */
  constructor(options) {
    this.difficulty = options.difficulty || 1;
    this.timeLimit = options.timeLimit || 60; // default 1 minute
    this.score = 0;
    this.questionsAnswered = 0;
    this.currentQuestion = null;
    this.gameInterval = null;
  }

  /**
   * Start the game
   */
  startGame() {
    console.log("Game started!");
    this.generateQuestion();
    this.gameInterval = setInterval(() => {
      this.updateTimer();
    }, 1000); // update timer every second
  }

  /**
   * Generate a random math question based on difficulty level
   */
  generateQuestion() {
    const operators = [
      { op: "+", func: (a, b) => a + b },
      { op: "-", func: (a, b) => a - b },
    ];

    const operator = operators[Math.floor(Math.random() * operators.length)];
    let num1, num2;

    switch (this.difficulty) {
      case 1:
        num1 = Math.floor(Math.random() * 10) + 1;
        num2 = Math.floor(Math.random() * 10) + 1;
        break;
      case 2:
        num1 = Math.floor(Math.random() * 50) + 1;
        num2 = Math.floor(Math.random() * 50) + 1;
        break;
      case 3:
        num1 = Math.floor(Math.random() * 100) + 1;
        num2 = Math.floor(Math.random() * 100) + 1;
        break;
      default:
        throw new Error("Invalid difficulty level");
    }

    this.currentQuestion = {
      num1,
      num2,
      operator: operator.op,
      correctAnswer: operator.func(num1, num2),
    };

    console.log(`What is ${num1} ${operator.op} ${num2}?`);
  }

  /**
   * Update the timer
   */
  updateTimer() {
    this.timeLimit -= 1;
    console.log(`Time remaining: ${this.timeLimit} seconds`);

    if (this.timeLimit === 0) {
      this.gameOver();
    }
  }

  /**
   * Game over logic
   */
  gameOver() {
    clearInterval(this.gameInterval);
    console.log(`Game over! Your score is ${this.score} / ${this.questionsAnswered}`);
    this.timeLimit = 60; // reset time limit
  }

  /**
   * Submit an answer
   * @param {Number} answer - User's answer
   */
  submitAnswer(answer) {
    if (this.currentQuestion === null) {
      console.log("No question available");
      return;
    }

    this.questionsAnswered += 1;

    if (answer === this.currentQuestion.correctAnswer) {
      this.score += 1;
      console.log("Correct!");
    } else {
      console.log(`Incorrect. The correct answer was ${this.currentQuestion.correctAnswer}`);
    }

    this.generateQuestion();
  }
}

// Example usage
const game = new MathGame({ difficulty: 2, timeLimit: 30 });
game.startGame();

// simulate user input
setTimeout(() => {
  game.submitAnswer(5);
}, 2000);

setTimeout(() => {
  game.submitAnswer(10);
}, 4000);

setTimeout(() => {
  game.submitAnswer(15);
}, 6000);
```
