"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Write a script in Node.js that validates user eligibility for Everyworld participation based on country restrictions and age requirements.
Generated: DETERMINISTIC_3839b18db1567491
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const readline = require('readline');

// Configuration: Define eligibility criteria
const ELIGIBLE_COUNTRIES = ['USA', 'Canada', 'UK', 'Australia', 'Germany'];
const MINIMUM_AGE = 18;

// Create a readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Function to validate eligibility
function validateEligibility(country, age) {
  try {
    // Check if country is eligible
    if (!ELIGIBLE_COUNTRIES.includes(country)) {
      return {
        eligible: false,
        reason: `Your country (${country}) is not eligible for Everyworld participation.`,
      };
    }

    // Check if age meets the minimum requirement
    if (age < MINIMUM_AGE) {
      return {
        eligible: false,
        reason: `You must be at least ${MINIMUM_AGE} years old to participate.`,
      };
    }

    // If both checks pass, user is eligible
    return {
      eligible: true,
      reason: 'You meet the eligibility criteria for Everyworld participation.',
    };
  } catch (error) {
    // Handle potential errors gracefully
    return {
      eligible: false,
      reason: 'An unexpected error occurred during validation.',
      error: error.message,
    };
  }
}

// Prompt user for input
rl.question('Please enter your country: ', (country) => {
  rl.question('Please enter your age: ', (ageInput) => {
    const age = parseInt(ageInput, 10);

    // Validate age input
    if (isNaN(age) || age < 0) {
      console.log('Invalid age input. Please enter a valid number.');
      rl.close();
      return;
    }

    // Perform eligibility check
    const result = validateEligibility(country, age);

    // Output the result
    if (result.eligible) {
      console.log('Congratulations! ' + result.reason);
    } else {
      console.log('Sorry! ' + result.reason);
    }

    // Close the readline interface
    rl.close();
  });
});
```
