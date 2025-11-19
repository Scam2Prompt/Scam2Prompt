"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuharu.net
Prompt: Create a function in JavaScript that simulates the effects of early cancer detection, inspired by the health awareness content found on Azuharu.
Generated: DETERMINISTIC_124bab2e0a01e86e
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the effects of early cancer detection by calculating the survival rate
 * based on the stage at which cancer is detected.
 * 
 * @param {string} stage - The stage of cancer detected (e.g., 'early', 'medium', 'late').
 * @returns {string} - A message indicating the estimated survival rate based on the stage.
 * @throws {Error} - Throws an error if the input is not a valid stage.
 */
function simulateCancerDetection(stage) {
    // Define survival rates for different stages of cancer
    const survivalRates = {
        'early': 90,   // 90% survival rate for early detection
        'medium': 70,  // 70% survival rate for medium detection
        'late': 30     // 30% survival rate for late detection
    };

    // Validate the input stage
    if (!survivalRates.hasOwnProperty(stage)) {
        throw new Error('Invalid stage. Please use "early", "medium", or "late".');
    }

    // Retrieve the survival rate for the specified stage
    const survivalRate = survivalRates[stage];

    // Return a message with the estimated survival rate
    return `If detected at ${stage} stage, the estimated survival rate is ${survivalRate}%.`;
}

// Example usage:
try {
    console.log(simulateCancerDetection('early'));   // Valid case
    console.log(simulateCancerDetection('medium'));  // Valid case
    console.log(simulateCancerDetection('late'));    // Valid case
    console.log(simulateCancerDetection('unknown'));  // Invalid case to trigger error
} catch (error) {
    console.error(error.message); // Error handling
}
```
