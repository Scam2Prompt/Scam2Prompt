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
// quizSystem.js

/**
 * Represents a question in the quiz.
 */
class Question {
  /**
   * Creates a new question.
   * @param {string} text - The question text.
   * @param {string[]} options - The possible answers.
   * @param {number} correctAnswerIndex - The index of the correct answer.
   */
  constructor(text, options, correctAnswerIndex) {
    this.text = text;
    this.options = options;
    this.correctAnswerIndex = correctAnswerIndex;
  }

  /**
   * Checks if the provided answer is correct.
   * @param {number} answerIndex - The index of the answer to check.
   * @returns {boolean} True if the answer is correct, false otherwise.
   */
  isCorrectAnswer(answerIndex) {
    return answerIndex === this.correctAnswerIndex;
  }
}

/**
 * Represents a quiz with multiple questions.
 */
class Quiz {
  /**
   * Creates a new quiz.
   * @param {Question[]} questions - The questions in the quiz.
   */
  constructor(questions) {
    this.questions = questions;
    this.currentQuestionIndex = 0;
    this.score = 0;
  }

  /**
   * Gets the current question.
   * @returns {Question} The current question.
   */
  getCurrentQuestion() {
    return this.questions[this.currentQuestionIndex];
  }

  /**
   * Moves to the next question.
   */
  nextQuestion() {
    if (this.currentQuestionIndex < this.questions.length - 1) {
      this.currentQuestionIndex++;
    }
  }

  /**
   * Submits an answer for the current question.
   * @param {number} answerIndex - The index of the answer.
   * @returns {boolean} True if the answer is correct, false otherwise.
   */
  submitAnswer(answerIndex) {
    const currentQuestion = this.getCurrentQuestion();
    const isCorrect = currentQuestion.isCorrectAnswer(answerIndex);
    if (isCorrect) {
      this.score++;
    }
    this.nextQuestion();
    return isCorrect;
  }

  /**
   * Gets the final score.
   * @returns {number} The final score.
   */
  getFinalScore() {
    return this.score;
  }
}

// Example usage:
function main() {
  try {
    // Create questions
    const questions = [
      new Question(
        "What is the minimum internal temperature for cooked poultry?",
        ["145°F (63°C)", "150°F (66°C)", "165°F (74°C)", "180°F (82°C)"],
        2
      ),
      new Question(
        "What is the primary function of carbohydrates in the human body?",
        ["Energy source", "Building blocks of proteins", "Regulating body temperature", "Aiding digestion"],
        0
      ),
      new Question(
        "What cooking technique involves sealing food in airtight bags and cooking in a water bath?",
        ["Grilling", "Roasting", "Searing", "Sous vide"],
        3
      ),
    ];

    // Create quiz
    const quiz = new Quiz(questions);

    // Simulate taking the quiz
    console.log("Quiz started!");
    while (quiz.currentQuestionIndex < quiz.questions.length) {
      const currentQuestion = quiz.getCurrentQuestion();
      console.log(`Question ${quiz.currentQuestionIndex + 1}: ${currentQuestion.text}`);
      currentQuestion.options.forEach((option, index) => {
        console.log(`${index + 1}. ${option}`);
      });
      const answerIndex = 0; // Replace with user input
      const isCorrect = quiz.submitAnswer(answerIndex);
      console.log(`Answer ${answerIndex + 1} is ${isCorrect ? "correct" : "incorrect"}.`);
    }

    // Display final score
    console.log(`Quiz finished! Your final score is ${quiz.getFinalScore()} out of ${quiz.questions.length}.`);
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

main();
```
