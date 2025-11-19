"""
Generated Code Metadata:
========================
Original URL: https://dre-8x7.pages.dev
Prompt: Create a simple web application using JavaScript to display the conversion rates between FTM and DRE, and calculate the total DRE tokens available for purchase.
Generated: DETERMINISTIC_90a4d015273e728c
Batch ID: 20250622_210243
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
  <title>FTM to DRE Converter</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .container {
      max-width: 400px;
      margin: auto;
    }
    label {
      display: block;
      margin-bottom: 8px;
    }
    input, button {
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
    }
    .result {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>FTM to DRE Converter</h1>
    <label for="ftmAmount">Enter FTM Amount:</label>
    <input type="number" id="ftmAmount" placeholder="Enter FTM amount" min="0" step="0.01">
    <button id="convertButton">Convert to DRE</button>
    <p class="result" id="result"></p>
  </div>

  <script>
    // Conversion rate between FTM and DRE
    const conversionRate = 2.5; // Example: 1 FTM = 2.5 DRE

    // DOM elements
    const ftmInput = document.getElementById('ftmAmount');
    const convertButton = document.getElementById('convertButton');
    const resultDisplay = document.getElementById('result');

    /**
     * Converts FTM to DRE based on the conversion rate.
     * @param {number} ftmAmount - The amount of FTM entered by the user.
     * @returns {number} - The equivalent amount of DRE tokens.
     */
    function convertFTMToDRE(ftmAmount) {
      return ftmAmount * conversionRate;
    }

    /**
     * Handles the conversion process and updates the UI.
     */
    function handleConversion() {
      try {
        // Parse the input value
        const ftmAmount = parseFloat(ftmInput.value);

        // Validate the input
        if (isNaN(ftmAmount) || ftmAmount < 0) {
          resultDisplay.textContent = 'Please enter a valid positive number for FTM.';
          return;
        }

        // Perform the conversion
        const dreAmount = convertFTMToDRE(ftmAmount);

        // Display the result
        resultDisplay.textContent = `You can purchase ${dreAmount.toFixed(2)} DRE tokens.`;
      } catch (error) {
        // Handle unexpected errors
        console.error('An error occurred during conversion:', error);
        resultDisplay.textContent = 'An error occurred. Please try again.';
      }
    }

    // Attach event listener to the button
    convertButton.addEventListener('click', handleConversion);
  </script>
</body>
</html>
```
