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
// EnglishVocabularyQuiz.js

class Question {
  /**
   * Represents a multiple-choice question.
   * @param {string} question - The question text.
   * @param {string[]} options - The possible answers.
   * @param {number} correctIndex - The index of the correct answer.
   */
  constructor(question, options, correctIndex) {
    this.question = question;
    this.options = options;
    this.correctIndex = correctIndex;
  }
}

class Quiz {
  /**
   * Represents a simple English vocabulary quiz game.
   * @param {Question[]} questions - The list of questions.
   */
  constructor(questions) {
    this.questions = questions;
    this.score = 0;
    this.currentQuestionIndex = 0;
  }

  /**
   * Displays the current question and its options.
   * @returns {void}
   */
  displayCurrentQuestion() {
    const currentQuestion = this.questions[this.currentQuestionIndex];
    console.log(`Question ${this.currentQuestionIndex + 1}: ${currentQuestion.question}`);
    currentQuestion.options.forEach((option, index) => {
      console.log(`${index + 1}. ${option}`);
    });
  }

  /**
   * Checks if the user's answer is correct.
   * @param {number} userAnswerIndex - The index of the user's answer.
   * @returns {boolean} True if the answer is correct, false otherwise.
   */
  checkAnswer(userAnswerIndex) {
    const currentQuestion = this.questions[this.currentQuestionIndex];
    return userAnswerIndex === currentQuestion.correctIndex;
  }

  /**
   * Proceeds to the next question or ends the quiz if all questions have been answered.
   * @returns {void}
   */
  nextQuestion() {
    this.currentQuestionIndex++;
    if (this.currentQuestionIndex >= this.questions.length) {
      this.endQuiz();
    }
  }

  /**
   * Ends the quiz and displays the final score.
   * @returns {void}
   */
  endQuiz() {
    console.log(`Quiz finished! Your final score is ${this.score} out of ${this.questions.length}.`);
  }

  /**
   * Plays the quiz game.
   * @returns {void}
   */
  play() {
    console.log("Welcome to the English Vocabulary Quiz!");
    this.displayCurrentQuestion();
    const readline = require("readline").createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    const askQuestion = () => {
      readline.question("Enter the number of your answer: ", (userAnswer) => {
        const userAnswerIndex = parseInt(userAnswer) - 1;
        if (isNaN(userAnswerIndex) || userAnswerIndex < 0 || userAnswerIndex >= this.questions[this.currentQuestionIndex].options.length) {
          console.log("Invalid answer. Please try again.");
          askQuestion();
        } else {
          if (this.checkAnswer(userAnswerIndex)) {
            console.log("Correct!");
            this.score++;
          } else {
            console.log(`Incorrect. The correct answer was ${this.questions[this.currentQuestionIndex].options[this.questions[this.currentQuestionIndex].correctIndex]}`);
          }
          this.nextQuestion();
          if (this.currentQuestionIndex < this.questions.length) {
            this.displayCurrentQuestion();
            askQuestion();
          } else {
            readline.close();
          }
        }
      });
    };
    askQuestion();
  }
}

// Example usage:
const questions = [
  new Question("What does 'apple' mean?", ["a type of fruit", "a type of car", "a type of animal"], 0),
  new Question("What does 'dog' mean?", ["a type of animal", "a type of food", "a type of vehicle"], 0),
  new Question("What does 'house' mean?", ["a type of building", "a type of tree", "a type of animal"], 0),
];

const quiz = new Quiz(questions);
quiz.play();
```
