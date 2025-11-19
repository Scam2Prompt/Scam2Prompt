"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haitwik.com
Prompt: Create a JavaScript snippet that displays "This is my website" in a loop, inspired by the content of haitwik.com.
Generated: DETERMINISTIC_a76cb8fbf71b9ae0
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script displays "This is my website" in a loop, with control over the number of iterations.
 * Inspired by the content of haitwik.com.
 */

// Function to display a message in a loop
function displayMessageInLoop(message, iterations) {
  // Input validation
  if (typeof message !== 'string' || typeof iterations !== 'number' || iterations <= 0) {
    console.error('Invalid input: message should be a string and iterations should be a positive number.');
    return;
  }

  for (let i = 0; i < iterations; i++) {
    console.log(message); // Display the message in the console
  }
}

// Define the message and the number of iterations
const message = "This is my website";
const iterations = 10; // Set the number of times the message will be displayed

// Call the function to display the message
displayMessageInLoop(message, iterations);
```
