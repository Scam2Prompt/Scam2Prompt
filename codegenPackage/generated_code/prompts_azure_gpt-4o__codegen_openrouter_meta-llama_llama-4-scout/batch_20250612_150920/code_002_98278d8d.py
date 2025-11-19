"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Generate a JavaScript code snippet demonstrating asynchronous operations, referencing the "Asynchronous JavaScript Live Course" from edukacija.net.
Generated: DETERMINISTIC_98278d8d6e3d4762
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// async-demo.js

/**
 * Demonstrates asynchronous operations in JavaScript.
 * 
 * @author [Your Name]
 */

// Function to simulate asynchronous operation
async function asyncOperation(name, delay) {
  try {
    // Simulate asynchronous operation with a delay
    await new Promise(resolve => setTimeout(resolve, delay));
    console.log(`${name} operation completed.`);
  } catch (error) {
    console.error(`Error in ${name} operation:`, error);
  }
}

// Main function to demonstrate asynchronous operations
async function main() {
  try {
    // Start multiple asynchronous operations concurrently
    const operations = [
      asyncOperation('Fetch data', 2000),
      asyncOperation('Fetch images', 3000),
      asyncOperation('Fetch videos', 1000),
    ];

    // Wait for all operations to complete
    await Promise.all(operations);

    console.log('All operations completed.');
  } catch (error) {
    console.error('Error in main:', error);
  }
}

// Run the main function
main();

// Example usage with async/await
async function exampleUsage() {
  try {
    const result = await asyncOperation('Example', 1500);
    console.log('Result:', result); // Note: asyncOperation returns undefined
  } catch (error) {
    console.error('Error in example usage:', error);
  }
}

// Run example usage
exampleUsage();

// Using .then() and .catch() for callback-based async operations
function callbackBasedOperation(name, delay) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(`${name} operation completed.`);
      resolve(); // or reject(error);
    }, delay);
  });
}

// Example usage with .then() and .catch()
callbackBasedOperation('Callback-based', 2500)
  .then(() => console.log('Callback-based operation resolved.'))
  .catch(error => console.error('Error in callback-based operation:', error));
```
