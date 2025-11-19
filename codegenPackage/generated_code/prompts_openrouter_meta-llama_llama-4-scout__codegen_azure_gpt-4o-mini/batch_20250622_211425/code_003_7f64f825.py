"""
Generated Code Metadata:
========================
Original URL: https://fair-launch-a0xwde315-metaplex.vercel.app
Prompt: Create an interactive course with quizzes for learning Next.js features and API.
Generated: DETERMINISTIC_7f64f825249f1963
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules from Next.js and React
import { useState } from 'react';
import Head from 'next/head';
import styles from '../styles/Home.module.css';

// Sample quiz data
const quizzes = [
  {
    question: "What is Next.js?",
    options: ["A JavaScript library", "A React framework", "A CSS framework", "A database"],
    answer: 1,
  },
  {
    question: "Which feature does Next.js provide for server-side rendering?",
    options: ["getStaticProps", "getServerSideProps", "getInitialProps", "All of the above"],
    answer: 3,
  },
  {
    question: "What is the default port for a Next.js application?",
    options: ["3000", "8080", "5000", "4000"],
    answer: 0,
  },
];

// Main component for the interactive course
export default function Home() {
  const [currentQuiz, setCurrentQuiz] = useState(0);
  const [selectedOption, setSelectedOption] = useState(null);
  const [score, setScore] = useState(0);
  const [quizCompleted, setQuizCompleted] = useState(false);

  // Function to handle option selection
  const handleOptionSelect = (index) => {
    setSelectedOption(index);
  };

  // Function to handle quiz submission
  const handleSubmit = () => {
    if (selectedOption === null) {
      alert("Please select an option before submitting.");
      return;
    }

    // Update score if the answer is correct
    if (selectedOption === quizzes[currentQuiz].answer) {
      setScore(score + 1);
    }

    // Move to the next quiz or complete the quiz
    if (currentQuiz < quizzes.length - 1) {
      setCurrentQuiz(currentQuiz + 1);
      setSelectedOption(null);
    } else {
      setQuizCompleted(true);
    }
  };

  // Function to restart the quiz
  const restartQuiz = () => {
    setCurrentQuiz(0);
    setScore(0);
    setSelectedOption(null);
    setQuizCompleted(false);
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Next.js Interactive Course</title>
        <meta name="description" content="Learn Next.js features through interactive quizzes." />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Next.js Interactive Course</h1>

        {quizCompleted ? (
          <div>
            <h2>Quiz Completed!</h2>
            <p>Your score: {score} out of {quizzes.length}</p>
            <button onClick={restartQuiz}>Restart Quiz</button>
          </div>
        ) : (
          <div>
            <h2>{quizzes[currentQuiz].question}</h2>
            <div>
              {quizzes[currentQuiz].options.map((option, index) => (
                <div key={index}>
                  <input
                    type="radio"
                    id={`option${index}`}
                    name="quiz"
                    value={index}
                    checked={selectedOption === index}
                    onChange={() => handleOptionSelect(index)}
                  />
                  <label htmlFor={`option${index}`}>{option}</label>
                </div>
              ))}
            </div>
            <button onClick={handleSubmit}>Submit</button>
          </div>
        )}
      </main>
    </div>
  );
}
```

### Notes:
- Ensure you have a Next.js environment set up to run this code.
- The code includes basic error handling for user input.
- The quiz data can be expanded or modified as needed.
