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
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * MathCaptcha Component
 *
 * A simple CAPTCHA component that displays a math problem and validates
 * the user's input. It generates a basic addition problem for the user
 * to solve.
 */
const MathCaptcha = ({ onValidate }) => {
    const [num1, setNum1] = useState(0);
    const [num2, setNum2] = useState(0);
    const [userInput, setUserInput] = useState('');
    const [isValid, setIsValid] = useState(null);

    // Generate two random numbers for the math problem
    const generateProblem = () => {
        const randomNum1 = Math.floor(Math.random() * 100);
        const randomNum2 = Math.floor(Math.random() * 100);
        setNum1(randomNum1);
        setNum2(randomNum2);
        setUserInput('');
        setIsValid(null);
    };

    // Validate the user's input against the correct answer
    const validateInput = () => {
        const correctAnswer = num1 + num2;
        if (parseInt(userInput, 10) === correctAnswer) {
            setIsValid(true);
            onValidate(true); // Notify parent component of successful validation
        } else {
            setIsValid(false);
        }
    };

    // Effect to generate a new problem on component mount
    useEffect(() => {
        generateProblem();
    }, []);

    return (
        <div className="math-captcha">
            <h3>CAPTCHA: Solve the following problem</h3>
            <p>
                {num1} + {num2} = ?
            </p>
            <input
                type="number"
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                placeholder="Your answer"
            />
            <button onClick={validateInput}>Submit</button>
            {isValid !== null && (
                <p className={isValid ? 'success' : 'error'}>
                    {isValid ? 'Correct!' : 'Incorrect, please try again.'}
                </p>
            )}
            <button onClick={generateProblem} style={{ marginTop: '10px' }}>
                Generate New Problem
            </button>
        </div>
    );
};

// PropTypes validation
MathCaptcha.propTypes = {
    onValidate: PropTypes.func.isRequired,
};

// Default export of the component
export default MathCaptcha;
```
