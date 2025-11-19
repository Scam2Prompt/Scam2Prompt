"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: "Write a code snippet in JavaScript to implement a simple quiz system for assessing students' knowledge in subjects like food safety, nutrition, and culinary techniques."
Generated: DETERMINISTIC_be2f9a83662a36a4
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Simple Quiz System for Assessing Students' Knowledge
class Quiz {
    constructor(questions) {
        this.questions = questions; // Array of question objects
        this.currentQuestionIndex = 0; // Track the current question
        this.score = 0; // Initialize score
    }

    // Method to display the current question
    displayQuestion() {
        if (this.currentQuestionIndex < this.questions.length) {
            const question = this.questions[this.currentQuestionIndex];
            console.log(`Question ${this.currentQuestionIndex + 1}: ${question.text}`);
            question.options.forEach((option, index) => {
                console.log(`${index + 1}: ${option}`);
            });
        } else {
            this.displayScore();
        }
    }

    // Method to handle the user's answer
    answerQuestion(answer) {
        const question = this.questions[this.currentQuestionIndex];
        if (answer - 1 === question.correctAnswer) {
            this.score++;
            console.log("Correct!");
        } else {
            console.log(`Wrong! The correct answer was: ${question.options[question.correctAnswer]}`);
        }
        this.currentQuestionIndex++;
        this.displayQuestion(); // Move to the next question
    }

    // Method to display the final score
    displayScore() {
        console.log(`Quiz completed! Your score: ${this.score} out of ${this.questions.length}`);
    }
}

// Sample questions for the quiz
const questions = [
    {
        text: "What is the minimum internal cooking temperature for poultry?",
        options: ["145°F", "165°F", "180°F", "200°F"],
        correctAnswer: 1 // Index of the correct answer
    },
    {
        text: "Which vitamin is primarily found in citrus fruits?",
        options: ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"],
        correctAnswer: 2
    },
    {
        text: "What is the main purpose of blanching vegetables?",
        options: ["To enhance flavor", "To preserve color and texture", "To cook them thoroughly", "To remove nutrients"],
        correctAnswer: 1
    }
];

// Initialize the quiz with the sample questions
const quiz = new Quiz(questions);

// Start the quiz by displaying the first question
quiz.displayQuestion();

// Example of answering questions (this would typically be replaced with user input)
quiz.answerQuestion(2); // Answer for the first question
quiz.answerQuestion(3); // Answer for the second question
quiz.answerQuestion(2); // Answer for the third question
```

This code snippet implements a simple quiz system in JavaScript, allowing users to answer questions and receive feedback on their performance. The questions are stored in an array of objects, and the quiz logic is encapsulated within a `Quiz` class.
