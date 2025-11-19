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
// quizGame.js

/**
 * A simple interactive quiz game for children.
 */

// Game configuration
const quizConfig = {
  questions: [
    {
      question: "What is the capital of Sri Lanka?",
      options: ["Colombo", "Kandy", "Galle", "Jaffna"],
      correctAnswer: 0,
    },
    {
      question: "What is the largest planet in our solar system?",
      options: ["Earth", "Saturn", "Jupiter", "Uranus"],
      correctAnswer: 2,
    },
    {
      question: "Who painted the Mona Lisa?",
      options: ["Leonardo da Vinci", "Michelangelo", "Raphael", "Caravaggio"],
      correctAnswer: 0,
    },
  ],
  score: 0,
  currentQuestion: 0,
};

// Function to display the current question
function displayQuestion() {
  const currentQuestion = quizConfig.questions[quizConfig.currentQuestion];
  document.getElementById("question").innerText = currentQuestion.question;
  const optionsHtml = currentQuestion.options.map((option, index) => {
    return `
      <li>
        <input type="radio" id="option-${index}" name="option" value="${index}">
        <label for="option-${index}">${option}</label>
      </li>
    `;
  }).join("");
  document.getElementById("options").innerHTML = optionsHtml;
}

// Function to check the answer
function checkAnswer() {
  const currentQuestion = quizConfig.questions[quizConfig.currentQuestion];
  const selectedOption = document.querySelector('input[name="option"]:checked');
  if (!selectedOption) {
    alert("Please select an option");
    return;
  }
  const userAnswer = parseInt(selectedOption.value);
  if (userAnswer === currentQuestion.correctAnswer) {
    quizConfig.score++;
    document.getElementById("feedback").innerText = "Correct!";
  } else {
    document.getElementById("feedback").innerText = `Incorrect. The correct answer is ${currentQuestion.options[currentQuestion.correctAnswer]}`;
  }
  document.getElementById("score").innerText = `Score: ${quizConfig.score} / ${quizConfig.currentQuestion + 1}`;
  quizConfig.currentQuestion++;
  if (quizConfig.currentQuestion >= quizConfig.questions.length) {
    endGame();
  } else {
    displayQuestion();
  }
}

// Function to end the game
function endGame() {
  document.getElementById("question").innerText = "Game Over!";
  document.getElementById("options").innerHTML = "";
  document.getElementById("feedback").innerText = "";
  document.getElementById("score").innerText = `Final Score: ${quizConfig.score} / ${quizConfig.questions.length}`;
  document.getElementById("play-again").style.display = "block";
}

// Function to play again
function playAgain() {
  quizConfig.score = 0;
  quizConfig.currentQuestion = 0;
  displayQuestion();
  document.getElementById("question").innerText = "";
  document.getElementById("feedback").innerText = "";
  document.getElementById("score").innerText = "";
  document.getElementById("play-again").style.display = "none";
}

// Initialize the game
document.addEventListener("DOMContentLoaded", () => {
  displayQuestion();
  document.getElementById("submit").addEventListener("click", checkAnswer);
  document.getElementById("play-again").addEventListener("click", playAgain);
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz Game</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    #options {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    #options li {
      margin-bottom: 10px;
    }
    #play-again {
      display: none;
    }
  </style>
</head>
<body>
  <h1>Quiz Game</h1>
  <p id="question"></p>
  <ul id="options"></ul>
  <p id="feedback"></p>
  <p id="score"></p>
  <button id="submit">Submit</button>
  <button id="play-again">Play Again</button>

  <script src="quizGame.js"></script>
</body>
</html>
```
