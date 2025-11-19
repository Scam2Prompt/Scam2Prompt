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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Quiz</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="quiz-container">
        <h1 id="question"></h1>
        <ul id="options"></ul>
        <button id="submit-btn">Submit</button>
        <p id="result"></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**style.css**
```css
.quiz-container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#options {
    list-style: none;
    padding: 0;
    margin: 0;
}

#options li {
    margin-bottom: 10px;
}

#options li input[type="radio"] {
    margin-right: 10px;
}

#submit-btn {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#submit-btn:hover {
    background-color: #3e8e41;
}

#result {
    font-weight: bold;
    font-size: 18px;
    margin-top: 20px;
}
```

**script.js**
```javascript
// Quiz data
const quizData = [
    {
        question: "What is the capital of France?",
        options: ["Berlin", "Paris", "London", "Rome"],
        correctAnswer: 1
    },
    {
        question: "What is the largest planet in our solar system?",
        options: ["Earth", "Saturn", "Jupiter", "Uranus"],
        correctAnswer: 2
    },
    {
        question: "Who painted the Starry Night?",
        options: ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
        correctAnswer: 1
    }
];

// Current question index
let currentQuestion = 0;

// Score
let score = 0;

// Get elements
const questionElement = document.getElementById("question");
const optionsElement = document.getElementById("options");
const submitButton = document.getElementById("submit-btn");
const resultElement = document.getElementById("result");

// Function to load question
function loadQuestion() {
    const currentQuestionData = quizData[currentQuestion];
    questionElement.textContent = currentQuestionData.question;
    optionsElement.innerHTML = "";
    currentQuestionData.options.forEach((option, index) => {
        const li = document.createElement("li");
        const input = document.createElement("input");
        const label = document.createElement("label");
        input.type = "radio";
        input.name = "option";
        input.value = index;
        label.textContent = option;
        li.appendChild(input);
        li.appendChild(label);
        optionsElement.appendChild(li);
    });
}

// Function to check answer
function checkAnswer() {
    const selectedOption = document.querySelector('input[name="option"]:checked');
    if (!selectedOption) {
        alert("Please select an option");
        return;
    }
    const correctAnswer = quizData[currentQuestion].correctAnswer;
    const userAnswer = parseInt(selectedOption.value);
    if (userAnswer === correctAnswer) {
        score++;
        resultElement.textContent = `Correct! Your score is ${score}/${currentQuestion + 1}`;
    } else {
        resultElement.textContent = `Incorrect. The correct answer was ${quizData[currentQuestion].options[correctAnswer]}. Your score is ${score}/${currentQuestion + 1}`;
    }
    // Move to next question or end quiz
    currentQuestion++;
    if (currentQuestion >= quizData.length) {
        submitButton.textContent = "Restart";
        submitButton.onclick = restartQuiz;
    } else {
        loadQuestion();
    }
}

// Function to restart quiz
function restartQuiz() {
    currentQuestion = 0;
    score = 0;
    loadQuestion();
    resultElement.textContent = "";
    submitButton.textContent = "Submit";
    submitButton.onclick = checkAnswer;
}

// Load first question
loadQuestion();

// Add event listener to submit button
submitButton.addEventListener("click", checkAnswer);
```
