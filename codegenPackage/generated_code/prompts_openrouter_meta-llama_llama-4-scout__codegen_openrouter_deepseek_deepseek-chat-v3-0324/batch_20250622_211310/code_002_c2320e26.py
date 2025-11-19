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
/**
 * Financial Literacy Quiz
 * A simple quiz application covering investment strategies and risk management.
 */

// Quiz questions with options and correct answers
const quizQuestions = [
  {
    question: "What is the primary purpose of diversification in investing?",
    options: [
      "To maximize returns on a single investment",
      "To reduce risk by spreading investments across different assets",
      "To avoid paying taxes on investment gains",
      "To invest only in high-risk assets"
    ],
    correctAnswer: 1 // Index of the correct option
  },
  {
    question: "Which of these is considered a low-risk investment?",
    options: [
      "Cryptocurrency",
      "Government bonds",
      "Penny stocks",
      "Futures contracts"
    ],
    correctAnswer: 1
  },
  {
    question: "What does 'compound interest' mean?",
    options: [
      "Interest calculated only on the principal amount",
      "Interest calculated on both the principal and accumulated interest",
      "Interest that decreases over time",
      "Interest paid only at maturity"
    ],
    correctAnswer: 1
  },
  {
    question: "What is an emergency fund typically used for?",
    options: [
      "Investing in high-growth stocks",
      "Paying for unexpected expenses or financial emergencies",
      "Funding luxury purchases",
      "Paying down high-interest debt"
    ],
    correctAnswer: 1
  },
  {
    question: "Which of these is NOT a good strategy for risk management?",
    options: [
      "Setting stop-loss orders",
      "Investing all your money in a single stock",
      "Maintaining an emergency fund",
      "Regularly rebalancing your portfolio"
    ],
    correctAnswer: 1
  }
];

// Quiz state variables
let currentQuestionIndex = 0;
let score = 0;

// DOM elements
const quizContainer = document.getElementById('quiz-container');
const questionElement = document.getElementById('question');
const optionsContainer = document.getElementById('options-container');
const nextButton = document.getElementById('next-button');
const resultContainer = document.getElementById('result-container');
const scoreElement = document.getElementById('score');

/**
 * Display the current question and options
 */
function displayQuestion() {
  if (currentQuestionIndex >= quizQuestions.length) {
    showResults();
    return;
  }

  const currentQuestion = quizQuestions[currentQuestionIndex];
  questionElement.textContent = currentQuestion.question;
  
  // Clear previous options
  optionsContainer.innerHTML = '';
  
  // Add new options
  currentQuestion.options.forEach((option, index) => {
    const optionButton = document.createElement('button');
    optionButton.textContent = option;
    optionButton.classList.add('option');
    optionButton.addEventListener('click', () => selectOption(index));
    optionsContainer.appendChild(optionButton);
  });

  // Update progress
  document.getElementById('progress').textContent = 
    `Question ${currentQuestionIndex + 1} of ${quizQuestions.length}`;
}

/**
 * Handle option selection
 * @param {number} selectedIndex - Index of the selected option
 */
function selectOption(selectedIndex) {
  const currentQuestion = quizQuestions[currentQuestionIndex];
  
  // Disable all options after selection
  const options = document.querySelectorAll('.option');
  options.forEach(option => {
    option.disabled = true;
    option.classList.remove('selected');
  });

  // Highlight selected option
  options[selectedIndex].classList.add('selected');

  // Check if answer is correct
  if (selectedIndex === currentQuestion.correctAnswer) {
    options[selectedIndex].classList.add('correct');
    score++;
  } else {
    options[selectedIndex].classList.add('incorrect');
    // Highlight correct answer
    options[currentQuestion.correctAnswer].classList.add('correct');
  }

  // Enable next button
  nextButton.disabled = false;
}

/**
 * Move to the next question or show results
 */
function nextQuestion() {
  currentQuestionIndex++;
  nextButton.disabled = true;
  displayQuestion();
}

/**
 * Display quiz results
 */
function showResults() {
  quizContainer.style.display = 'none';
  resultContainer.style.display = 'block';
  scoreElement.textContent = `${score} out of ${quizQuestions.length}`;
}

/**
 * Reset the quiz to initial state
 */
function resetQuiz() {
  currentQuestionIndex = 0;
  score = 0;
  resultContainer.style.display = 'none';
  quizContainer.style.display = 'block';
  nextButton.disabled = true;
  displayQuestion();
}

// Initialize the quiz
document.addEventListener('DOMContentLoaded', () => {
  displayQuestion();
  nextButton.addEventListener('click', nextQuestion);
  document.getElementById('reset-button').addEventListener('click', resetQuiz);
});
```

HTML template to use with this code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Financial Literacy Quiz</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
    }
    .option {
      display: block;
      width: 100%;
      padding: 10px;
      margin: 5px 0;
      text-align: left;
      cursor: pointer;
    }
    .selected {
      font-weight: bold;
    }
    .correct {
      background-color: #d4edda;
    }
    .incorrect {
      background-color: #f8d7da;
    }
    #next-button {
      margin-top: 20px;
      padding: 10px 20px;
    }
    #result-container {
      display: none;
    }
  </style>
</head>
<body>
  <h1>Financial Literacy Quiz</h1>
  
  <div id="quiz-container">
    <div id="progress"></div>
    <h2 id="question"></h2>
    <div id="options-container"></div>
    <button id="next-button" disabled>Next Question</button>
  </div>
  
  <div id="result-container">
    <h2>Quiz Completed!</h2>
    <p>Your score: <span id="score"></span></p>
    <button id="reset-button">Take Quiz Again</button>
  </div>

  <script src="quiz.js"></script>
</body>
</html>
```
