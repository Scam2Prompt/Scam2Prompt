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
// Financial Literacy Quiz Application
// This script implements a simple quiz on financial literacy topics such as investment strategies and risk management.

// Questions for the quiz
const quizQuestions = [
  {
    question: "What is the primary benefit of diversification in investing?",
    options: [
      "A. Higher returns",
      "B. Reduced risk",
      "C. Lower taxes",
      "D. Increased liquidity"
    ],
    correctAnswer: "B"
  },
  {
    question: "Which investment type typically carries the highest risk?",
    options: [
      "A. Bonds",
      "B. Mutual Funds",
      "C. Stocks",
      "D. Savings Account"
    ],
    correctAnswer: "C"
  },
  {
    question: "What does 'risk tolerance' refer to?",
    options: [
      "A. The ability to avoid losses",
      "B. The willingness to take on financial risk",
      "C. The amount of money invested",
      "D. The time horizon for investments"
    ],
    correctAnswer: "B"
  }
];

// Function to run the quiz
function runQuiz() {
  let score = 0;

  console.log("Welcome to the Financial Literacy Quiz!");
  console.log("Answer the following questions by typing the letter corresponding to your choice.\n");

  quizQuestions.forEach((questionObj, index) => {
    console.log(`Question ${index + 1}: ${questionObj.question}`);
    questionObj.options.forEach(option => console.log(option));

    let userAnswer = prompt("Your answer (A, B, C, or D): ").toUpperCase();

    // Validate user input
    while (!["A", "B", "C", "D"].includes(userAnswer)) {
      console.log("Invalid input. Please enter A, B, C, or D.");
      userAnswer = prompt("Your answer (A, B, C, or D): ").toUpperCase();
    }

    // Check if the answer is correct
    if (userAnswer === questionObj.correctAnswer) {
      console.log("Correct!\n");
      score++;
    } else {
      console.log(`Incorrect. The correct answer was ${questionObj.correctAnswer}.\n`);
    }
  });

  // Display final score
  console.log(`Quiz completed! Your final score is ${score}/${quizQuestions.length}.`);
  console.log("Thank you for participating in the Financial Literacy Quiz!");
}

// Error handling for prompt function (browser environment required)
try {
  runQuiz();
} catch (error) {
  console.error("An error occurred while running the quiz:", error.message);
  console.log("Please ensure you are running this script in a browser environment that supports 'prompt'.");
}
```
