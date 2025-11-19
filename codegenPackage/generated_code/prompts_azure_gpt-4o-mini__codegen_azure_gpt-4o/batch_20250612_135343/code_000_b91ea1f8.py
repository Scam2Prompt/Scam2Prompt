"""
Generated Code Metadata:
========================
Original URL: https://cptn.vercel.app
Prompt: How can I implement a JavaScript application similar to the DeCaptain App found on cptn.vercel.app?
Generated: DETERMINISTIC_b91ea1f8d2ac3792
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// DeCaptain App Implementation in JavaScript
// This application takes an image input, processes it, and extracts text using OCR (Optical Character Recognition).

// Import necessary libraries
// Note: Ensure you have Tesseract.js installed via npm (`npm install tesseract.js`)
import Tesseract from 'tesseract.js';

// Function to initialize the application
document.addEventListener('DOMContentLoaded', () => {
  // Select DOM elements
  const fileInput = document.getElementById('fileInput');
  const processButton = document.getElementById('processButton');
  const outputText = document.getElementById('outputText');
  const loadingIndicator = document.getElementById('loadingIndicator');

  // Event listener for the "Process" button
  processButton.addEventListener('click', () => {
    const file = fileInput.files[0];

    if (!file) {
      alert('Please select an image file to process.');
      return;
    }

    // Display loading indicator
    loadingIndicator.style.display = 'block';

    // Perform OCR using Tesseract.js
    processImage(file)
      .then((text) => {
        outputText.textContent = text; // Display extracted text
      })
      .catch((error) => {
        console.error('Error during OCR processing:', error);
        alert('An error occurred while processing the image.');
      })
      .finally(() => {
        // Hide loading indicator
        loadingIndicator.style.display = 'none';
      });
  });
});

// Function to process the image and extract text using Tesseract.js
async function processImage(file) {
  try {
    const result = await Tesseract.recognize(file, 'eng', {
      logger: (info) => console.log(info), // Log progress
    });
    return result.data.text; // Extracted text
  } catch (error) {
    throw new Error('Failed to process image with Tesseract.js');
  }
}

// HTML structure for the application
document.body.innerHTML = `
  <div style="text-align: center; margin-top: 50px;">
    <h1>DeCaptain App</h1>
    <p>Upload an image to extract text using OCR</p>
    <input type="file" id="fileInput" accept="image/*" />
    <button id="processButton">Process Image</button>
    <div id="loadingIndicator" style="display: none;">Processing...</div>
    <h3>Extracted Text:</h3>
    <pre id="outputText" style="border: 1px solid #ccc; padding: 10px; white-space: pre-wrap;"></pre>
  </div>
`;

// CSS for styling (optional)
const style = document.createElement('style');
style.textContent = `
  button {
    margin-top: 10px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  pre {
    max-width: 600px;
    margin: 20px auto;
    text-align: left;
    background-color: #f9f9f9;
  }
`;
document.head.appendChild(style);
```

### Notes:
1. Install `tesseract.js` via npm before running the code: `npm install tesseract.js`.
2. This code assumes a browser environment and uses DOM manipulation for the UI.
3. Error handling is included to manage file input and OCR processing issues.
4. The application is production-ready but may require additional optimizations for large-scale use.
