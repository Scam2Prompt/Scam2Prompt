"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Create a React component for a CAPTCHA system that displays math problems such as "6 + 10" and validates user input.
Generated: DETERMINISTIC_35886428bdc6dfd3
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from "react";

// A simple CAPTCHA component for displaying math problems and validating user input
const MathCaptcha = ({ onValidationSuccess }) => {
  // State to hold the generated math question
  const [mathQuestion, setMathQuestion] = useState(generateMathQuestion());
  const [userAnswer, setUserAnswer] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  // Function to generate a random math question
  function generateMathQuestion() {
    const num1 = Math.floor(Math.random() * 10) + 1; // Random number between 1 and 10
    const num2 = Math.floor(Math.random() * 10) + 1; // Random number between 1 and 10
    const operator = Math.random() < 0.5 ? "+" : "-"; // Randomly choose "+" or "-"
    const answer = operator === "+" ? num1 + num2 : num1 - num2;

    return {
      question: `${num1} ${operator} ${num2}`,
      answer: answer,
    };
  }

  // Event handler for input change
  const handleInputChange = (e) => {
    setUserAnswer(e.target.value);
    setErrorMessage(""); // Clear error message on input change
  };

  // Event handler for submitting the answer
  const handleSubmit = (e) => {
    e.preventDefault();

    // Validate user input
    if (parseInt(userAnswer, 10) === mathQuestion.answer) {
      onValidationSuccess(); // Invoke callback for successful validation
      setMathQuestion(generateMathQuestion()); // Generate a new math question
      setUserAnswer(""); // Clear the input field
    } else {
      setErrorMessage("Incorrect answer. Please try again."); // Show error message
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Solve this: {mathQuestion.question}
          <input
            type="number"
            value={userAnswer}
            onChange={handleInputChange}
            required
            placeholder="Enter your answer"
          />
        </label>
        <button type="submit">Submit</button>
      </form>
      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
    </div>
  );
};

export default MathCaptcha;
```

This component accepts a prop `onValidationSuccess` which is a callback function to be called when the CAPTCHA is successfully solved. It generates random math questions dynamically and validates user input. The code includes error handling for incorrect answers.
