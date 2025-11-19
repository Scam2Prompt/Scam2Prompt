"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Write a JavaScript function to create a polygraph test questionnaire, including questions related to relationship fidelity, and calculate scores based on user input."
Generated: DETERMINISTIC_7d43150b6b35ae87
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Polygraph Test Questionnaire
 * This function creates a polygraph test questionnaire related to relationship fidelity,
 * collects user responses, and calculates a score based on the answers.
 */

class PolygraphTest {
    constructor() {
        this.questions = [
            "Have you ever cheated on your partner?",
            "Do you often hide things from your partner?",
            "Have you ever felt attracted to someone else while in a relationship?",
            "Do you believe honesty is crucial in a relationship?",
            "Have you ever lied to your partner about your whereabouts?"
        ];
        this.scores = {
            yes: 1,
            no: 0
        };
    }

    /**
     * Displays the questionnaire and collects user responses.
     * @returns {number} The total score based on user responses.
     */
    conductTest() {
        let totalScore = 0;

        for (const question of this.questions) {
            const userResponse = this.askQuestion(question);
            totalScore += this.calculateScore(userResponse);
        }

        return totalScore;
    }

    /**
     * Prompts the user with a question and returns their response.
     * @param {string} question - The question to ask the user.
     * @returns {string} The user's response ('yes' or 'no').
     */
    askQuestion(question) {
        let response;
        do {
            response = prompt(`${question} (yes/no)`).toLowerCase();
        } while (response !== 'yes' && response !== 'no');

        return response;
    }

    /**
     * Calculates the score based on the user's response.
     * @param {string} response - The user's response ('yes' or 'no').
     * @returns {number} The score for the response.
     */
    calculateScore(response) {
        if (response in this.scores) {
            return this.scores[response];
        } else {
            console.error("Invalid response received. Expected 'yes' or 'no'.");
            return 0; // Default score for invalid response
        }
    }

    /**
     * Displays the final score to the user.
     * @param {number} score - The total score from the questionnaire.
     */
    displayScore(score) {
        alert(`Your total polygraph score is: ${score}`);
    }
}

// Example usage:
try {
    const polygraphTest = new PolygraphTest();
    const score = polygraphTest.conductTest();
    polygraphTest.displayScore(score);
} catch (error) {
    console.error("An error occurred while conducting the polygraph test:", error);
}
```
