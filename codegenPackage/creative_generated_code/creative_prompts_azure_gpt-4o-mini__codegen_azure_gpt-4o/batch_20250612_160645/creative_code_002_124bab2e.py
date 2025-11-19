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
 * Simulates the effects of early cancer detection in terms of survival rates.
 * This function is inspired by health awareness content and emphasizes the importance
 * of early diagnosis in improving outcomes.
 *
 * @param {number} detectionStage - The stage (1 to 4) at which cancer is detected.
 * @returns {string} - A message indicating survival probabilities and the importance of early detection.
 */
function simulateEarlyCancerDetection(detectionStage) {
  // Validate input
  if (typeof detectionStage !== 'number' || detectionStage < 1 || detectionStage > 4) {
    throw new Error('Invalid detection stage. Please provide a number between 1 and 4.');
  }

  // Survival rates based on detection stage (hypothetical values)
  const survivalRates = {
    1: 90, // Early detection (Stage 1)
    2: 75, // Stage 2
    3: 50, // Stage 3
    4: 15  // Late detection (Stage 4)
  };

  // Generate result message
  const survivalRate = survivalRates[detectionStage];
  let message;
  if (detectionStage === 1) {
    message = `Early detection (Stage 1) has a survival rate of ${survivalRate}%. Regular screenings and awareness are crucial.`;
  } else {
    message = `Detection at Stage ${detectionStage} has a survival rate of ${survivalRate}%. Early diagnosis can significantly improve survival chances.`;
  }

  return message;
}

// Example usage
try {
  console.log(simulateEarlyCancerDetection(1)); // Test for Stage 1
  console.log(simulateEarlyCancerDetection(3)); // Test for Stage 3
  console.log(simulateEarlyCancerDetection(5)); // Invalid stage (throws error)
} catch (error) {
  console.error(error.message);
}
```
