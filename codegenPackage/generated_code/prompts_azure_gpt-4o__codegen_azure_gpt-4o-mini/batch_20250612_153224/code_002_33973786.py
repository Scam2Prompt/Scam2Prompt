"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Generate JavaScript code for a quiz application that incorporates questions about the values of responsibility and equality, tailored for children as outlined in the "Vivir es Convivir" educational program.
Generated: DETERMINISTIC_339737863094b710
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Quiz Application for "Vivir es Convivir" Educational Program
// This application presents a quiz about the values of responsibility and equality tailored for children.

class Quiz {
    constructor(questions) {
        this.questions = questions; // Array of questions
        this.currentQuestionIndex = 0; // Track the current question
        this.score = 0; // Track the user's score
    }

    // Method to display the current question
    displayQuestion() {
        if (this.currentQuestionIndex < this.questions.length) {
            const question = this.questions[this.currentQuestionIndex];
            console.log(`Question ${this.currentQuestionIndex + 1}: ${question.text}`);
            question.answers.forEach((answer, index) => {
                console.log(`${index + 1}: ${answer}`);
            });
        } else {
            this.displayScore();
        }
    }

    // Method to handle user's answer
    answerQuestion(answerIndex) {
        const question = this.questions[this.currentQuestionIndex];
        if (answerIndex < 1 || answerIndex > question.answers.length) {
            console.error("Invalid answer. Please select a valid option.");
            return;
        }

        if (question.correctAnswer === answerIndex) {
            this.score++;
            console.log("Correct answer!");
        } else {
            console.log("Wrong answer. The correct answer was: " + question.answers[question.correctAnswer - 1]);
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
        text: "What does it mean to be responsible?",
        answers: [
            "To take care of your things",
            "To ignore your duties",
            "To blame others for mistakes"
        ],
        correctAnswer: 1 // Correct answer is the first option
    },
    {
        text: "Why is equality important?",
        answers: [
            "Because everyone should be treated the same",
            "Because some people are better than others",
            "Because it doesn't matter how we treat others"
        ],
        correctAnswer: 1 // Correct answer is the first option
    },
    {
        text: "How can you show responsibility at school?",
        answers: [
            "By doing your homework",
            "By not listening to the teacher",
            "By making fun of others"
        ],
        correctAnswer: 1 // Correct answer is the first option
    },
    {
        text: "What is a way to promote equality among friends?",
        answers: [
            "By sharing and including everyone",
            "By choosing favorites",
            "By ignoring those who are different"
        ],
        correctAnswer: 1 // Correct answer is the first option
    }
];

// Initialize the quiz with the questions
const quiz = new Quiz(questions);

// Start the quiz
quiz.displayQuestion();

// Example of answering questions (this would typically be replaced with user input)
quiz.answerQuestion(1); // Answer for the first question
quiz.answerQuestion(1); // Answer for the second question
quiz.answerQuestion(1); // Answer for the third question
quiz.answerQuestion(1); // Answer for the fourth question
```

This code provides a simple console-based quiz application that can be expanded with user input handling for a complete interactive experience.
