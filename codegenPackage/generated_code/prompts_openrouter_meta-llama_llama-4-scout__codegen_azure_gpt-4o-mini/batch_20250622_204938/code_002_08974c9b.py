"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Generate a code snippet in JavaScript to create an interactive quiz or game for children, inspired by the educational activities mentioned on smplanka.lk.
Generated: DETERMINISTIC_08974c9b75eddc1b
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Interactive Quiz Game for Children
// This game presents a series of questions and tracks the user's score.

class QuizGame {
    constructor(questions) {
        this.questions = questions; // Array of question objects
        this.currentQuestionIndex = 0; // Track the current question
        this.score = 0; // Initialize score
    }

    // Method to start the quiz
    start() {
        this.currentQuestionIndex = 0;
        this.score = 0;
        this.displayQuestion();
    }

    // Method to display the current question
    displayQuestion() {
        if (this.currentQuestionIndex < this.questions.length) {
            const question = this.questions[this.currentQuestionIndex];
            const questionContainer = document.getElementById('question-container');
            questionContainer.innerHTML = `
                <h2>${question.question}</h2>
                <ul>
                    ${question.answers.map((answer, index) => `
                        <li>
                            <button onclick="quizGame.checkAnswer(${index})">${answer}</button>
                        </li>
                    `).join('')}
                </ul>
            `;
        } else {
            this.displayScore();
        }
    }

    // Method to check the selected answer
    checkAnswer(selectedIndex) {
        const question = this.questions[this.currentQuestionIndex];
        if (selectedIndex === question.correctAnswerIndex) {
            this.score++;
        }
        this.currentQuestionIndex++;
        this.displayQuestion();
    }

    // Method to display the final score
    displayScore() {
        const questionContainer = document.getElementById('question-container');
        questionContainer.innerHTML = `
            <h2>Quiz Finished!</h2>
            <p>Your score: ${this.score} out of ${this.questions.length}</p>
            <button onclick="quizGame.start()">Restart Quiz</button>
        `;
    }
}

// Sample questions for the quiz
const questions = [
    {
        question: "What is the capital of Sri Lanka?",
        answers: ["Colombo", "Kandy", "Galle", "Jaffna"],
        correctAnswerIndex: 0
    },
    {
        question: "Which animal is known as the king of the jungle?",
        answers: ["Elephant", "Lion", "Tiger", "Giraffe"],
        correctAnswerIndex: 1
    },
    {
        question: "What is 2 + 2?",
        answers: ["3", "4", "5", "6"],
        correctAnswerIndex: 1
    }
];

// Initialize the quiz game
const quizGame = new QuizGame(questions);

// Start the quiz when the page loads
window.onload = () => {
    quizGame.start();
};
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Quiz Game</title>
    <style>
        body { font-family: Arial, sans-serif; }
        #question-container { margin: 20px; }
        button { margin: 5px; }
    </style>
</head>
<body>
    <div id="question-container"></div>
    <script src="quizGame.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
