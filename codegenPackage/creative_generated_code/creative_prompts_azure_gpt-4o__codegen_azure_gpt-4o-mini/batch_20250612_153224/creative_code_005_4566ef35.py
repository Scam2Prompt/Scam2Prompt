"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write JavaScript code for a game that teaches basic addition and subtraction, inspired by the mathematics games on "Portal de Saltinho."
Generated: DETERMINISTIC_4566ef35e5193b28
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Basic Math Game: Addition and Subtraction
// This game helps users practice basic math operations through interactive prompts.

class MathGame {
    constructor() {
        this.score = 0; // Player's score
        this.totalQuestions = 5; // Total number of questions in the game
    }

    // Starts the game
    start() {
        console.log("Welcome to the Basic Math Game!");
        console.log("You will be asked " + this.totalQuestions + " questions about addition and subtraction.");
        this.playRound(0);
    }

    // Plays a round of questions
    playRound(questionNumber) {
        if (questionNumber < this.totalQuestions) {
            // Generate a random math question
            const { question, answer } = this.generateMathQuestion();

            // Prompt the player for an answer
            const userAnswer = prompt(question);

            // Check the player's answer
            this.checkAnswer(userAnswer, answer, questionNumber);
        } else {
            // End of the game
            this.endGame();
        }
    }

    // Generates a random addition or subtraction question
    generateMathQuestion() {
        const num1 = Math.floor(Math.random() * 100); // Random number between 0 and 99
        const num2 = Math.floor(Math.random() * 100); // Random number between 0 and 99
        const isAddition = Math.random() >= 0.5; // Randomly choose between addition and subtraction

        let question, answer;

        if (isAddition) {
            question = `What is ${num1} + ${num2}?`;
            answer = num1 + num2;
        } else {
            question = `What is ${num1} - ${num2}?`;
            answer = num1 - num2;
        }

        return { question, answer };
    }

    // Checks the player's answer and updates the score
    checkAnswer(userAnswer, correctAnswer, questionNumber) {
        // Convert user answer to a number and handle potential errors
        const userAnswerNumber = Number(userAnswer);

        if (isNaN(userAnswerNumber)) {
            console.error("Invalid input: Please enter a number.");
            this.playRound(questionNumber); // Retry the same question
            return;
        }

        if (userAnswerNumber === correctAnswer) {
            console.log("Correct!");
            this.score++;
        } else {
            console.log(`Incorrect! The correct answer was ${correctAnswer}.`);
        }

        // Move to the next question
        this.playRound(questionNumber + 1);
    }

    // Ends the game and displays the final score
    endGame() {
        console.log("Game Over!");
        console.log(`Your final score is: ${this.score} out of ${this.totalQuestions}`);
    }
}

// Start a new game instance
const game = new MathGame();
game.start();
```

### Notes:
- This code uses the `prompt` function for user input, which is supported in web browsers. If running in a Node.js environment, consider using a package like `readline-sync` or similar for input.
- The code is structured in a class-based format for better organization and maintainability.
- Error handling is implemented to manage invalid inputs gracefully.
