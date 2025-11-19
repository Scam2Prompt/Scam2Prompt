"""
Generated Code Metadata:
========================
Original URL: https://ssdsd.netlify.app
Prompt: Write a code snippet in JavaScript to create an interactive quiz for 상일미디어고 students, specifically for the 환경 (Environmental Science) subject.
Generated: DETERMINISTIC_98b55ed06d0eb81f
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Environmental Science Quiz for Sangil Media High School Students
 * 
 * Features:
 * - Multiple-choice questions
 * - Score tracking
 * - Feedback for correct/incorrect answers
 * - Timer functionality
 */

class EnvironmentalScienceQuiz {
  constructor() {
    this.questions = [
      {
        question: "Which of the following is a renewable energy source?",
        options: ["Coal", "Natural Gas", "Solar Power", "Nuclear Power"],
        answer: 2
      },
      {
        question: "What is the primary cause of acid rain?",
        options: ["CO2 emissions", "SO2 and NOx emissions", "Methane emissions", "Ozone depletion"],
        answer: 1
      },
      {
        question: "Which ecosystem has the highest biodiversity?",
        options: ["Desert", "Tundra", "Tropical Rainforest", "Grassland"],
        answer: 2
      },
      {
        question: "What does the '3Rs' in environmental science stand for?",
        options: [
          "Reduce, Reuse, Recycle",
          "Read, Remember, Repeat",
          "Reduce, Rebuild, Restore",
          "Reclaim, Reuse, Replenish"
        ],
        answer: 0
      },
      {
        question: "Which gas is primarily responsible for global warming?",
        options: ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"],
        answer: 2
      }
    ];
    
    this.currentQuestionIndex = 0;
    this.score = 0;
    this.timeLeft = 60;
    this.timer = null;
    this.quizCompleted = false;
  }

  startQuiz() {
    this.displayQuestion();
    this.startTimer();
    document.getElementById('start-btn').disabled = true;
  }

  displayQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      this.endQuiz();
      return;
    }

    const currentQuestion = this.questions[this.currentQuestionIndex];
    const quizContainer = document.getElementById('quiz-container');
    
    quizContainer.innerHTML = `
      <div class="question">${currentQuestion.question}</div>
      <div class="options">
        ${currentQuestion.options.map((option, index) => `
          <button class="option-btn" onclick="quiz.selectOption(${index})">
            ${option}
          </button>
        `).join('')}
      </div>
      <div class="feedback" id="feedback"></div>
    `;
  }

  selectOption(selectedIndex) {
    if (this.quizCompleted) return;

    const currentQuestion = this.questions[this.currentQuestionIndex];
    const feedbackElement = document.getElementById('feedback');

    if (selectedIndex === currentQuestion.answer) {
      this.score++;
      feedbackElement.innerHTML = "<p class='correct'>Correct! Well done!</p>";
    } else {
      feedbackElement.innerHTML = `
        <p class='incorrect'>Incorrect. The correct answer is: ${currentQuestion.options[currentQuestion.answer]}</p>
      `;
    }

    setTimeout(() => {
      this.currentQuestionIndex++;
      this.displayQuestion();
    }, 1500);
  }

  startTimer() {
    this.timer = setInterval(() => {
      this.timeLeft--;
      document.getElementById('time').textContent = this.timeLeft;

      if (this.timeLeft <= 0) {
        clearInterval(this.timer);
        this.endQuiz();
      }
    }, 1000);
  }

  endQuiz() {
    clearInterval(this.timer);
    this.quizCompleted = true;
    
    const quizContainer = document.getElementById('quiz-container');
    quizContainer.innerHTML = `
      <h2>Quiz Completed!</h2>
      <p>Your score: ${this.score} out of ${this.questions.length}</p>
      <p>Percentage: ${Math.round((this.score / this.questions.length) * 100)}%</p>
      <button onclick="quiz.resetQuiz()">Try Again</button>
    `;
  }

  resetQuiz() {
    this.currentQuestionIndex = 0;
    this.score = 0;
    this.timeLeft = 60;
    this.quizCompleted = false;
    document.getElementById('start-btn').disabled = false;
    document.getElementById('quiz-container').innerHTML = '';
    document.getElementById('time').textContent = this.timeLeft;
  }
}

// Initialize quiz
const quiz = new EnvironmentalScienceQuiz();

// HTML structure (would be in a separate file in production)
document.body.innerHTML = `
  <div class="quiz-app">
    <h1>Environmental Science Quiz</h1>
    <p>Time left: <span id="time">60</span> seconds</p>
    <button id="start-btn" onclick="quiz.startQuiz()">Start Quiz</button>
    <div id="quiz-container"></div>
  </div>
  
  <style>
    .quiz-app {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      font-family: Arial, sans-serif;
      text-align: center;
    }
    .question {
      font-size: 1.2em;
      margin: 20px 0;
      font-weight: bold;
    }
    .options {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .option-btn {
      padding: 10px;
      background: #f0f0f0;
      border: 1px solid #ddd;
      border-radius: 5px;
      cursor: pointer;
      transition: background 0.3s;
    }
    .option-btn:hover {
      background: #e0e0e0;
    }
    .feedback {
      margin: 20px 0;
      min-height: 50px;
    }
    .correct {
      color: green;
    }
    .incorrect {
      color: red;
    }
    #start-btn {
      padding: 10px 20px;
      background: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 1em;
    }
    #start-btn:hover {
      background: #45a049;
    }
    #start-btn:disabled {
      background: #cccccc;
      cursor: not-allowed;
    }
  </style>
`;
```
