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
/**
 * English Vocabulary Quiz Game
 * A simple multiple-choice quiz game for learning English vocabulary.
 * Inspired by Portal de Saltinho games.
 */

class QuizGame {
  constructor() {
    this.questions = [];
    this.currentQuestionIndex = 0;
    this.score = 0;
    this.quizContainer = null;
    this.resultContainer = null;
    this.nextButton = null;
    this.initialize();
  }

  /**
   * Initialize the quiz game
   */
  initialize() {
    this.loadQuestions();
    this.setupDOM();
    this.displayQuestion();
  }

  /**
   * Load quiz questions
   */
  loadQuestions() {
    this.questions = [
      {
        question: "What is the synonym of 'happy'?",
        options: ["Sad", "Joyful", "Angry", "Tired"],
        correctAnswer: 1
      },
      {
        question: "What does 'benevolent' mean?",
        options: ["Kind", "Evil", "Confused", "Small"],
        correctAnswer: 0
      },
      {
        question: "Which word means 'to run quickly'?",
        options: ["Walk", "Sprint", "Crawl", "Jump"],
        correctAnswer: 1
      },
      {
        question: "What is the opposite of 'ancient'?",
        options: ["Old", "Modern", "Historic", "Classic"],
        correctAnswer: 1
      },
      {
        question: "Which word describes 'extremely hungry'?",
        options: ["Full", "Starving", "Thirsty", "Tired"],
        correctAnswer: 1
      }
    ];
  }

  /**
   * Setup DOM elements
   */
  setupDOM() {
    this.quizContainer = document.getElementById('quiz');
    this.resultContainer = document.getElementById('result');
    this.nextButton = document.getElementById('next');

    if (!this.quizContainer || !this.resultContainer || !this.nextButton) {
      throw new Error('Required DOM elements not found');
    }

    this.nextButton.addEventListener('click', () => this.nextQuestion());
  }

  /**
   * Display current question
   */
  displayQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      this.showResults();
      return;
    }

    const currentQuestion = this.questions[this.currentQuestionIndex];
    const questionElement = document.createElement('div');
    questionElement.className = 'question';
    questionElement.textContent = currentQuestion.question;

    const optionsElement = document.createElement('div');
    optionsElement.className = 'options';

    currentQuestion.options.forEach((option, index) => {
      const optionElement = document.createElement('button');
      optionElement.className = 'option';
      optionElement.textContent = option;
      optionElement.dataset.index = index;
      optionElement.addEventListener('click', (e) => this.selectAnswer(e));
      optionsElement.appendChild(optionElement);
    });

    this.quizContainer.innerHTML = '';
    this.quizContainer.appendChild(questionElement);
    this.quizContainer.appendChild(optionsElement);

    this.nextButton.style.display = 'none';
  }

  /**
   * Handle answer selection
   * @param {Event} e - Click event
   */
  selectAnswer(e) {
    const selectedOption = e.target;
    const selectedIndex = parseInt(selectedOption.dataset.index);
    const correctIndex = this.questions[this.currentQuestionIndex].correctAnswer;

    // Disable all options
    const options = document.querySelectorAll('.option');
    options.forEach(option => {
      option.disabled = true;
      option.classList.remove('correct', 'incorrect');
    });

    // Highlight correct and selected answers
    selectedOption.classList.add(selectedIndex === correctIndex ? 'correct' : 'incorrect');
    options[correctIndex].classList.add('correct');

    // Update score if correct
    if (selectedIndex === correctIndex) {
      this.score++;
    }

    this.nextButton.style.display = 'block';
  }

  /**
   * Move to next question or show results
   */
  nextQuestion() {
    this.currentQuestionIndex++;
    if (this.currentQuestionIndex < this.questions.length) {
      this.displayQuestion();
    } else {
      this.showResults();
    }
  }

  /**
   * Display final results
   */
  showResults() {
    this.quizContainer.style.display = 'none';
    this.nextButton.style.display = 'none';

    const percentage = Math.round((this.score / this.questions.length) * 100);
    let message = '';

    if (percentage >= 80) {
      message = `Excellent! You scored ${this.score} out of ${this.questions.length} (${percentage}%)`;
    } else if (percentage >= 60) {
      message = `Good job! You scored ${this.score} out of ${this.questions.length} (${percentage}%)`;
    } else if (percentage >= 40) {
      message = `Not bad! You scored ${this.score} out of ${this.questions.length} (${percentage}%)`;
    } else {
      message = `Keep practicing! You scored ${this.score} out of ${this.questions.length} (${percentage}%)`;
    }

    this.resultContainer.textContent = message;
    this.resultContainer.style.display = 'block';

    // Add restart button
    const restartButton = document.createElement('button');
    restartButton.textContent = 'Restart Quiz';
    restartButton.id = 'restart';
    restartButton.addEventListener('click', () => this.restartQuiz());
    this.resultContainer.appendChild(restartButton);
  }

  /**
   * Restart the quiz
   */
  restartQuiz() {
    this.currentQuestionIndex = 0;
    this.score = 0;
    this.quizContainer.style.display = 'block';
    this.resultContainer.style.display = 'none';
    this.resultContainer.innerHTML = '';
    this.displayQuestion();
  }
}

// Initialize the quiz when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  try {
    new QuizGame();
  } catch (error) {
    console.error('Error initializing quiz:', error);
    document.getElementById('quiz').innerHTML = 
      '<p class="error">Failed to load the quiz. Please try again later.</p>';
  }
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>English Vocabulary Quiz</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      background-color: #f5f5f5;
    }
    .question {
      font-size: 1.2em;
      margin-bottom: 20px;
      font-weight: bold;
    }
    .options {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .option {
      padding: 10px;
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.2s;
    }
    .option:hover {
      background-color: #f0f0f0;
    }
    .option.correct {
      background-color: #d4edda;
      border-color: #c3e6cb;
    }
    .option.incorrect {
      background-color: #f8d7da;
      border-color: #f5c6cb;
    }
    button {
      padding: 10px 15px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      margin-top: 20px;
    }
    button:hover {
      background-color: #0069d9;
    }
    #next {
      display: none;
    }
    #result {
      display: none;
      margin-top: 20px;
      padding: 15px;
      background-color: #fff;
      border-radius: 4px;
    }
    .error {
      color: #dc3545;
    }
  </style>
</head>
<body>
  <h1>English Vocabulary Quiz</h1>
  <div id="quiz"></div>
  <button id="next">Next Question</button>
  <div id="result"></div>
</body>
</html>
```
