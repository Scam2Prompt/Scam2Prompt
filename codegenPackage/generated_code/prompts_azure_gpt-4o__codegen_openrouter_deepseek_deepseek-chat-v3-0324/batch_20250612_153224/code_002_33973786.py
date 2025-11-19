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
/**
 * Quiz Application for "Vivir es Convivir" Educational Program
 * 
 * This application presents a quiz about responsibility and equality values
 * tailored for children. It includes multiple-choice questions with feedback,
 * scoring, and progress tracking.
 */

class QuizApp {
  constructor() {
    this.questions = [
      {
        id: 1,
        text: "What does it mean to be responsible?",
        options: [
          { id: 1, text: "Doing your homework on time" },
          { id: 2, text: "Helping with household chores" },
          { id: 3, text: "Taking care of your belongings" },
          { id: 4, text: "All of the above" }
        ],
        correctAnswer: 4,
        feedback: "Being responsible means doing all these things and more!"
      },
      {
        id: 2,
        text: "If you see a classmate being treated unfairly, what should you do?",
        options: [
          { id: 1, text: "Ignore it" },
          { id: 2, text: "Tell a teacher or adult" },
          { id: 3, text: "Join in the unfair treatment" },
          { id: 4, text: "Laugh about it" }
        ],
        correctAnswer: 2,
        feedback: "Standing up for equality means speaking up when someone is treated unfairly."
      },
      {
        id: 3,
        text: "How can we show equality in our classroom?",
        options: [
          { id: 1, text: "Include everyone in games" },
          { id: 2, text: "Share materials equally" },
          { id: 3, text: "Listen to everyone's ideas" },
          { id: 4, text: "All of the above" }
        ],
        correctAnswer: 4,
        feedback: "Great job! Equality means treating everyone fairly in all situations."
      }
    ];
    
    this.currentQuestionIndex = 0;
    this.score = 0;
    this.quizContainer = document.getElementById('quiz-container');
    this.resultContainer = document.getElementById('result-container');
    this.nextButton = document.getElementById('next-btn');
    this.restartButton = document.getElementById('restart-btn');
    
    this.initialize();
  }
  
  initialize() {
    this.nextButton.addEventListener('click', () => this.nextQuestion());
    this.restartButton.addEventListener('click', () => this.restartQuiz());
    this.showQuestion();
  }
  
  showQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      this.showResults();
      return;
    }
    
    const question = this.questions[this.currentQuestionIndex];
    let optionsHTML = '';
    
    question.options.forEach(option => {
      optionsHTML += `
        <div class="option">
          <input type="radio" name="question-${question.id}" id="option-${option.id}" value="${option.id}">
          <label for="option-${option.id}">${option.text}</label>
        </div>
      `;
    });
    
    this.quizContainer.innerHTML = `
      <div class="question">
        <h3>Question ${this.currentQuestionIndex + 1} of ${this.questions.length}</h3>
        <p>${question.text}</p>
        <div class="options">${optionsHTML}</div>
      </div>
    `;
    
    this.resultContainer.innerHTML = '';
    this.nextButton.style.display = 'block';
  }
  
  checkAnswer() {
    const question = this.questions[this.currentQuestionIndex];
    const selectedOption = document.querySelector(`input[name="question-${question.id}"]:checked`);
    
    if (!selectedOption) {
      alert('Please select an answer!');
      return false;
    }
    
    const selectedAnswer = parseInt(selectedOption.value);
    const isCorrect = selectedAnswer === question.correctAnswer;
    
    if (isCorrect) {
      this.score++;
    }
    
    this.resultContainer.innerHTML = `
      <div class="feedback ${isCorrect ? 'correct' : 'incorrect'}">
        <p>${isCorrect ? 'Correct!' : 'Incorrect!'}</p>
        <p>${question.feedback}</p>
      </div>
    `;
    
    return true;
  }
  
  nextQuestion() {
    if (this.checkAnswer()) {
      this.currentQuestionIndex++;
      
      if (this.currentQuestionIndex < this.questions.length) {
        this.showQuestion();
      } else {
        this.showResults();
      }
    }
  }
  
  showResults() {
    this.quizContainer.innerHTML = `
      <div class="results">
        <h2>Quiz Completed!</h2>
        <p>Your score: ${this.score} out of ${this.questions.length}</p>
        <p>${this.getEncouragementMessage()}</p>
      </div>
    `;
    
    this.nextButton.style.display = 'none';
    this.restartButton.style.display = 'block';
  }
  
  getEncouragementMessage() {
    const percentage = (this.score / this.questions.length) * 100;
    
    if (percentage >= 80) {
      return "Excellent! You understand responsibility and equality very well!";
    } else if (percentage >= 50) {
      return "Good job! You're learning about these important values!";
    } else {
      return "Keep practicing! Responsibility and equality are important for living together.";
    }
  }
  
  restartQuiz() {
    this.currentQuestionIndex = 0;
    this.score = 0;
    this.showQuestion();
    this.restartButton.style.display = 'none';
  }
}

// Initialize the quiz when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  new QuizApp();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vivir es Convivir - Values Quiz</title>
  <style>
    body {
      font-family: 'Comic Sans MS', cursive, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      background-color: #f0f8ff;
      color: #333;
    }
    h1 {
      color: #2e8b57;
      text-align: center;
    }
    .question {
      background-color: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      margin-bottom: 20px;
    }
    .options {
      margin-top: 15px;
    }
    .option {
      margin: 10px 0;
      padding: 10px;
      background-color: #e6f7ff;
      border-radius: 5px;
    }
    .option:hover {
      background-color: #cceeff;
    }
    input[type="radio"] {
      margin-right: 10px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 10px 20px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 10px 2px;
      cursor: pointer;
      border-radius: 5px;
    }
    button:hover {
      background-color: #45a049;
    }
    .feedback {
      padding: 15px;
      margin-top: 20px;
      border-radius: 5px;
    }
    .correct {
      background-color: #dff0d8;
      color: #3c763d;
    }
    .incorrect {
      background-color: #f2dede;
      color: #a94442;
    }
    .results {
      text-align: center;
      background-color: white;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    #restart-btn {
      display: none;
      background-color: #337ab7;
    }
    #restart-btn:hover {
      background-color: #286090;
    }
  </style>
</head>
<body>
  <h1>Vivir es Convivir - Values Quiz</h1>
  <div id="quiz-container"></div>
  <div id="result-container"></div>
  <button id="next-btn">Next Question</button>
  <button id="restart-btn">Restart Quiz</button>
  
  <script src="quiz.js"></script>
</body>
</html>
```
