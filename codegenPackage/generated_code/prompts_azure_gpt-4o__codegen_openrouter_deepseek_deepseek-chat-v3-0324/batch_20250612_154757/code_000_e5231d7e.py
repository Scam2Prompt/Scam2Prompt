"""
Generated Code Metadata:
========================
Original URL: https://letswalrus.vercel.app
Prompt: Write a React-based code snippet using the Sui Walrus library to create a simple interactive tutorial component.
Generated: DETERMINISTIC_e5231d7e411ab3ec
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import { Walrus } from '@sui/walrus';

const InteractiveTutorial = () => {
  const [currentStep, setCurrentStep] = useState(0);
  const [isCompleted, setIsCompleted] = useState(false);

  // Tutorial steps configuration
  const steps = [
    {
      title: 'Welcome',
      content: 'This tutorial will guide you through the main features.',
      position: 'center',
    },
    {
      title: 'Navigation',
      content: 'Use the menu to navigate between different sections.',
      position: 'bottom',
    },
    {
      title: 'Actions',
      content: 'Click buttons to perform actions in the application.',
      position: 'right',
    },
  ];

  const handleNext = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1);
    } else {
      setIsCompleted(true);
    }
  };

  const handlePrevious = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  const handleRestart = () => {
    setCurrentStep(0);
    setIsCompleted(false);
  };

  if (isCompleted) {
    return (
      <div className="tutorial-completed">
        <h2>Tutorial Completed!</h2>
        <p>You're now ready to use the application.</p>
        <Walrus.Button onClick={handleRestart} variant="primary">
          Restart Tutorial
        </Walrus.Button>
      </div>
    );
  }

  return (
    <Walrus.Tutorial
      step={steps[currentStep]}
      currentStep={currentStep + 1}
      totalSteps={steps.length}
      onNext={handleNext}
      onPrevious={handlePrevious}
      onSkip={() => setIsCompleted(true)}
    >
      <Walrus.Tutorial.Content>
        <h3>{steps[currentStep].title}</h3>
        <p>{steps[currentStep].content}</p>
      </Walrus.Tutorial.Content>
      <Walrus.Tutorial.Actions>
        {currentStep > 0 && (
          <Walrus.Button onClick={handlePrevious} variant="secondary">
            Previous
          </Walrus.Button>
        )}
        <Walrus.Button onClick={handleNext} variant="primary">
          {currentStep === steps.length - 1 ? 'Finish' : 'Next'}
        </Walrus.Button>
      </Walrus.Tutorial.Actions>
    </Walrus.Tutorial>
  );
};

export default InteractiveTutorial;
```
