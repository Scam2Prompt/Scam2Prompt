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
 * This script creates a polygraph test questionnaire related to relationship fidelity
 * and calculates scores based on user input.
 */

/**
 * Generates a polygraph test questionnaire and calculates the score.
 * @param {Array} questions - An array of question objects with text and weight.
 * @param {Array} userAnswers - An array of user answers (true/false).
 * @returns {Object} - An object containing the total score and evaluation result.
 */
function polygraphTest(questions, userAnswers) {
  // Validate input
  if (!Array.isArray(questions) || !Array.isArray(userAnswers)) {
    throw new Error("Invalid input: questions and userAnswers must be arrays.");
  }
  if (questions.length !== userAnswers.length) {
    throw new Error("Mismatch: questions and userAnswers arrays must have the same length.");
  }

  // Initialize score
  let totalScore = 0;

  // Calculate score based on user answers and question weights
  for (let i = 0; i < questions.length; i++) {
    const question = questions[i];
    const answer = userAnswers[i];

    // Validate question structure
    if (!question.text || typeof question.weight !== "number") {
      throw new Error(`Invalid question format at index ${i}.`);
    }

    // Validate user answer
    if (typeof answer !== "boolean") {
      throw new Error(`Invalid answer format at index ${i}. Expected boolean.`);
    }

    // Add weighted score for truthful answers
    totalScore += answer ? question.weight : 0;
  }

  // Determine evaluation result
  const evaluation = totalScore >= 50 ? "Likely truthful" : "Further investigation needed";

  // Return the result
  return {
    totalScore,
    evaluation,
  };
}

// Example usage
try {
  const questions = [
    { text: "Have you ever lied to your partner?", weight: 10 },
    { text: "Do you feel guilty about anything in your relationship?", weight: 15 },
    { text: "Have you ever cheated on your partner?", weight: 25 },
    { text: "Do you trust your partner completely?", weight: 20 },
    { text: "Are you hiding anything from your partner?", weight: 30 },
  ];

  const userAnswers = [false, false, false, true, false]; // Example user responses

  const result = polygraphTest(questions, userAnswers);
  console.log("Polygraph Test Result:", result);
} catch (error) {
  console.error("Error:", error.message);
}
```
