"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Generate a code snippet in JavaScript to create an interactive quiz or game for children, inspired by the educational activities mentioned on smplanka.lk.
Generated: DETERMINISTIC_08974c9b75eddc1b
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Interactive Quiz Game for Children
 * Inspired by educational activities on smplanka.lk
 */

class QuizGame {
  constructor() {
    this.questions = [];
    this.currentQuestionIndex = 0;
    this.score = 0;
    this.initialize();
  }

  initialize() {
    this.loadQuestions();
    this.setupEventListeners();
    this.displayQuestion();
  }

  loadQuestions() {
    // Sample questions - these could be loaded from an API in a real implementation
    this.questions = [
      {
        question: "What is 2 + 3?",
        options: ["4", "5", "6", "7"],
        correctAnswer: 1
      },
      {
        question: "Which animal says 'meow'?",
        options: ["Dog", "Cow", "Cat", "Lion"],
        correctAnswer: 2
      },
      {
        question: "What color is the sky on a clear day?",
        options: ["Green", "Red", "Blue", "Yellow"],
        correctAnswer: 2
      }
    ];
  }

  setupEventListeners() {
    document.getElementById('next-btn').addEventListener('click', () => this.nextQuestion());
    document.getElementById('restart-btn').addEventListener('click', () => this.restartGame());
    
    const optionsContainer = document.getElementById('options-container');
    optionsContainer.addEventListener('click', (e) => {
      if (e.target.classList.contains('option-btn')) {
        this.checkAnswer(parseInt(e.target.dataset.index));
      }
    });
  }

  displayQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      this.showResults();
      return;
    }

    const currentQuestion = this.questions[this.currentQuestionIndex];
    document.getElementById('question-text').textContent = currentQuestion.question;
    
    const optionsContainer = document.getElementById('options-container');
    optionsContainer.innerHTML = '';
    
    currentQuestion.options.forEach((option, index) => {
      const button = document.createElement('button');
      button.className = 'option-btn';
      button.textContent = option;
      button.dataset.index = index;
      optionsContainer.appendChild(button);
    });
    
    document.getElementById('progress').textContent = 
      `Question ${this.currentQuestionIndex + 1} of ${this.questions.length}`;
  }

  checkAnswer(selectedIndex) {
    const currentQuestion = this.questions[this.currentQuestionIndex];
    const options = document.querySelectorAll('.option-btn');
    
    options.forEach(option => {
      option.disabled = true;
      if (parseInt(option.dataset.index) === currentQuestion.correctAnswer) {
        option.classList.add('correct');
      } else if (parseInt(option.dataset.index) === selectedIndex && selectedIndex !== currentQuestion.correctAnswer) {
        option.classList.add('incorrect');
      }
    });

    if (selectedIndex === currentQuestion.correctAnswer) {
      this.score++;
      document.getElementById('feedback').textContent = "Correct! 🎉";
    } else {
      document.getElementById('feedback').textContent = "Oops! Try again. 🤔";
    }
  }

  nextQuestion() {
    this.currentQuestionIndex++;
    document.getElementById('feedback').textContent = '';
    this.displayQuestion();
  }

  showResults() {
    const quizContainer = document.getElementById('quiz-container');
    quizContainer.innerHTML = `
      <div class="results">
        <h2>Quiz Completed!</h2>
        <p>Your score: ${this.score} out of ${this.questions.length}</p>
        <button id="restart-btn" class="btn">Play Again</button>
      </div>
    `;
    document.getElementById('restart-btn').addEventListener('click', () => this.restartGame());
  }

  restartGame() {
    this.currentQuestionIndex = 0;
    this.score = 0;
    document.getElementById('quiz-container').innerHTML = `
      <div id="question-container">
        <p id="progress"></p>
        <h2 id="question-text"></h2>
        <div id="options-container" class="options"></div>
        <p id="feedback"></p>
        <button id="next-btn" class="btn">Next Question</button>
      </div>
    `;
    this.initialize();
  }
}

// Initialize the game when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new QuizGame();
});
```
