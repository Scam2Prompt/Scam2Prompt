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
// QuizSystem.js

/**
 * Represents a Quiz System for Physics students in Class XI or XII.
 */
class QuizSystem {
  /**
   * Initializes a new instance of the QuizSystem class.
   */
  constructor() {
    this.questions = [];
    this.score = 0;
    this.currentQuestionIndex = 0;
  }

  /**
   * Adds a new question to the quiz system.
   * @param {string} question - The question text.
   * @param {string[]} options - The possible options.
   * @param {number} correctOptionIndex - The index of the correct option.
   */
  addQuestion(question, options, correctOptionIndex) {
    if (!question || !options || options.length === 0 || correctOptionIndex < 0 || correctOptionIndex >= options.length) {
      throw new Error("Invalid question data");
    }

    this.questions.push({
      question,
      options,
      correctOptionIndex,
    });
  }

  /**
   * Starts the quiz.
   */
  startQuiz() {
    if (this.questions.length === 0) {
      console.log("No questions added to the quiz system.");
      return;
    }

    this.score = 0;
    this.currentQuestionIndex = 0;
    this.displayCurrentQuestion();
  }

  /**
   * Displays the current question.
   */
  displayCurrentQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      this.displayQuizResults();
      return;
    }

    const currentQuestion = this.questions[this.currentQuestionIndex];
    console.log(`Question ${this.currentQuestionIndex + 1}: ${currentQuestion.question}`);

    currentQuestion.options.forEach((option, index) => {
      console.log(`${index + 1}. ${option}`);
    });

    const readline = require("readline").createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    readline.question("Enter the option number: ", (optionNumber) => {
      const selectedOptionIndex = parseInt(optionNumber) - 1;

      if (isNaN(selectedOptionIndex) || selectedOptionIndex < 0 || selectedOptionIndex >= currentQuestion.options.length) {
        console.log("Invalid option. Please try again.");
        this.displayCurrentQuestion();
        return;
      }

      if (selectedOptionIndex === currentQuestion.correctOptionIndex) {
        console.log("Correct answer!");
        this.score++;
      } else {
        console.log(`Incorrect answer. The correct answer is ${currentQuestion.options[currentQuestion.correctOptionIndex]}`);
      }

      this.currentQuestionIndex++;
      readline.close();
      this.displayCurrentQuestion();
    });
  }

  /**
   * Displays the quiz results.
   */
  displayQuizResults() {
    console.log(`Quiz completed! Your final score is ${this.score} out of ${this.questions.length}`);
  }
}

// Example usage:
const quizSystem = new QuizSystem();

quizSystem.addQuestion(
  "What is the unit of electric charge?",
  ["Ampere", "Volt", "Coulomb", "Ohm"],
  2
);

quizSystem.addQuestion(
  "What is the force that opposes motion between two surfaces?",
  ["Friction", "Gravity", "Normal force", "Tension"],
  0
);

quizSystem.addQuestion(
  "What is the energy transferred per unit time?",
  ["Power", "Energy", "Work", "Force"],
  0
);

quizSystem.startQuiz();
```
