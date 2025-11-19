"""
Generated Code Metadata:
========================
Original URL: https://immediate-core.com
Prompt: Generate a code snippet in JavaScript to implement a simple quiz on financial literacy, covering topics such as investment strategies and risk management.
Generated: DETERMINISTIC_c2320e26ca981db7
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Financial Literacy Quiz

class Question {
  /**
   * Represents a question in the quiz.
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

class Quiz {
  /**
   * Represents a financial literacy quiz.
   */
  constructor() {
    this.questions = [];
    this.score = 0;
    this.currentQuestionIndex = 0;
  }

  /**
   * Adds a question to the quiz.
   * @param {Question} question - The question to add.
   */
  addQuestion(question) {
    this.questions.push(question);
  }

  /**
   * Starts the quiz.
   */
  start() {
    if (this.questions.length === 0) {
      throw new Error("No questions added to the quiz.");
    }
    this.currentQuestionIndex = 0;
    this.score = 0;
  }

  /**
   * Answers the current question.
   * @param {number} answerIndex - The index of the answer.
   * @returns {boolean} True if the answer is correct, false otherwise.
   */
  answerCurrentQuestion(answerIndex) {
    if (this.currentQuestionIndex >= this.questions.length) {
      throw new Error("No current question.");
    }
    const isCorrect = this.questions[this.currentQuestionIndex].isCorrectAnswer(answerIndex);
    if (isCorrect) {
      this.score++;
    }
    this.currentQuestionIndex++;
    return isCorrect;
  }

  /**
   * Gets the current question.
   * @returns {Question} The current question.
   */
  getCurrentQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      return null;
    }
    return this.questions[this.currentQuestionIndex];
  }

  /**
   * Gets the final score.
   * @returns {number} The final score.
   */
  getFinalScore() {
    return this.score;
  }
}

// Create a quiz
const quiz = new Quiz();

// Add questions
quiz.addQuestion(new Question(
  "What is the primary goal of diversification in investment?",
  ["To increase potential returns", "To reduce risk", "To avoid taxes", "To maximize fees"],
  1
));

quiz.addQuestion(new Question(
  "What type of risk is associated with the possibility of a borrower defaulting on a loan?",
  ["Market risk", "Credit risk", "Liquidity risk", "Operational risk"],
  1
));

quiz.addQuestion(new Question(
  "What is a key benefit of a long-term investment strategy?",
  ["Higher liquidity", "Lower risk", "Increased potential for returns", "Easier access to funds"],
  2
));

// Start the quiz
quiz.start();

// Example usage
function runQuiz() {
  try {
    while (true) {
      const currentQuestion = quiz.getCurrentQuestion();
      if (!currentQuestion) {
        break;
      }
      console.log(`Question ${quiz.currentQuestionIndex + 1}: ${currentQuestion.text}`);
      for (let i = 0; i < currentQuestion.options.length; i++) {
        console.log(`${i + 1}. ${currentQuestion.options[i]}`);
      }
      const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
      });
      readline.question('Enter the number of your answer: ', (answer) => {
        const answerIndex = parseInt(answer) - 1;
        if (isNaN(answerIndex) || answerIndex < 0 || answerIndex >= currentQuestion.options.length) {
          console.log("Invalid answer. Please try again.");
          return readline.close() && runQuiz();
        }
        const isCorrect = quiz.answerCurrentQuestion(answerIndex);
        console.log(`Your answer is ${isCorrect ? 'correct' : 'incorrect'}.`);
        readline.close();
      });
    }
    console.log(`Quiz finished. Your final score is ${quiz.getFinalScore()} out of ${quiz.questions.length}.`);
  } catch (error) {
    console.error(error.message);
  }
}

runQuiz();
```
