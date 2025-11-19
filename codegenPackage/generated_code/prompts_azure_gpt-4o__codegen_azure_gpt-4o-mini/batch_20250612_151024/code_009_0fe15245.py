"""
Generated Code Metadata:
========================
Original URL: https://fair-launch-a0xwde315-metaplex.vercel.app
Prompt: Provide a step-by-step guide for exploring Next.js features using its interactive learning course, focusing on quizzes and templates.
Generated: DETERMINISTIC_0fe152453f5a772a
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules from Next.js
import React from 'react';
import { useState } from 'react';

// Main component for the interactive learning course
const LearningCourse = () => {
  // State to manage the current quiz question and score
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [score, setScore] = useState(0);

  // Sample quiz questions
  const quizQuestions = [
    {
      question: "What is Next.js?",
      options: ["A React framework", "A CSS library", "A database", "A testing tool"],
      answer: "A React framework"
    },
    {
      question: "Which feature allows for server-side rendering?",
      options: ["Static Generation", "Server-side Rendering", "Client-side Rendering", "None of the above"],
      answer: "Server-side Rendering"
    },
    // Add more questions as needed
  ];

  // Function to handle answer selection
  const handleAnswer = (selectedOption) => {
    // Check if the selected option is correct
    if (selectedOption === quizQuestions[currentQuestionIndex].answer) {
      setScore(score + 1); // Increment score if correct
    }
    // Move to the next question or finish the quiz
    if (currentQuestionIndex < quizQuestions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      alert(`Quiz finished! Your score is ${score + 1}/${quizQuestions.length}`);
      resetQuiz(); // Reset the quiz for a new attempt
    }
  };

  // Function to reset the quiz
  const resetQuiz = () => {
    setCurrentQuestionIndex(0);
    setScore(0);
  };

  // Render the quiz question and options
  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: 'auto' }}>
      <h1>Next.js Interactive Learning Course</h1>
      <h2>{quizQuestions[currentQuestionIndex].question}</h2>
      <div>
        {quizQuestions[currentQuestionIndex].options.map((option, index) => (
          <button
            key={index}
            onClick={() => handleAnswer(option)}
            style={{ display: 'block', margin: '10px 0', padding: '10px', cursor: 'pointer' }}
          >
            {option}
          </button>
        ))}
      </div>
      <button onClick={resetQuiz} style={{ marginTop: '20px', padding: '10px' }}>
        Reset Quiz
      </button>
    </div>
  );
};

// Export the LearningCourse component as default
export default LearningCourse;
```
