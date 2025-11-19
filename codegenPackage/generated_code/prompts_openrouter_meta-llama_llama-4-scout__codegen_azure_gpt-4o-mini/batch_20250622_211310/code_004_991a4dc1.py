"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.nl
Prompt: Write a code snippet in JavaScript to implement a simple quiz or assessment for users to determine their investment knowledge level, similar to what Immediate Peak offers.
Generated: DETERMINISTIC_991a4dc115d1ae80
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Investment Knowledge Quiz
// This script implements a simple quiz to assess the user's investment knowledge level.

const quizQuestions = [
    {
        question: "What is a stock?",
        options: ["A loan to a company", "A share of ownership in a company", "A type of bond", "None of the above"],
        answer: 1 // Index of the correct answer
    },
    {
        question: "What does diversification mean?",
        options: ["Investing in a single asset", "Spreading investments across various assets", "Investing only in stocks", "None of the above"],
        answer: 1
    },
    {
        question: "What is a mutual fund?",
        options: ["A type of stock", "A pool of money from many investors to buy securities", "A government bond", "None of the above"],
        answer: 1
    },
    {
        question: "What is the primary goal of investing?",
        options: ["To lose money", "To preserve capital", "To grow wealth over time", "To avoid taxes"],
        answer: 2
    },
    {
        question: "What is a bear market?",
        options: ["A market that is rising", "A market that is falling", "A market with no change", "None of the above"],
        answer: 1
    }
];

// Function to start the quiz
function startQuiz() {
    let score = 0; // Initialize score
    const totalQuestions = quizQuestions.length;

    // Loop through each question
    for (let i = 0; i < totalQuestions; i++) {
        const question = quizQuestions[i];
        const userAnswer = askQuestion(question);

        // Check if the answer is correct
        if (userAnswer === question.answer) {
            score++;
        }
    }

    // Display the final score
    displayResults(score, totalQuestions);
}

// Function to ask a question and get user's answer
function askQuestion(question) {
    const optionsString = question.options.map((option, index) => `${index + 1}: ${option}`).join("\n");
    const userInput = prompt(`${question.question}\n${optionsString}\nPlease enter the number of your answer:`);

    // Validate user input
    const answerIndex = parseInt(userInput) - 1;
    if (isNaN(answerIndex) || answerIndex < 0 || answerIndex >= question.options.length) {
        alert("Invalid input. Please enter a number corresponding to your answer.");
        return askQuestion(question); // Retry asking the question
    }

    return answerIndex; // Return the index of the user's answer
}

// Function to display the results of the quiz
function displayResults(score, totalQuestions) {
    const percentage = (score / totalQuestions) * 100;
    let knowledgeLevel;

    // Determine knowledge level based on score
    if (percentage === 100) {
        knowledgeLevel = "Expert";
    } else if (percentage >= 75) {
        knowledgeLevel = "Proficient";
    } else if (percentage >= 50) {
        knowledgeLevel = "Intermediate";
    } else {
        knowledgeLevel = "Beginner";
    }

    alert(`Your score: ${score}/${totalQuestions} (${percentage.toFixed(2)}%)\nKnowledge Level: ${knowledgeLevel}`);
}

// Start the quiz when the script is loaded
startQuiz();
```
