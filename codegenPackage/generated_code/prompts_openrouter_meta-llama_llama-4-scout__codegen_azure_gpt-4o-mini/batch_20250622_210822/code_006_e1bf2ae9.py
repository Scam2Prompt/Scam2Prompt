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
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .quiz-container {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .question {
            margin-bottom: 15px;
        }
        .options {
            list-style-type: none;
            padding: 0;
        }
        .options li {
            margin: 5px 0;
        }
        button {
            padding: 10px 15px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .result {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="quiz-container">
    <h1>Simple Quiz</h1>
    <div class="question" id="question"></div>
    <ul class="options" id="options"></ul>
    <button id="submit">Submit</button>
    <div class="result" id="result"></div>
</div>

<script>
    // Quiz questions and answers
    const quizData = [
        {
            question: "What is the capital of France?",
            options: ["Berlin", "Madrid", "Paris", "Lisbon"],
            answer: "Paris"
        },
        {
            question: "Which planet is known as the Red Planet?",
            options: ["Earth", "Mars", "Jupiter", "Saturn"],
            answer: "Mars"
        },
        {
            question: "What is the largest ocean on Earth?",
            options: ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            answer: "Pacific Ocean"
        }
    ];

    let currentQuestionIndex = 0;
    let score = 0;

    // Function to load the current question
    function loadQuestion() {
        const currentQuestion = quizData[currentQuestionIndex];
        document.getElementById('question').innerText = currentQuestion.question;
        const optionsList = document.getElementById('options');
        optionsList.innerHTML = ''; // Clear previous options

        currentQuestion.options.forEach(option => {
            const li = document.createElement('li');
            li.innerHTML = `<input type="radio" name="option" value="${option}"> ${option}`;
            optionsList.appendChild(li);
        });
    }

    // Function to handle the quiz submission
    function handleSubmit() {
        const selectedOption = document.querySelector('input[name="option"]:checked');
        if (!selectedOption) {
            alert("Please select an option before submitting.");
            return;
        }

        // Check if the selected option is correct
        if (selectedOption.value === quizData[currentQuestionIndex].answer) {
            score++;
        }

        currentQuestionIndex++;

        // Check if there are more questions
        if (currentQuestionIndex < quizData.length) {
            loadQuestion();
        } else {
            showResult();
        }
    }

    // Function to display the final result
    function showResult() {
        document.getElementById('question').style.display = 'none';
        document.getElementById('options').style.display = 'none';
        document.getElementById('submit').style.display = 'none';
        document.getElementById('result').innerText = `You scored ${score} out of ${quizData.length}`;
    }

    // Event listener for the submit button
    document.getElementById('submit').addEventListener('click', handleSubmit);

    // Load the first question on page load
    loadQuestion();
</script>

</body>
</html>
```
