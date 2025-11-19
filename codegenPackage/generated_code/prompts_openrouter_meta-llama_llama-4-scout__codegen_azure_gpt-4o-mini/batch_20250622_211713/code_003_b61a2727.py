"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Provide a JavaScript code snippet to create a quiz system for Physics students in Class XI or XII, with questions and answers based on CBSE syllabus.
Generated: DETERMINISTIC_b61a27270971f610
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Quiz System for Physics Students (Class XI/XII) based on CBSE Syllabus

class Quiz {
    constructor(questions) {
        this.questions = questions; // Array of question objects
        this.currentQuestionIndex = 0; // Track the current question
        this.score = 0; // Track the user's score
    }

    // Method to display the current question
    displayQuestion() {
        if (this.currentQuestionIndex < this.questions.length) {
            const question = this.questions[this.currentQuestionIndex];
            console.log(`Q${this.currentQuestionIndex + 1}: ${question.question}`);
            question.options.forEach((option, index) => {
                console.log(`${index + 1}: ${option}`);
            });
        } else {
            this.displayScore();
        }
    }

    // Method to handle user's answer
    answerQuestion(answer) {
        const question = this.questions[this.currentQuestionIndex];
        if (question.options[answer - 1] === question.correctAnswer) {
            this.score++;
            console.log("Correct answer!");
        } else {
            console.log(`Wrong answer! The correct answer is: ${question.correctAnswer}`);
        }
        this.currentQuestionIndex++;
        this.displayQuestion(); // Display the next question
    }

    // Method to display the final score
    displayScore() {
        console.log(`Quiz completed! Your score: ${this.score} out of ${this.questions.length}`);
    }
}

// Sample questions based on CBSE syllabus
const questions = [
    {
        question: "What is the unit of force?",
        options: ["Newton", "Joule", "Pascal", "Watt"],
        correctAnswer: "Newton"
    },
    {
        question: "What is the acceleration due to gravity on Earth?",
        options: ["9.8 m/s²", "10 m/s²", "9.81 m/s²", "8.9 m/s²"],
        correctAnswer: "9.8 m/s²"
    },
    {
        question: "Which law states that for every action, there is an equal and opposite reaction?",
        options: ["Newton's First Law", "Newton's Second Law", "Newton's Third Law", "Law of Conservation of Energy"],
        correctAnswer: "Newton's Third Law"
    },
    {
        question: "What is the speed of light in vacuum?",
        options: ["3 x 10^8 m/s", "3 x 10^6 m/s", "3 x 10^7 m/s", "3 x 10^9 m/s"],
        correctAnswer: "3 x 10^8 m/s"
    }
];

// Initialize the quiz with the questions
const physicsQuiz = new Quiz(questions);

// Start the quiz by displaying the first question
physicsQuiz.displayQuestion();

// Example of answering questions (this would typically be replaced with user input)
physicsQuiz.answerQuestion(1); // User selects option 1 for the first question
physicsQuiz.answerQuestion(3); // User selects option 3 for the second question
physicsQuiz.answerQuestion(3); // User selects option 3 for the third question
physicsQuiz.answerQuestion(1); // User selects option 1 for the fourth question
```

This code snippet creates a simple quiz system for Physics students, allowing them to answer questions and receive feedback on their answers. The questions are based on the CBSE syllabus, and the system tracks the user's score throughout the quiz.
