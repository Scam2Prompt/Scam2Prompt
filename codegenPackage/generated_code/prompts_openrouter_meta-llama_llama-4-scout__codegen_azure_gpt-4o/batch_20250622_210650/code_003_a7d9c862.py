"""
Generated Code Metadata:
========================
Original URL: https://signup-echo.pages.dev
Prompt: "Write a code example for a simple web page that requires JavaScript to display its main functionality, inspired by Echo's approach."
Generated: DETERMINISTIC_a7d9c8626beda42d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Echo Functionality</title>
  <style>
    /* Basic styling for the page */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    .container {
      text-align: center;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    input[type="text"] {
      width: 80%;
      padding: 10px;
      margin: 10px 0;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    button {
      padding: 10px 20px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }

    .output {
      margin-top: 20px;
      font-size: 1.2em;
      color: #333;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Echo Functionality</h1>
    <p>Type something below and click "Echo" to see it displayed:</p>
    <input type="text" id="userInput" placeholder="Enter text here">
    <button id="echoButton">Echo</button>
    <div class="output" id="output"></div>
  </div>

  <script>
    // Select DOM elements
    const userInput = document.getElementById('userInput');
    const echoButton = document.getElementById('echoButton');
    const output = document.getElementById('output');

    // Add event listener to the button
    echoButton.addEventListener('click', () => {
      try {
        // Get the input value
        const inputValue = userInput.value.trim();

        // Check if the input is empty
        if (!inputValue) {
          throw new Error('Input cannot be empty.');
        }

        // Display the input value in the output div
        output.textContent = inputValue;
      } catch (error) {
        // Handle errors gracefully
        output.textContent = error.message;
      }
    });
  </script>
</body>
</html>
```
