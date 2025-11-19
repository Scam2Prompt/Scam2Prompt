"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Write a JavaScript function to create a polygraph test questionnaire, including questions related to relationship fidelity, and calculate scores based on user input."
Generated: DETERMINISTIC_7d43150b6b35ae87
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Polygraph Test Questionnaire
 * 
 * This module generates a polygraph test questionnaire and calculates scores based on user input.
 * 
 * @module polygraphTest
 */

// Define the questionnaire questions and their corresponding scores
const questionnaire = [
  {
    question: "Have you ever lied to your partner about your whereabouts?",
    score: 2
  },
  {
    question: "Have you ever had a romantic relationship with someone other than your partner?",
    score: 5
  },
  {
    question: "Have you ever sent or received flirtatious messages to/from someone other than your partner?",
    score: 3
  },
  {
    question: "Have you ever kept a secret from your partner that could potentially harm your relationship?",
    score: 4
  },
  {
    question: "Have you ever felt attracted to someone other than your partner?",
    score: 1
  }
];

/**
 * Calculates the polygraph test score based on user input.
 * 
 * @param {Object[]} answers - An array of user answers, where each answer is an object with a 'questionIndex' and a 'response' (true or false).
 * @returns {number} The calculated polygraph test score.
 */
function calculateScore(answers) {
  let score = 0;
  answers.forEach(answer => {
    if (answer.response) {
      score += questionnaire[answer.questionIndex].score;
    }
  });
  return score;
}

/**
 * Generates the polygraph test questionnaire and handles user input.
 */
function polygraphTest() {
  console.log("Polygraph Test Questionnaire:");
  let answers = [];

  // Display each question and get user response
  questionnaire.forEach((question, index) => {
    console.log(`\n${index + 1}. ${question.question}`);
    let response = readlineSync.question("Please respond with 'yes' or 'no': ");
    response = response.toLowerCase() === 'yes';
    answers.push({ questionIndex: index, response });
  });

  // Calculate and display the polygraph test score
  let score = calculateScore(answers);
  console.log(`\nYour polygraph test score is: ${score}`);

  // Interpret the polygraph test score
  if (score <= 5) {
    console.log("Your relationship appears to be healthy and faithful.");
  } else if (score <= 10) {
    console.log("Your relationship may have some issues related to fidelity, consider discussing with your partner.");
  } else {
    console.log("Your relationship may be at risk due to significant fidelity issues, consider seeking professional help.");
  }
}

// Import readlineSync for getting user input
const readlineSync = require('readline-sync');

// Run the polygraph test
polygraphTest();
```
