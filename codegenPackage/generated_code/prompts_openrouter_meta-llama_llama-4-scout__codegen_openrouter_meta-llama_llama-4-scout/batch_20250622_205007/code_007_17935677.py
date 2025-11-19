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
// quiz.js

/**
 * Represents a quiz question.
 * @typedef {Object} Question
 * @property {string} text - The question text.
 * @property {string[]} options - The possible answers.
 * @property {string} correctAnswer - The correct answer.
 */

/**
 * Represents a quiz.
 * @typedef {Object} Quiz
 * @property {Question[]} questions - The quiz questions.
 * @property {number} score - The current score.
 */

/**
 * Creates a new quiz.
 * @returns {Quiz} A new quiz object.
 */
function createQuiz() {
  return {
    questions: [],
    score: 0,
  };
}

/**
 * Adds a question to the quiz.
 * @param {Quiz} quiz - The quiz object.
 * @param {Question} question - The question to add.
 */
function addQuestion(quiz, question) {
  quiz.questions.push(question);
}

/**
 * Displays a question and returns the user's answer.
 * @param {Question} question - The question to display.
 * @returns {string} The user's answer.
 */
function displayQuestion(question) {
  console.log(`Question: ${question.text}`);
  for (let i = 0; i < question.options.length; i++) {
    console.log(`${i + 1}. ${question.options[i]}`);
  }
  let answer;
  while (true) {
    answer = prompt("Enter the number of your answer:");
    if (!isNaN(answer) && answer > 0 && answer <= question.options.length) {
      return question.options[answer - 1];
    }
    console.log("Invalid answer. Please try again.");
  }
}

/**
 * Checks if the user's answer is correct.
 * @param {Question} question - The question.
 * @param {string} userAnswer - The user's answer.
 * @returns {boolean} True if the answer is correct, false otherwise.
 */
function checkAnswer(question, userAnswer) {
  return userAnswer === question.correctAnswer;
}

/**
 * Runs the quiz.
 * @param {Quiz} quiz - The quiz object.
 */
function runQuiz(quiz) {
  for (let i = 0; i < quiz.questions.length; i++) {
    const question = quiz.questions[i];
    const userAnswer = displayQuestion(question);
    if (checkAnswer(question, userAnswer)) {
      console.log("Correct!");
      quiz.score++;
    } else {
      console.log(`Incorrect. The correct answer was ${question.correctAnswer}.`);
    }
  }
  console.log(`Quiz finished. Your score is ${quiz.score} out of ${quiz.questions.length}.`);
}

// Create a new quiz
const quiz = createQuiz();

// Add questions to the quiz
addQuestion(quiz, {
  text: "What is the capital of Iran?",
  options: ["Tehran", "Mashhad", "Isfahan", "Shiraz"],
  correctAnswer: "Tehran",
});

addQuestion(quiz, {
  text: "What is the largest planet in our solar system?",
  options: ["Earth", "Saturn", "Jupiter", "Uranus"],
  correctAnswer: "Jupiter",
});

addQuestion(quiz, {
  text: "Who wrote 'To Kill a Mockingbird'?",
  options: ["F. Scott Fitzgerald", "Harper Lee", "Jane Austen", "J.K. Rowling"],
  correctAnswer: "Harper Lee",
});

// Run the quiz
runQuiz(quiz);
```
