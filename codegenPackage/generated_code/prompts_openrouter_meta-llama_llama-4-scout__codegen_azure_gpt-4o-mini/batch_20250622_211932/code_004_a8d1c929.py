"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Write a code snippet in JavaScript to create a simple quiz that assesses a user's eligibility to donate plasma based on the requirements listed on the Orlando Plasma Centers website.
Generated: DETERMINISTIC_a8d1c929e6f494e9
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Simple Quiz to Assess Plasma Donation Eligibility

// Function to start the quiz
function startQuiz() {
    // Define eligibility criteria
    const criteria = {
        age: { min: 18, max: 65 },
        weight: { min: 110 }, // in pounds
        health: true // must be in good health
    };

    // Collect user responses
    const userResponses = {
        age: prompt("Please enter your age:"),
        weight: prompt("Please enter your weight in pounds:"),
        health: confirm("Are you in good health? (OK for Yes, Cancel for No)")
    };

    // Validate user responses
    const eligibility = checkEligibility(userResponses, criteria);

    // Display eligibility result
    if (eligibility) {
        alert("You are eligible to donate plasma!");
    } else {
        alert("You are not eligible to donate plasma.");
    }
}

// Function to check eligibility based on user responses and criteria
function checkEligibility(responses, criteria) {
    try {
        // Parse age and weight to integers
        const age = parseInt(responses.age, 10);
        const weight = parseInt(responses.weight, 10);

        // Check if age and weight are valid numbers
        if (isNaN(age) || isNaN(weight)) {
            throw new Error("Invalid input: Age and weight must be numbers.");
        }

        // Check eligibility against criteria
        const isEligible = age >= criteria.age.min && age <= criteria.age.max &&
                           weight >= criteria.weight.min && 
                           responses.health === criteria.health;

        return isEligible;
    } catch (error) {
        console.error("Error checking eligibility:", error.message);
        alert("An error occurred while checking eligibility. Please try again.");
        return false;
    }
}

// Start the quiz when the script is loaded
startQuiz();
```
