"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-presales1.pages.dev
Prompt: Create a web interface using HTML and JavaScript for users to input their BASE investment amount and display the corresponding JESSE tokens they will receive based on the presale rates.
Generated: DETERMINISTIC_a76db300102b70d4
Batch ID: 20250612_153225
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
  <title>Investment Converter</title>
  <style>
    /* Basic styling for the interface */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      background-color: #f4f4f4;
    }
    .container {
      width: 100%;
      max-width: 400px;
      background: white;
      padding: 20px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
      border-radius: 8px;
    }
    h1 {
      margin: 0;
      font-size: 24px;
      text-align: center;
    }
    label {
      display: block;
      margin-top: 15px;
      font-weight: bold;
    }
    input {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }
    button {
      width: 100%;
      padding: 10px;
      margin-top: 20px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #0056b3;
    }
    .result {
      margin-top: 20px;
      font-size: 18px;
      text-align: center;
      font-weight: bold;
      color: #333;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Investment Converter</h1>
    <form id="investmentForm">
      <label for="baseAmount">Enter BASE Investment Amount:</label>
      <input type="number" id="baseAmount" name="baseAmount" placeholder="e.g., 100" required min="0" step="0.01">
      <button type="button" id="calculateButton">Calculate JESSE Tokens</button>
    </form>
    <div id="result" class="result"></div>
  </div>

  <script>
    // Presale rate for JESSE tokens (change as needed)
    const PRESALE_RATE = 10; // 1 BASE unit gives 10 JESSE tokens

    /**
     * Function to calculate JESSE tokens based on BASE investment
     * @param {number} baseAmount - The BASE investment amount
     * @returns {number} - The equivalent number of JESSE tokens
     */
    function calculateJesseTokens(baseAmount) {
      if (isNaN(baseAmount) || baseAmount < 0) {
        throw new Error('Invalid BASE investment amount');
      }
      return baseAmount * PRESALE_RATE;
    }

    // DOM references
    const baseAmountInput = document.getElementById('baseAmount');
    const calculateButton = document.getElementById('calculateButton');
    const resultDiv = document.getElementById('result');

    // Event listener for the calculate button
    calculateButton.addEventListener('click', () => {
      try {
        // Parse the input value
        const baseAmount = parseFloat(baseAmountInput.value);

        // Perform calculation
        const jesseTokens = calculateJesseTokens(baseAmount);

        // Display the result
        resultDiv.textContent = `You will receive ${jesseTokens} JESSE tokens.`;
      } catch (error) {
        // Handle errors gracefully
        resultDiv.textContent = 'Error: ' + error.message;
      }
    });
  </script>
</body>
</html>
```
