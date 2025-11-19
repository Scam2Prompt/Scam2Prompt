"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Write a JavaScript code to create an interactive quiz for students in کارو دانش schools, covering topics from various subjects.
Generated: DETERMINISTIC_179356775d42987d
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Interactive Quiz Application for کارو دانش Schools

// Quiz class to manage the quiz functionality
class Quiz {
    constructor(questions) {
        this.questions = questions; // Array of questions
        this.currentQuestionIndex = 0; // Track the current question
        this.score = 0; // Track the user's score
    }

    // Method to get the current question
    getCurrentQuestion() {
        return this.questions[this.currentQuestionIndex];
    }

    // Method to check the answer and update the score
    checkAnswer(answer) {
        const currentQuestion = this.getCurrentQuestion();
        if (currentQuestion.correctAnswer === answer) {
            this.score++;
        }
        this.currentQuestionIndex++;
    }

    // Method to check if there are more questions
    hasMoreQuestions() {
        return this.currentQuestionIndex < this.questions.length;
    }

    // Method to get the final score
    getScore() {
        return this.score;
    }
}

// Function to display the quiz
function displayQuiz(quiz) {
    const questionElement = document.getElementById('question');
    const optionsElement = document.getElementById('options');
    const scoreElement = document.getElementById('score');

    // Clear previous options
    optionsElement.innerHTML = '';

    // Check if there are more questions
    if (quiz.hasMoreQuestions()) {
        const currentQuestion = quiz.getCurrentQuestion();
        questionElement.textContent = currentQuestion.question;

        // Display options
        currentQuestion.options.forEach(option => {
            const button = document.createElement('button');
            button.textContent = option;
            button.onclick = () => {
                quiz.checkAnswer(option);
                displayQuiz(quiz); // Display next question
            };
            optionsElement.appendChild(button);
        });
    } else {
        // Display final score
        questionElement.textContent = 'Quiz Completed!';
        scoreElement.textContent = `Your score: ${quiz.getScore()} out of ${quiz.questions.length}`;
        optionsElement.innerHTML = ''; // Clear options
    }
}

// Sample questions for the quiz
const questions = [
    {
        question: 'What is the capital of France?',
        options: ['Berlin', 'Madrid', 'Paris', 'Lisbon'],
        correctAnswer: 'Paris'
    },
    {
        question: 'What is 2 + 2?',
        options: ['3', '4', '5', '6'],
        correctAnswer: '4'
    },
    {
        question: 'Which planet is known as the Red Planet?',
        options: ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        correctAnswer: 'Mars'
    }
];

// Initialize the quiz
const quiz = new Quiz(questions);

// Start the quiz on page load
window.onload = () => {
    displayQuiz(quiz);
};
```

```html
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Quiz</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        button {
            margin: 5px;
            padding: 10px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>Quiz for کارو دانش Schools</h1>
    <div id="quiz-container">
        <h2 id="question"></h2>
        <div id="options"></div>
        <h3 id="score"></h3>
    </div>
    <script src="quiz.js"></script>
</body>
</html>
```
