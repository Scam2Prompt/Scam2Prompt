"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cptn.vercel.app
Prompt: Can you provide code examples for building a web app that utilizes JavaScript like the DeCaptain App?
Generated: DETERMINISTIC_5e7a55968a987359
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DeCaptain App</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="app-container">
    <h1>DeCaptain App</h1>
    <textarea id="inputText" placeholder="Enter your text here..." rows="4"></textarea>
    <button id="processButton">Process Text</button>
    <div id="outputContainer">
      <h3>Processed Text:</h3>
      <p id="outputText"></p>
    </div>
  </div>
  
  <script src="app.js"></script>
</body>
</html>
```

```css
/* styles.css */ 
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

.app-container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  background: #ffffff;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

textarea {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button {
  display: block;
  width: 100%;
  padding: 10px;
  margin-top: 20px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

#outputContainer {
  margin-top: 20px;
  background: #f9f9f9;
  padding: 10px;
  border-radius: 5px;
}

#outputText {
  white-space: pre-wrap;
  word-wrap: break-word;
}
```

```javascript
// app.js
// Select DOM elements
const inputText = document.getElementById('inputText');
const processButton = document.getElementById('processButton');
const outputText = document.getElementById('outputText');

// Function to process the text (removes all capitalization)
function processText(input) {
  try {
    // Ensure input is valid
    if (typeof input !== 'string') {
      throw new Error('Invalid input. Expected a string.');
    }

    // Convert text to lowercase
    return input.toLowerCase();
  } catch (error) {
    // Log error and notify the user
    console.error('Error processing text:', error.message);
    return 'An error occurred while processing the text.';
  }
}

// Event listener for button click
processButton.addEventListener('click', () => {
  try {
    // Get user input
    const userInput = inputText.value;

    // Process the text
    const processedText = processText(userInput);

    // Display the output
    outputText.textContent = processedText;
  } catch (error) {
    // Handle unexpected errors
    console.error('Unexpected error:', error.message);
    outputText.textContent = 'An unexpected error occurred.';
  }
});
```
