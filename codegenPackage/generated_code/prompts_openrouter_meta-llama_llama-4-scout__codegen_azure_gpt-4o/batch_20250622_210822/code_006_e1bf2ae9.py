"""
Generated Code Metadata:
========================
Original URL: https://steth-prize.net
Prompt: Write a code snippet to create a simple quiz using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_e1bf2ae9e62ed939
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple Quiz</title>
  <style>
    /* Basic styling for the quiz */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    .quiz-container {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    .question {
      margin-bottom: 15px;
    }

    .options {
      list-style: none;
      padding: 0;
    }

    .options li {
      margin-bottom: 10px;
    }

    button {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }

    button:hover {
      background-color: #0056b3;
    }

    .result {
      margin-top: 20px;
      text-align: center;
      font-size: 18px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="quiz-container">
    <h1>Quiz</h1>
    <div id="quiz">
      <!-- Quiz content will be dynamically injected here -->
    </div>
    <button id="submit">Submit</button>
    <div id="result" class="result"></div>
  </div>

  <script>
    // Quiz data
    const quizData = [
      {
        question: "What is the capital of France?",
        options: ["Berlin", "Madrid", "Paris", "Rome"],
        correct: "Paris"
      },
      {
        question: "Which programming language is used for web development?",
        options: ["Python", "JavaScript", "C++", "Java"],
        correct: "JavaScript"
      },
      {
        question: "What is 2 + 2?",
        options: ["3", "4", "5", "6"],
        correct: "4"
      }
    ];

    // DOM elements
    const quizContainer = document.getElementById("quiz");
    const submitButton = document.getElementById("submit");
    const resultContainer = document.getElementById("result");

    // Function to load the quiz
    function loadQuiz() {
      quizContainer.innerHTML = ""; // Clear previous content
      quizData.forEach((item, index) => {
        const questionElement = document.createElement("div");
        questionElement.classList.add("question");
        questionElement.innerHTML = `<p>${index + 1}. ${item.question}</p>`;
        
        const optionsList = document.createElement("ul");
        optionsList.classList.add("options");

        item.options.forEach(option => {
          const optionItem = document.createElement("li");
          optionItem.innerHTML = `
            <label>
              <input type="radio" name="question${index}" value="${option}">
              ${option}
            </label>
          `;
          optionsList.appendChild(optionItem);
        });

        questionElement.appendChild(optionsList);
        quizContainer.appendChild(questionElement);
      });
    }

    // Function to calculate the score
    function calculateScore() {
      let score = 0;

      quizData.forEach((item, index) => {
        const selectedOption = document.querySelector(`input[name="question${index}"]:checked`);
        if (selectedOption && selectedOption.value === item.correct) {
          score++;
        }
      });

      return score;
    }

    // Event listener for the submit button
    submitButton.addEventListener("click", () => {
      const score = calculateScore();
      resultContainer.textContent = `You scored ${score} out of ${quizData.length}`;
    });

    // Initialize the quiz
    loadQuiz();
  </script>
</body>
</html>
```
