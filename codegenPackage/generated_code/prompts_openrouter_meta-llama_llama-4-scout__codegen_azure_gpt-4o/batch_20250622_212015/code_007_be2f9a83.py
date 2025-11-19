"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: "Write a code snippet in JavaScript to implement a simple quiz system for assessing students' knowledge in subjects like food safety, nutrition, and culinary techniques."
Generated: DETERMINISTIC_be2f9a83662a36a4
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Quiz System Implementation in JavaScript

// Question data structure
const quizQuestions = [
  {
    subject: "Food Safety",
    question: "What is the safe temperature range for storing perishable food?",
    options: ["0-5°C", "10-20°C", "30-40°C", "50-60°C"],
    correctAnswer: 0, // Index of the correct answer
  },
  {
    subject: "Nutrition",
    question: "Which vitamin is primarily found in citrus fruits?",
    options: ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"],
    correctAnswer: 2,
  },
  {
    subject: "Culinary Techniques",
    question: "What is the term for cooking food in a vacuum-sealed bag at a low temperature?",
    options: ["Sous Vide", "Sautéing", "Grilling", "Braising"],
    correctAnswer: 0,
  },
];

// Function to display a question and get user input
function askQuestion(questionObj) {
  console.log(`Subject: ${questionObj.subject}`);
  console.log(`Question: ${questionObj.question}`);
  questionObj.options.forEach((option, index) => {
    console.log(`${index + 1}. ${option}`);
  });

  // Simulate user input (replace with actual input mechanism in production)
  const userAnswer = prompt("Enter the number of your answer:");

  // Validate user input
  if (isNaN(userAnswer) || userAnswer < 1 || userAnswer > questionObj.options.length) {
    console.error("Invalid input. Please enter a valid option number.");
    return false;
  }

  // Check if the answer is correct
  const isCorrect = parseInt(userAnswer) - 1 === questionObj.correctAnswer;
  if (isCorrect) {
    console.log("Correct! Well done.");
  } else {
    console.log(
      `Incorrect. The correct answer was: ${
        questionObj.options[questionObj.correctAnswer]
      }`
    );
  }

  return isCorrect;
}

// Main function to run the quiz
function runQuiz(questions) {
  let score = 0;

  console.log("Welcome to the Quiz System!");
  console.log("Answer the following questions to test your knowledge.\n");

  questions.forEach((questionObj, index) => {
    console.log(`Question ${index + 1}:`);
    const result = askQuestion(questionObj);
    if (result) {
      score++;
    }
    console.log(""); // Add a blank line for better readability
  });

  console.log(`Quiz completed! Your score: ${score}/${questions.length}`);
}

// Error handling for prompt (browser environment required)
if (typeof prompt === "undefined") {
  console.error(
    "Error: 'prompt' function is not available. Please run this code in a browser environment."
  );
} else {
  // Start the quiz
  runQuiz(quizQuestions);
}
```
