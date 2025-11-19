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
// Interactive Quiz Game for Children
// This code creates a simple quiz game where children can answer multiple-choice questions.
// The game is designed to be fun and educational.

document.addEventListener("DOMContentLoaded", () => {
  // Array of quiz questions
  const quizQuestions = [
    {
      question: "What is the color of the sky?",
      options: ["Blue", "Green", "Red", "Yellow"],
      correctAnswer: 0, // Index of the correct answer
    },
    {
      question: "How many legs does a spider have?",
      options: ["6", "8", "4", "10"],
      correctAnswer: 1,
    },
    {
      question: "Which animal is known as the king of the jungle?",
      options: ["Elephant", "Lion", "Tiger", "Bear"],
      correctAnswer: 1,
    },
  ];

  let currentQuestionIndex = 0;
  let score = 0;

  // DOM Elements
  const questionContainer = document.getElementById("question-container");
  const questionText = document.getElementById("question-text");
  const optionsContainer = document.getElementById("options-container");
  const scoreDisplay = document.getElementById("score-display");
  const nextButton = document.getElementById("next-button");

  // Function to load a question
  function loadQuestion() {
    const currentQuestion = quizQuestions[currentQuestionIndex];
    questionText.textContent = currentQuestion.question;
    optionsContainer.innerHTML = ""; // Clear previous options

    currentQuestion.options.forEach((option, index) => {
      const button = document.createElement("button");
      button.textContent = option;
      button.classList.add("option-button");
      button.addEventListener("click", () => handleAnswer(index));
      optionsContainer.appendChild(button);
    });
  }

  // Function to handle answer selection
  function handleAnswer(selectedIndex) {
    const currentQuestion = quizQuestions[currentQuestionIndex];
    if (selectedIndex === currentQuestion.correctAnswer) {
      score++;
      alert("Correct! Great job!");
    } else {
      alert("Oops! That's not correct. Try the next one!");
    }
    nextButton.disabled = false; // Enable the "Next" button
  }

  // Function to move to the next question
  function nextQuestion() {
    currentQuestionIndex++;
    if (currentQuestionIndex < quizQuestions.length) {
      loadQuestion();
      nextButton.disabled = true; // Disable the "Next" button until an answer is selected
    } else {
      endQuiz();
    }
  }

  // Function to end the quiz
  function endQuiz() {
    questionContainer.innerHTML = `<h2>Quiz Completed!</h2>`;
    scoreDisplay.textContent = `Your final score is: ${score}/${quizQuestions.length}`;
    nextButton.style.display = "none"; // Hide the "Next" button
  }

  // Initialize the quiz
  loadQuestion();
  nextButton.addEventListener("click", nextQuestion);
});
```

```html
<!-- HTML Structure for the Quiz Game -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Interactive Quiz Game</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 20px;
    }
    #question-container {
      margin-bottom: 20px;
    }
    .option-button {
      display: block;
      margin: 10px auto;
      padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    .option-button:hover {
      background-color: #45a049;
    }
    #next-button {
      padding: 10px 20px;
      background-color: #008CBA;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    #next-button:disabled {
      background-color: #cccccc;
      cursor: not-allowed;
    }
  </style>
</head>
<body>
  <div id="question-container">
    <h1 id="question-text">Question will appear here</h1>
    <div id="options-container"></div>
  </div>
  <button id="next-button" disabled>Next Question</button>
  <h2 id="score-display">Your score will appear here</h2>
  <script src="quiz.js"></script>
</body>
</html>
```
