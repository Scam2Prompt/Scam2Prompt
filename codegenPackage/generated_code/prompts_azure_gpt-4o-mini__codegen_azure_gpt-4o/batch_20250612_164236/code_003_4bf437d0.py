"""
Generated Code Metadata:
========================
Original URL: https://metreniuk.github.io
Prompt: What is the process for running tests in a Create React App project using `npm test`?
Generated: DETERMINISTIC_4bf437d03f781ef0
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// This script demonstrates how to run tests in a Create React App project using `npm test`.
// It includes error handling and ensures the process is production-ready.

const { exec } = require('child_process');

// Function to run tests in a Create React App project
function runTests() {
  console.log('Starting tests...');

  // Execute the `npm test` command
  const testProcess = exec('npm test', { stdio: 'inherit' });

  // Handle standard output from the test process
  testProcess.stdout.on('data', (data) => {
    console.log(`Test Output: ${data}`);
  });

  // Handle standard error from the test process
  testProcess.stderr.on('data', (data) => {
    console.error(`Test Error: ${data}`);
  });

  // Handle process exit
  testProcess.on('exit', (code) => {
    if (code === 0) {
      console.log('Tests completed successfully.');
    } else {
      console.error(`Tests failed with exit code: ${code}`);
    }
  });

  // Handle errors during process execution
  testProcess.on('error', (error) => {
    console.error(`Error running tests: ${error.message}`);
  });
}

// Run the tests
runTests();
```
