"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-31--distracted-jepsen-bc9c39.netlify.app
Prompt: "Write a JavaScript function to calculate a clinical assessment score for opioid risk based on user input."
Generated: DETERMINISTIC_e733802ceb93a728
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the Opioid Risk Tool (ORT) score based on user input.
 * The ORT is a brief screening tool to assess the risk of opioid misuse in patients.
 * 
 * @param {Object} userInput - An object containing the user's responses to the ORT questions.
 * @param {number} userInput.age - Age group: 1 (16-45), 0 (otherwise).
 * @param {number} userInput.familyHistory - Family history of substance abuse: 1 (yes), 0 (no).
 * @param {number} userInput.personalHistory - Personal history of substance abuse: 1 (yes), 0 (no).
 * @param {number} userInput.mentalHealth - History of mental health disorders: 1 (yes), 0 (no).
 * @param {number} userInput.sexualAbuse - History of preadolescent sexual abuse: 1 (yes), 0 (no).
 * @returns {number} The total ORT score (0-5).
 * @throws {Error} If any input is invalid or missing.
 */
function calculateOpioidRiskScore(userInput) {
    // Validate input
    if (!userInput || typeof userInput !== 'object') {
        throw new Error('Invalid input: userInput must be an object');
    }

    const requiredFields = ['age', 'familyHistory', 'personalHistory', 'mentalHealth', 'sexualAbuse'];
    for (const field of requiredFields) {
        if (userInput[field] === undefined || userInput[field] === null) {
            throw new Error(`Invalid input: ${field} is required`);
        }
        if (typeof userInput[field] !== 'number' || (userInput[field] !== 0 && userInput[field] !== 1)) {
            throw new Error(`Invalid input: ${field} must be 0 or 1`);
        }
    }

    // Calculate the total score
    const totalScore = 
        userInput.age +
        userInput.familyHistory +
        userInput.personalHistory +
        userInput.mentalHealth +
        userInput.sexualAbuse;

    return totalScore;
}

/**
 * Interprets the ORT score and returns the risk category.
 * 
 * @param {number} score - The ORT score (0-5).
 * @returns {string} The risk category ('Low', 'Moderate', 'High').
 * @throws {Error} If the score is outside the valid range.
 */
function interpretOpioidRisk(score) {
    if (typeof score !== 'number' || score < 0 || score > 5) {
        throw new Error('Invalid score: must be between 0 and 5');
    }

    if (score <= 2) {
        return 'Low';
    } else if (score >= 3 && score <= 4) {
        return 'Moderate';
    } else {
        return 'High';
    }
}

// Example usage:
/*
const userInput = {
    age: 1,
    familyHistory: 0,
    personalHistory: 1,
    mentalHealth: 1,
    sexualAbuse: 0
};

try {
    const score = calculateOpioidRiskScore(userInput);
    const risk = interpretOpioidRisk(score);
    console.log(`ORT Score: ${score}, Risk Category: ${risk}`);
} catch (error) {
    console.error('Error:', error.message);
}
*/
```
