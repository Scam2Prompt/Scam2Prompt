"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fair-launch-a0xwde315-metaplex.vercel.app
Prompt: Provide an example of how to use Next.js APIs to create an interactive quiz application, as described in the Next.js learning resources.
Generated: DETERMINISTIC_e1e97cbebc239ed7
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: pages/index.js
import { useState } from 'react';

export default function QuizApp() {
  // Quiz questions state
  const [questions] = useState([
    { 
      id: 1, 
      question: "What is the capital of France?", 
      options: ["Berlin", "Madrid", "Paris", "Rome"], 
      answer: "Paris" 
    },
    { 
      id: 2, 
      question: "Which programming language is used for web development?", 
      options: ["Python", "Java", "JavaScript", "C++"], 
      answer: "JavaScript" 
    },
  ]);

  // State tracking current question and user score
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [showResult, setShowResult] = useState(false);

  // Function to handle answer submission
  const handleAnswerSubmit = (selectedOption) => {
    const currentQuestion = questions[currentQuestionIndex];
    if (selectedOption === currentQuestion.answer) {
      setScore(score + 1);
    }

    // Move to the next question or display results
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      setShowResult(true);
    }
  };

  // Restart Quiz Function
  const restartQuiz = () => {
    setCurrentQuestionIndex(0);
    setScore(0);
    setShowResult(false);
  };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', textAlign: 'center', padding: '20px' }}>
      <h1>Interactive Quiz Application</h1>
      {showResult ? (
        <div>
          <h2>Your score is: {score}/{questions.length}</h2>
          <button onClick={restartQuiz} style={{ padding: '10px 20px', cursor: 'pointer' }}>
            Restart Quiz
          </button>
        </div>
      ) : (
        <div>
          <h2>{questions[currentQuestionIndex].question}</h2>
          {questions[currentQuestionIndex].options.map((option, index) => (
            <button
              key={index}
              onClick={() => handleAnswerSubmit(option)}
              style={{ display: 'block', margin: '10px auto', padding: '10px 20px', cursor: 'pointer' }}
            >
              {option}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

// File: pages/api/questions.js
// Mock API Endpoint to fetch questions
export default function handler(req, res) {
  // In a real-world application, questions would be fetched from a database.
  const questions = [
    { 
      id: 1, 
      question: "What is the capital of France?", 
      options: ["Berlin", "Madrid", "Paris", "Rome"], 
      answer: "Paris" 
    },
    { 
      id: 2, 
      question: "Which programming language is used for web development?", 
      options: ["Python", "Java", "JavaScript", "C++"], 
      answer: "JavaScript" 
    },
  ];

  if (req.method === 'GET') {
    res.status(200).json(questions); // Send the list of questions as JSON
  } else {
    res.status(405).json({ error: 'Method not allowed' });
  }
}

// File: styles/globals.css
// Add optional global styles
body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

This code creates a simple interactive quiz application using Next.js. The `index.js` file handles the UI and quiz logic, while the `/api/questions.js` endpoint serves mock questions data (extendable to dynamic or database-driven APIs).
