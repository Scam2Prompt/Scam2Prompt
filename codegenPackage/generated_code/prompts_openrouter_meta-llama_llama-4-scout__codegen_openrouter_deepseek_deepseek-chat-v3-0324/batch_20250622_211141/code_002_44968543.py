"""
Generated Code Metadata:
========================
Original URL: https://get-galagames.com
Prompt: Generate a JavaScript function to create a simple quiz, similar to the "Question of the day" section, that determines a user's home security company preference.
Generated: DETERMINISTIC_449685436e04fcc3
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple quiz to determine user's home security company preference.
 * 
 * @param {Array} questions - Array of question objects with text and options.
 * @param {Object} scoring - Scoring rules mapping company names to option indices.
 * @returns {Function} Function to start the quiz and return the result.
 */
function createHomeSecurityQuiz(questions, scoring) {
    // Validate inputs
    if (!Array.isArray(questions) || questions.length === 0) {
        throw new Error('Questions must be a non-empty array');
    }
    if (typeof scoring !== 'object' || Object.keys(scoring).length === 0) {
        throw new Error('Scoring must be a non-empty object');
    }

    let currentQuestionIndex = 0;
    const scores = {};

    // Initialize scores for all companies
    Object.keys(scoring).forEach(company => {
        scores[company] = 0;
    });

    /**
     * Display the current question and handle user response.
     * 
     * @param {number} answerIndex - Index of the selected answer.
     * @returns {Object|null} Result object if quiz is complete, otherwise null.
     */
    function nextQuestion(answerIndex) {
        // Validate answer index
        if (typeof answerIndex !== 'number' || answerIndex < 0 || answerIndex >= questions[currentQuestionIndex].options.length) {
            throw new Error('Invalid answer index');
        }

        // Update scores based on answer
        Object.entries(scoring).forEach(([company, optionIndices]) => {
            if (optionIndices.includes(answerIndex)) {
                scores[company]++;
            }
        });

        // Move to next question or return result
        currentQuestionIndex++;
        if (currentQuestionIndex >= questions.length) {
            return getResult();
        }
        return null;
    }

    /**
     * Determine the winning company based on scores.
     * 
     * @returns {Object} Result with company name and score.
     */
    function getResult() {
        let maxScore = -1;
        let winningCompany = null;

        Object.entries(scores).forEach(([company, score]) => {
            if (score > maxScore) {
                maxScore = score;
                winningCompany = company;
            }
        });

        return {
            company: winningCompany,
            score: maxScore
        };
    }

    /**
     * Get the current question.
     * 
     * @returns {Object} Current question object.
     */
    function getCurrentQuestion() {
        return questions[currentQuestionIndex];
    }

    /**
     * Check if quiz is complete.
     * 
     * @returns {boolean} True if quiz is complete.
     */
    function isComplete() {
        return currentQuestionIndex >= questions.length;
    }

    return {
        nextQuestion,
        getCurrentQuestion,
        isComplete,
        getResult
    };
}

// Example usage:
/*
const questions = [
    {
        text: "What is your top priority in a security system?",
        options: [
            "24/7 Professional Monitoring",
            "Smart Home Integration",
            "Affordability",
            "DIY Installation"
        ]
    },
    {
        text: "How important is mobile app control to you?",
        options: [
            "Essential",
            "Nice to have",
            "Not important"
        ]
    }
];

const scoring = {
    "Company A": [0, 0], // Scores for 24/7 Monitoring and Essential app control
    "Company B": [1, 1], // Scores for Smart Home and Nice to have app control
    "Company C": [2, 2]  // Scores for Affordability and Not important app control
};

const quiz = createHomeSecurityQuiz(questions, scoring);

// Simulate user answering questions
quiz.nextQuestion(0); // Answer first question with first option
quiz.nextQuestion(1); // Answer second question with second option

if (quiz.isComplete()) {
    const result = quiz.getResult();
    console.log(`Recommended company: ${result.company} (Score: ${result.score})`);
}
*/
```
