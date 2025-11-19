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
// QuizApplication.js

/**
 * Quiz Application for "Vivir es Convivir" educational program.
 * 
 * This application presents a series of questions to the user, 
 * assessing their understanding of responsibility and equality values.
 */

// Quiz questions and answers
const quizQuestions = [
  {
    question: "What does it mean to be responsible?",
    options: [
      "To do what you want, when you want",
      "To take care of things and do what's right",
      "To blame others for your mistakes",
      "To ignore problems and hope they go away"
    ],
    correctAnswer: 1,
    explanation: "Being responsible means taking care of things and doing what's right."
  },
  {
    question: "What is equality?",
    options: [
      "When everyone is the same",
      "When everyone has the same opportunities and is treated fairly",
      "When some people are better than others",
      "When some people have more than others"
    ],
    correctAnswer: 1,
    explanation: "Equality means everyone has the same opportunities and is treated fairly."
  },
  {
    question: "Why is it important to respect others?",
    options: [
      "Because it's a rule",
      "Because it makes others happy and we can all get along",
      "Because it's a sign of weakness",
      "Because it's not important"
    ],
    correctAnswer: 1,
    explanation: "Respecting others is important because it makes others happy and we can all get along."
  }
];

// Quiz application class
class QuizApplication {
  constructor(questions) {
    this.questions = questions;
    this.currentQuestionIndex = 0;
    this.score = 0;
  }

  /**
   * Presents the current question to the user.
   * 
   * @returns {object} The current question object.
   */
  presentQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      throw new Error("No more questions available.");
    }

    return this.questions[this.currentQuestionIndex];
  }

  /**
   * Submits the user's answer for the current question.
   * 
   * @param {number} answerIndex The index of the user's answer.
   */
  submitAnswer(answerIndex) {
    const currentQuestion = this.questions[this.currentQuestionIndex];

    if (answerIndex === currentQuestion.correctAnswer) {
      this.score++;
      console.log(`Correct! ${currentQuestion.explanation}`);
    } else {
      console.log(`Incorrect. The correct answer is ${currentQuestion.options[currentQuestion.correctAnswer]}. ${currentQuestion.explanation}`);
    }

    this.currentQuestionIndex++;
  }

  /**
   * Gets the final score.
   * 
   * @returns {number} The user's final score.
   */
  getFinalScore() {
    return this.score;
  }
}

// Main function
function main() {
  const quizApp = new QuizApplication(quizQuestions);

  console.log("Welcome to the 'Vivir es Convivir' quiz!");

  for (let i = 0; i < quizQuestions.length; i++) {
    const question = quizApp.presentQuestion();
    console.log(`Question ${i + 1}: ${question.question}`);

    question.options.forEach((option, index) => {
      console.log(`${index}. ${option}`);
    });

    const readline = require('readline').createInterface({
      input: process.stdin,
      output: process.stdout
    });

    readline.question('Enter the number of your answer: ', (answer) => {
      const answerIndex = parseInt(answer);

      if (isNaN(answerIndex) || answerIndex < 0 || answerIndex >= question.options.length) {
        console.log("Invalid answer. Please try again.");
        return;
      }

      quizApp.submitAnswer(answerIndex);

      readline.close();

      if (i === quizQuestions.length - 1) {
        console.log(`Quiz finished! Your final score is ${quizApp.getFinalScore()} out of ${quizQuestions.length}.`);
      }
    });
  }
}

main();
```
