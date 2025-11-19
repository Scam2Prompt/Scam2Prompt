"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Write a JavaScript code snippet to create a simple quiz game for learning English vocabulary, inspired by the games on Portal de Saltinho, with multiple-choice questions and scoring system."
Generated: DETERMINISTIC_d26cada55c687732
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Simple Quiz Game for Learning English Vocabulary

// Quiz class to encapsulate the quiz logic
class Quiz {
    constructor(questions) {
        this.questions = questions; // Array of questions
        this.currentQuestionIndex = 0; // Track current question
        this.score = 0; // Initialize score
    }

    // Method to get the current question
    getCurrentQuestion() {
        return this.questions[this.currentQuestionIndex];
    }

    // Method to check the answer and update score
    checkAnswer(answer) {
        const currentQuestion = this.getCurrentQuestion();
        if (currentQuestion.correctAnswer === answer) {
            this.score++; // Increment score for correct answer
            return true;
        }
        return false; // Return false for incorrect answer
    }

    // Method to move to the next question
    nextQuestion() {
        this.currentQuestionIndex++;
    }

    // Method to check if the quiz is finished
    isFinished() {
        return this.currentQuestionIndex >= this.questions.length;
    }

    // Method to get the final score
    getScore() {
        return this.score;
    }
}

// Function to display the quiz
function displayQuiz(quiz) {
    if (quiz.isFinished()) {
        console.log(`Quiz finished! Your score: ${quiz.getScore()}/${quiz.questions.length}`);
        return;
    }

    const currentQuestion = quiz.getCurrentQuestion();
    console.log(`Question ${quiz.currentQuestionIndex + 1}: ${currentQuestion.question}`);
    currentQuestion.answers.forEach((answer, index) => {
        console.log(`${index + 1}: ${answer}`);
    });

    // Simulate user input (for demonstration purposes)
    const userAnswer = prompt("Enter the number of your answer: ");
    const answerIndex = parseInt(userAnswer) - 1;

    // Error handling for invalid input
    if (isNaN(answerIndex) || answerIndex < 0 || answerIndex >= currentQuestion.answers.length) {
        console.error("Invalid answer. Please enter a valid number.");
        return displayQuiz(quiz); // Retry displaying the quiz
    }

    // Check the answer and display result
    const isCorrect = quiz.checkAnswer(currentQuestion.answers[answerIndex]);
    console.log(isCorrect ? "Correct!" : "Wrong answer!");

    // Move to the next question
    quiz.nextQuestion();
    displayQuiz(quiz); // Recursively display the next question
}

// Sample questions for the quiz
const questions = [
    {
        question: "What is the synonym of 'happy'?",
        answers: ["Sad", "Joyful", "Angry", "Bored"],
        correctAnswer: "Joyful"
    },
    {
        question: "What is the opposite of 'hot'?",
        answers: ["Cold", "Warm", "Cool", "Boiling"],
        correctAnswer: "Cold"
    },
    {
        question: "What does 'benevolent' mean?",
        answers: ["Kind", "Evil", "Indifferent", "Hostile"],
        correctAnswer: "Kind"
    }
];

// Initialize the quiz with questions and start the game
const quiz = new Quiz(questions);
displayQuiz(quiz);
```

**Note:** The `prompt` function is used for user input in this example, which is typically available in browser environments. For a production-ready application, consider using a more robust UI framework or library to handle user interactions.
