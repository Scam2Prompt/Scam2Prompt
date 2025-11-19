"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Write a JavaScript code to create an interactive quiz for students in کارو دانش schools, covering topics from various subjects.
Generated: DETERMINISTIC_179356775d42987d
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Quiz Application for کارو دانش Schools
class Quiz {
  constructor(questions) {
    this.questions = questions;
    this.currentQuestionIndex = 0;
    this.score = 0;
    this.timeLeft = 0;
    this.timer = null;
    this.quizDuration = 60; // seconds
  }

  // Initialize quiz
  init() {
    this.displayQuestion();
    this.startTimer();
    document.getElementById('next-btn').addEventListener('click', () => this.nextQuestion());
    document.getElementById('submit-btn').addEventListener('click', () => this.submitQuiz());
  }

  // Display current question
  displayQuestion() {
    const currentQuestion = this.questions[this.currentQuestionIndex];
    const questionElement = document.getElementById('question');
    const optionsElement = document.getElementById('options');
    const progressElement = document.getElementById('progress');

    questionElement.textContent = currentQuestion.question;
    optionsElement.innerHTML = '';

    currentQuestion.options.forEach((option, index) => {
      const optionElement = document.createElement('div');
      optionElement.className = 'option';
      optionElement.textContent = option;
      optionElement.addEventListener('click', () => this.selectOption(index));
      optionsElement.appendChild(optionElement);
    });

    progressElement.textContent = `سوال ${this.currentQuestionIndex + 1} از ${this.questions.length}`;
  }

  // Select an option
  selectOption(optionIndex) {
    const options = document.querySelectorAll('.option');
    options.forEach(option => option.classList.remove('selected'));
    options[optionIndex].classList.add('selected');
  }

  // Move to next question
  nextQuestion() {
    const selectedOption = document.querySelector('.option.selected');
    if (!selectedOption && this.questions[this.currentQuestionIndex].required) {
      alert('لطفاً یک گزینه را انتخاب کنید!');
      return;
    }

    if (selectedOption) {
      const selectedIndex = Array.from(document.querySelectorAll('.option')).indexOf(selectedOption);
      this.checkAnswer(selectedIndex);
    }

    this.currentQuestionIndex++;
    if (this.currentQuestionIndex < this.questions.length) {
      this.displayQuestion();
    } else {
      this.endQuiz();
    }
  }

  // Check if answer is correct
  checkAnswer(selectedIndex) {
    const currentQuestion = this.questions[this.currentQuestionIndex];
    if (selectedIndex === currentQuestion.correctAnswer) {
      this.score++;
    }
  }

  // Start quiz timer
  startTimer() {
    this.timeLeft = this.quizDuration;
    document.getElementById('time').textContent = this.formatTime(this.timeLeft);
    
    this.timer = setInterval(() => {
      this.timeLeft--;
      document.getElementById('time').textContent = this.formatTime(this.timeLeft);
      
      if (this.timeLeft <= 0) {
        clearInterval(this.timer);
        this.endQuiz();
      }
    }, 1000);
  }

  // Format time as MM:SS
  formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  }

  // Submit quiz
  submitQuiz() {
    if (confirm('آیا مطمئن هستید که می‌خواهید آزمون را تمام کنید؟')) {
      this.endQuiz();
    }
  }

  // End quiz and show results
  endQuiz() {
    clearInterval(this.timer);
    document.getElementById('quiz-container').style.display = 'none';
    document.getElementById('result-container').style.display = 'block';
    
    const resultElement = document.getElementById('result');
    const percentage = Math.round((this.score / this.questions.length) * 100);
    
    resultElement.innerHTML = `
      <h2>نتیجه آزمون</h2>
      <p>شما ${this.score} از ${this.questions.length} سوال را صحیح پاسخ دادید.</p>
      <p>درصد شما: ${percentage}%</p>
      ${percentage >= 70 ? '<p class="success">تبریک! شما قبول شدید.</p>' : '<p class="fail">متأسفانه قبول نشدید.</p>'}
    `;
  }
}

// Sample questions (can be loaded from API in production)
const questions = [
  {
    question: "کدام یک از موارد زیر یک ماده معدنی است؟",
    options: ["آهن", "پلاستیک", "چوب", "نایلون"],
    correctAnswer: 0,
    required: true
  },
  {
    question: "در مثلث قائم‌الزاویه، وتر مقابل کدام زاویه است؟",
    options: ["زاویه قائمه", "زاویه حاده", "زاویه منفرجه", "هیچکدام"],
    correctAnswer: 0,
    required: true
  },
  {
    question: "کدام گزینه در مورد الکتریسیته صحیح است؟",
    options: [
      "جریان الکتریکی از مثبت به منفی است",
      "جریان الکتریکی از منفی به مثبت است",
      "الکتریسیته فقط در فلزات وجود دارد",
      "الکتریسیته نوعی انرژی شیمیایی است"
    ],
    correctAnswer: 0,
    required: true
  }
];

// Initialize quiz when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const quiz = new Quiz(questions);
  quiz.init();
});

// HTML Structure (would be in separate file in production)
/*
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>آزمون کارو دانش</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 20px;
      background-color: #f5f5f5;
    }
    .container {
      max-width: 800px;
      margin: 0 auto;
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    #question {
      font-size: 1.2em;
      margin-bottom: 20px;
      font-weight: bold;
    }
    .option {
      padding: 10px;
      margin: 5px 0;
      background: #f0f0f0;
      border-radius: 4px;
      cursor: pointer;
    }
    .option:hover {
      background: #e0e0e0;
    }
    .option.selected {
      background: #4CAF50;
      color: white;
    }
    .controls {
      margin-top: 20px;
      display: flex;
      justify-content: space-between;
    }
    button {
      padding: 10px 20px;
      background: #4CAF50;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background: #45a049;
    }
    #progress, #time {
      font-weight: bold;
    }
    #result-container {
      display: none;
    }
    .success {
      color: #4CAF50;
    }
    .fail {
      color: #f44336;
    }
  </style>
</head>
<body>
  <div class="container">
    <div id="quiz-container">
      <div id="progress"></div>
      <div id="time"></div>
      <div id="question"></div>
      <div id="options"></div>
      <div class="controls">
        <button id="submit-btn">پایان آزمون</button>
        <button id="next-btn">سوال بعدی</button>
      </div>
    </div>
    <div id="result-container">
      <div id="result"></div>
    </div>
  </div>
  <script src="quiz.js"></script>
</body>
</html>
*/
```
