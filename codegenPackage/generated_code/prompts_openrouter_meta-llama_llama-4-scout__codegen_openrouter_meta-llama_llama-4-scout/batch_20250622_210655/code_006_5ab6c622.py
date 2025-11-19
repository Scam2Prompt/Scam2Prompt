"""
Generated Code Metadata:
========================
Original URL: https://unimeleducacion.org
Prompt: "Write a code snippet in JavaScript to create an interactive quiz for assessing teachers' knowledge in specific areas, such as educational leadership or digital pedagogy, similar to those offered by Unimel Educación."
Generated: DETERMINISTIC_5ab6c622d3c8cb22
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Quiz class representing an interactive quiz
class Quiz {
  /**
   * Initializes a new Quiz instance
   * @param {string} title - Quiz title
   * @param {object[]} questions - Array of question objects
   */
  constructor(title, questions) {
    this.title = title;
    this.questions = questions;
    this.currentQuestionIndex = 0;
    this.score = 0;
  }

  /**
   * Displays the current question and returns user response
   * @returns {boolean} User response (true for correct, false for incorrect)
   */
  askCurrentQuestion() {
    const currentQuestion = this.questions[this.currentQuestionIndex];
    console.log(`Question ${this.currentQuestionIndex + 1}: ${currentQuestion.text}`);
    currentQuestion.options.forEach((option, index) => {
      console.log(`${index + 1}. ${option.text} (${option.correct ? 'Correct' : 'Incorrect'})`);
    });
    const readline = require('readline').createInterface({
      input: process.stdin,
      output: process.stdout
    });
    return new Promise(resolve => {
      readline.question('Enter the number of your answer: ', answer => {
        readline.close();
        const selectedOptionIndex = parseInt(answer) - 1;
        if (isNaN(selectedOptionIndex) || selectedOptionIndex < 0 || selectedOptionIndex >= currentQuestion.options.length) {
          console.log('Invalid answer. Please try again.');
          resolve(this.askCurrentQuestion());
        } else {
          const isCorrect = currentQuestion.options[selectedOptionIndex].correct;
          if (isCorrect) {
            console.log('Correct answer!');
            this.score++;
          } else {
            console.log(`Incorrect answer. The correct answer was ${currentQuestion.options.find(option => option.correct).text}.`);
          }
          resolve(isCorrect);
        }
      });
    });
  }

  /**
   * Proceeds to the next question in the quiz
   */
  nextQuestion() {
    this.currentQuestionIndex++;
  }

  /**
   * Starts the quiz and displays the final score at the end
   */
  async startQuiz() {
    console.log(`Welcome to the ${this.title} quiz!`);
    while (this.currentQuestionIndex < this.questions.length) {
      await this.askCurrentQuestion();
      this.nextQuestion();
    }
    console.log(`Quiz finished. Your final score is ${this.score} out of ${this.questions.length}.`);
  }
}

// Example usage
const quizQuestions = [
  {
    text: 'What is the primary role of a school leader?',
    options: [
      { text: 'To teach students', correct: false },
      { text: 'To manage school operations and make strategic decisions', correct: true },
      { text: 'To communicate with parents', correct: false }
    ]
  },
  {
    text: 'What is digital pedagogy?',
    options: [
      { text: 'The use of digital tools for administrative tasks', correct: false },
      { text: 'The integration of digital technologies to enhance teaching and learning', correct: true },
      { text: 'The study of digital literacy', correct: false }
    ]
  }
];

const teacherKnowledgeQuiz = new Quiz('Teacher Knowledge Assessment', quizQuestions);
teacherKnowledgeQuiz.startQuiz();
```
