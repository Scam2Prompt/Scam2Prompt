"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Provide a JavaScript code snippet to create a quiz system for Physics students in Class XI or XII, with questions and answers based on CBSE syllabus.
Generated: DETERMINISTIC_b61a27270971f610
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Quiz System for Physics Students (Class XI/XII - CBSE Syllabus)

// Question and Answer Data
const quizData = [
  {
    question: "What is the SI unit of force?",
    options: ["Newton", "Joule", "Pascal", "Watt"],
    correctAnswer: "Newton",
  },
  {
    question: "Who proposed the law of gravitation?",
    options: ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "James Clerk Maxwell"],
    correctAnswer: "Isaac Newton",
  },
  {
    question: "What is the speed of light in vacuum?",
    options: ["3 × 10^8 m/s", "1 × 10^6 m/s", "5 × 10^7 m/s", "2 × 10^9 m/s"],
    correctAnswer: "3 × 10^8 m/s",
  },
  {
    question: "Which of the following is a scalar quantity?",
    options: ["Velocity", "Force", "Energy", "Acceleration"],
    correctAnswer: "Energy",
  },
];

// Function to start the quiz
function startQuiz() {
  let score = 0;

  // Loop through each question
  quizData.forEach((item, index) => {
    console.log(`Question ${index + 1}: ${item.question}`);
    item.options.forEach((option, i) => {
      console.log(`${i + 1}. ${option}`);
    });

    // Prompt user for their answer
    const userAnswer = prompt(`Enter the number corresponding to your answer for Question ${index + 1}:`);

    // Validate user input
    if (!userAnswer || isNaN(userAnswer) || userAnswer < 1 || userAnswer > item.options.length) {
      console.error("Invalid input. Please enter a valid option number.");
      return;
    }

    // Check if the answer is correct
    const selectedAnswer = item.options[userAnswer - 1];
    if (selectedAnswer === item.correctAnswer) {
      console.log("Correct!");
      score++;
    } else {
      console.log(`Wrong! The correct answer is: ${item.correctAnswer}`);
    }
  });

  // Display final score
  console.log(`Quiz Completed! Your final score is: ${score}/${quizData.length}`);
}

// Error handling for unsupported environments
if (typeof prompt === "undefined") {
  console.error("The 'prompt' function is not supported in this environment. Please run this code in a browser.");
} else {
  // Start the quiz
  startQuiz();
}
```
