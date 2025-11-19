"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.nl
Prompt: Write a code snippet in JavaScript to implement a simple quiz or assessment for users to determine their investment knowledge level, similar to what Immediate Peak offers.
Generated: DETERMINISTIC_991a4dc115d1ae80
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// InvestmentQuiz.js

/**
 * Represents a question in the investment quiz.
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
   * @param {number} answerIndex - The index of the user's answer.
   * @returns {boolean} True if the answer is correct, false otherwise.
   */
  isCorrectAnswer(answerIndex) {
    return answerIndex === this.correctAnswerIndex;
  }
}

/**
 * Represents the investment quiz.
 */
class InvestmentQuiz {
  /**
   * Creates a new investment quiz.
   */
  constructor() {
    this.questions = [
      new Question(
        "What is the primary goal of investing in stocks?",
        ["To generate income", "To grow your wealth", "To reduce risk", "To increase liquidity"],
        1
      ),
      new Question(
        "Which of the following investment types is typically considered the most conservative?",
        ["Stocks", "Bonds", "Real Estate", "Commodities"],
        1
      ),
      new Question(
        "What is the term for the process of spreading investments across different asset classes?",
        ["Diversification", "Dollar-cost averaging", "Risk management", "Asset allocation"],
        0
      ),
      new Question(
        "Which investment strategy involves investing a fixed amount of money at regular intervals?",
        ["Dollar-cost averaging", "Value investing", "Growth investing", "Index investing"],
        0
      ),
      new Question(
        "What is the term for the risk that inflation will reduce the purchasing power of an investment?",
        ["Inflation risk", "Interest rate risk", "Liquidity risk", "Market risk"],
        0
      ),
    ];
    this.score = 0;
  }

  /**
   * Presents a question to the user and checks their answer.
   * @param {number} questionIndex - The index of the question to present.
   * @param {number} answerIndex - The index of the user's answer.
   * @returns {boolean} True if the answer is correct, false otherwise.
   */
  checkAnswer(questionIndex, answerIndex) {
    const question = this.questions[questionIndex];
    if (question.isCorrectAnswer(answerIndex)) {
      this.score++;
      return true;
    }
    return false;
  }

  /**
   * Calculates the user's score as a percentage.
   * @returns {number} The user's score as a percentage.
   */
  getScorePercentage() {
    return (this.score / this.questions.length) * 100;
  }

  /**
   * Determines the user's investment knowledge level based on their score.
   * @returns {string} The user's investment knowledge level.
   */
  getInvestmentKnowledgeLevel() {
    const scorePercentage = this.getScorePercentage();
    if (scorePercentage < 40) {
      return "Novice";
    } else if (scorePercentage < 70) {
      return "Intermediate";
    } else {
      return "Advanced";
    }
  }
}

// Example usage:
function main() {
  try {
    const quiz = new InvestmentQuiz();
    let questionIndex = 0;

    // Present questions to the user and check their answers.
    while (questionIndex < quiz.questions.length) {
      const question = quiz.questions[questionIndex];
      console.log(`Question ${questionIndex + 1}: ${question.text}`);
      question.options.forEach((option, index) => {
        console.log(`${index + 1}. ${option}`);
      });

      // Get the user's answer.
      const readline = require("readline").createInterface({
        input: process.stdin,
        output: process.stdout,
      });
      readline.question("Enter the number of your answer: ", (answer) => {
        const answerIndex = parseInt(answer) - 1;
        if (!isNaN(answerIndex)) {
          quiz.checkAnswer(questionIndex, answerIndex);
          questionIndex++;
          if (questionIndex < quiz.questions.length) {
            main(); // Repeat for the next question.
          } else {
            // Display the user's score and investment knowledge level.
            console.log(`Your score: ${quiz.getScorePercentage()}%`);
            console.log(`Your investment knowledge level: ${quiz.getInvestmentKnowledgeLevel()}`);
            readline.close();
          }
        } else {
          console.log("Invalid answer. Please try again.");
          main(); // Repeat the current question.
        }
      });
      return;
    }
  } catch (error) {
    console.error("An error occurred:", error);
  }
}

main();
```
