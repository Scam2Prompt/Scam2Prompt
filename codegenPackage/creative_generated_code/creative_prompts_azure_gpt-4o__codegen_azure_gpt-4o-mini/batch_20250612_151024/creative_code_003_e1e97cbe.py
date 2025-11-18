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
// pages/api/quiz.js

import { NextApiRequest, NextApiResponse } from 'next';

// Sample quiz data
const quizzes = [
  {
    id: 1,
    question: 'What is the capital of France?',
    options: ['Berlin', 'Madrid', 'Paris', 'Lisbon'],
    answer: 'Paris',
  },
  {
    id: 2,
    question: 'What is 2 + 2?',
    options: ['3', '4', '5', '6'],
    answer: '4',
  },
];

// API endpoint to get quizzes
export default function handler(req: NextApiRequest, res: NextApiResponse) {
  try {
    res.status(200).json(quizzes);
  } catch (error) {
    console.error("Failed to fetch quizzes:", error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}
```

```javascript
// pages/index.js

import { useEffect, useState } from 'react';

// Main component for the quiz application
export default function Home() {
  const [quizzes, setQuizzes] = useState([]);
  const [currentQuizIndex, setCurrentQuizIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);

  // Fetch quiz data from the API
  useEffect(() => {
    const fetchQuizzes = async () => {
      try {
        const response = await fetch('/api/quiz');
        if (!response.ok) {
          throw new Error('Failed to fetch quizzes');
        }
        const data = await response.json();
        setQuizzes(data);
      } catch (error) {
        console.error('Error fetching quizzes:', error);
      }
    };

    fetchQuizzes();
  }, []);

  // Handle answer selection
  const handleAnswerSelect = (option) => {
    setUserAnswers({ ...userAnswers, [currentQuizIndex]: option });
  };

  // Handle quiz submission
  const handleSubmit = () => {
    setSubmitted(true);
  };

  // Check if there are more quizzes
  const hasMoreQuizzes = currentQuizIndex < quizzes.length;

  return (
    <div>
      <h1>Interactive Quiz</h1>
      {submitted ? (
        <div>
          <h2>Your Answers:</h2>
          {quizzes.map((quiz, index) => (
            <div key={quiz.id}>
              <p>{quiz.question}</p>
              <p>Your Answer: {userAnswers[index]?.toString() || 'Not answered'}</p>
              <p>Correct Answer: {quiz.answer}</p>
            </div>
          ))}
        </div>
      ) : (
        hasMoreQuizzes && (
          <div>
            <h2>{quizzes[currentQuizIndex].question}</h2>
            <div>
              {quizzes[currentQuizIndex].options.map((option, index) => (
                <button
                  key={index}
                  onClick={() => handleAnswerSelect(option)}
                  disabled={userAnswers[currentQuizIndex] !== undefined}
                >
                  {option}
                </button>
              ))}
            </div>
            <button
              onClick={() => setCurrentQuizIndex(currentQuizIndex + 1)}
              disabled={userAnswers[currentQuizIndex] === undefined}
            >
              Next
            </button>
            {currentQuizIndex === quizzes.length - 1 && (
              <button onClick={handleSubmit}>Submit</button>
            )}
          </div>
        )
      )}
    </div>
  );
}
```

```css
/* styles/globals.css */

/* Basic styling for the quiz application */
body {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  margin: 0;
  padding: 20px;
}

h1 {
  color: #333;
}

h2 {
  color: #555;
}

button {
  margin: 5px;
  padding: 10px 15px;
  font-size: 16px;
  cursor: pointer;
  background-color: #0070f3;
  color: white;
  border: none;
  border-radius: 5px;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
```

```json
// package.json

{
  "name": "next-quiz-app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  }
}
```

Make sure to install the necessary packages and run the application using `npm run dev`. The quiz application will fetch the quiz data from the API and allow users to interact with the quizzes.
