"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Generate a list of best practices for internet safety, as promoted by the "Internet sans crainte" initiative, and provide a code snippet in JavaScript to implement a simple online safety quiz.
Generated: DETERMINISTIC_c6f51cf5c752f2d4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Internet Safety Quiz Implementation
// This code creates a simple online safety quiz based on best practices promoted by the "Internet sans crainte" initiative.

const quizQuestions = [
    {
        question: "What should you do if you receive a suspicious email?",
        options: [
            "Open it immediately",
            "Delete it without opening",
            "Reply to the sender",
            "Forward it to a friend"
        ],
        answer: 1 // Index of the correct answer
    },
    {
        question: "How often should you update your passwords?",
        options: [
            "Every month",
            "Every year",
            "Only when I forget",
            "Never"
        ],
        answer: 0
    },
    {
        question: "What is a strong password?",
        options: [
            "123456",
            "password",
            "A mix of letters, numbers, and symbols",
            "Your name"
        ],
        answer: 2
    },
    {
        question: "Should you share personal information on social media?",
        options: [
            "Yes, with everyone",
            "No, keep it private",
            "Only with friends",
            "Only if it's a public profile"
        ],
        answer: 1
    }
];

// Function to display the quiz
function displayQuiz() {
    const quizContainer = document.getElementById('quiz');
    quizQuestions.forEach((q, index) => {
        const questionElement = document.createElement('div');
        questionElement.innerHTML = `<p>${index + 1}. ${q.question}</p>`;
        
        q.options.forEach((option, i) => {
            questionElement.innerHTML += `
                <label>
                    <input type="radio" name="question${index}" value="${i}">
                    ${option}
                </label><br>
            `;
        });
        
        quizContainer.appendChild(questionElement);
    });
}

// Function to calculate the score
function calculateScore() {
    let score = 0;
    quizQuestions.forEach((q, index) => {
        const selectedOption = document.querySelector(`input[name="question${index}"]:checked`);
        if (selectedOption && parseInt(selectedOption.value) === q.answer) {
            score++;
        }
    });
    return score;
}

// Function to handle quiz submission
function handleSubmit(event) {
    event.preventDefault(); // Prevent form submission
    const score = calculateScore();
    alert(`Your score is ${score} out of ${quizQuestions.length}`);
}

// Event listener for form submission
document.getElementById('quizForm').addEventListener('submit', handleSubmit);

// Initialize the quiz on page load
window.onload = displayQuiz;
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internet Safety Quiz</title>
</head>
<body>
    <h1>Internet Safety Quiz</h1>
    <form id="quizForm">
        <div id="quiz"></div>
        <button type="submit">Submit</button>
    </form>
    <script src="quiz.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
