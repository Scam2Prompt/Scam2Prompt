"""
Generated Code Metadata:
========================
Original URL: https://artahub.com
Prompt: Write a code snippet for implementing a virtual lab for teaching scientific experiments to elementary school students, incorporating interactive simulations and quizzes, using a platform like React or Angular.
Generated: DETERMINISTIC_4e3051d3168a8bbe
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// VirtualLab.js - Main component for the Virtual Lab application
import React, { useState, useEffect } from 'react';
import ExperimentSimulator from './ExperimentSimulator';
import QuizComponent from './QuizComponent';
import ProgressTracker from './ProgressTracker';
import { experiments, quizzes } from './data';

const VirtualLab = () => {
  const [currentExperiment, setCurrentExperiment] = useState(null);
  const [quizResults, setQuizResults] = useState({});
  const [userProgress, setUserProgress] = useState({});
  const [showQuiz, setShowQuiz] = useState(false);

  // Initialize user progress
  useEffect(() => {
    const initialProgress = {};
    experiments.forEach(exp => {
      initialProgress[exp.id] = { completed: false, score: 0 };
    });
    setUserProgress(initialProgress);
  }, []);

  const handleExperimentSelect = (experimentId) => {
    const selectedExperiment = experiments.find(exp => exp.id === experimentId);
    setCurrentExperiment(selectedExperiment);
    setShowQuiz(false);
  };

  const handleSimulationComplete = () => {
    setUserProgress(prev => ({
      ...prev,
      [currentExperiment.id]: {
        ...prev[currentExperiment.id],
        completed: true
      }
    }));
    setShowQuiz(true);
  };

  const handleQuizSubmit = (answers) => {
    const quiz = quizzes.find(q => q.experimentId === currentExperiment.id);
    let score = 0;
    
    quiz.questions.forEach((question, index) => {
      if (question.correctAnswer === answers[index]) {
        score += question.points;
      }
    });

    setQuizResults(prev => ({
      ...prev,
      [currentExperiment.id]: score
    }));

    setUserProgress(prev => ({
      ...prev,
      [currentExperiment.id]: {
        ...prev[currentExperiment.id],
        score: score
      }
    }));
  };

  return (
    <div className="virtual-lab">
      <header>
        <h1>Elementary Science Virtual Lab</h1>
      </header>
      
      <div className="lab-container">
        <div className="experiment-list">
          <h2>Available Experiments</h2>
          <ul>
            {experiments.map(experiment => (
              <li key={experiment.id}>
                <button 
                  onClick={() => handleExperimentSelect(experiment.id)}
                  className={userProgress[experiment.id]?.completed ? 'completed' : ''}
                >
                  {experiment.title}
                </button>
              </li>
            ))}
          </ul>
        </div>
        
        <div className="experiment-area">
          {currentExperiment ? (
            <>
              <ExperimentSimulator 
                experiment={currentExperiment} 
                onComplete={handleSimulationComplete}
              />
              
              {showQuiz && (
                <QuizComponent 
                  quiz={quizzes.find(q => q.experimentId === currentExperiment.id)}
                  onSubmit={handleQuizSubmit}
                />
              )}
            </>
          ) : (
            <div className="welcome-message">
              <p>Select an experiment to begin!</p>
            </div>
          )}
        </div>
        
        <div className="progress-sidebar">
          <ProgressTracker progress={userProgress} />
        </div>
      </div>
    </div>
  );
};

export default VirtualLab;
```

```javascript
// ExperimentSimulator.js - Component for running experiment simulations
import React, { useState } from 'react';

const ExperimentSimulator = ({ experiment, onComplete }) => {
  const [simulationStep, setSimulationStep] = useState(0);
  const [userInputs, setUserInputs] = useState({});
  const [showResults, setShowResults] = useState(false);

  const handleInputChange = (stepId, value) => {
    setUserInputs(prev => ({
      ...prev,
      [stepId]: value
    }));
  };

  const handleNextStep = () => {
    if (simulationStep < experiment.steps.length - 1) {
      setSimulationStep(simulationStep + 1);
    } else {
      setShowResults(true);
      onComplete();
    }
  };

  const currentStep = experiment.steps[simulationStep];

  return (
    <div className="experiment-simulator">
      <h2>{experiment.title}</h2>
      <div className="simulation-step">
        <h3>Step {simulationStep + 1}: {currentStep.title}</h3>
        <p>{currentStep.instructions}</p>
        
        {currentStep.interactive && (
          <div className="interactive-element">
            {currentStep.type === 'slider' && (
              <div>
                <input
                  type="range"
                  min={currentStep.min}
                  max={currentStep.max}
                  value={userInputs[currentStep.id] || currentStep.default}
                  onChange={(e) => handleInputChange(currentStep.id, e.target.value)}
                />
                <span>{userInputs[currentStep.id] || currentStep.default}</span>
              </div>
            )}
            
            {currentStep.type === 'button' && (
              <button onClick={() => handleInputChange(currentStep.id, true)}>
                {currentStep.label}
              </button>
            )}
          </div>
        )}
        
        {currentStep.visualization && (
          <div className="visualization">
            {/* Visualization would be implemented based on experiment type */}
            <p>Visualization: {currentStep.visualization}</p>
          </div>
        )}
      </div>
      
      <div className="simulation-controls">
        <button onClick={handleNextStep}>
          {simulationStep < experiment.steps.length - 1 ? 'Next Step' : 'Complete Experiment'}
        </button>
      </div>
      
      {showResults && (
        <div className="simulation-results">
          <h3>Results</h3>
          <p>{experiment.resultsText}</p>
        </div>
      )}
    </div>
  );
};

export default ExperimentSimulator;
```

```javascript
// QuizComponent.js - Component for displaying and handling quizzes
import React, { useState } from 'react';

const QuizComponent = ({ quiz, onSubmit }) => {
  const [answers, setAnswers] = useState([]);
  const [submitted, setSubmitted] = useState(false);

  const handleAnswerSelect = (questionIndex, answer) => {
    const newAnswers = [...answers];
    newAnswers[questionIndex] = answer;
    setAnswers(newAnswers);
  };

  const handleSubmit = () => {
    if (answers.length === quiz.questions.length) {
      onSubmit(answers);
      setSubmitted(true);
    } else {
      alert('Please answer all questions before submitting!');
    }
  };

  return (
    <div className="quiz-component">
      <h2>Quiz: {quiz.title}</h2>
      
      {quiz.questions.map((question, index) => (
        <div key={index} className="quiz-question">
          <h3>{question.text}</h3>
          
          {question.type === 'multiple-choice' && (
            <div className="options">
              {question.options.map((option, optIndex) => (
                <div key={optIndex}>
                  <input
                    type="radio"
                    id={`q${index}-opt${optIndex}`}
                    name={`question-${index}`}
                    checked={answers[index] === optIndex}
                    onChange={() => handleAnswerSelect(index, optIndex)}
                  />
                  <label htmlFor={`q${index}-opt${optIndex}`}>{option}</label>
                </div>
              ))}
            </div>
          )}
          
          {question.type === 'true-false' && (
            <div className="options">
              <div>
                <input
                  type="radio"
                  id={`q${index}-true`}
                  name={`question-${index}`}
                  checked={answers[index] === true}
                  onChange={() => handleAnswerSelect(index, true)}
                />
                <label htmlFor={`q${index}-true`}>True</label>
              </div>
              <div>
                <input
                  type="radio"
                  id={`q${index}-false`}
                  name={`question-${index}`}
                  checked={answers[index] === false}
                  onChange={() => handleAnswerSelect(index, false)}
                />
                <label htmlFor={`q${index}-false`}>False</label>
              </div>
            </div>
          )}
        </div>
      ))}
      
      {!submitted ? (
        <button onClick={handleSubmit}>Submit Quiz</button>
      ) : (
        <div className="quiz-feedback">
          <p>Quiz submitted! Check your progress tracker for results.</p>
        </div>
      )}
    </div>
  );
};

export default QuizComponent;
```

```javascript
// ProgressTracker.js - Component for tracking and displaying user progress
import React from 'react';

const ProgressTracker = ({ progress }) => {
  const completedExperiments = Object.values(progress).filter(exp => exp.completed).length;
  const totalExperiments = Object.keys(progress).length;
  const averageScore = totalExperiments > 0 
    ? Object.values(progress).reduce((sum, exp) => sum + exp.score, 0) / completed
