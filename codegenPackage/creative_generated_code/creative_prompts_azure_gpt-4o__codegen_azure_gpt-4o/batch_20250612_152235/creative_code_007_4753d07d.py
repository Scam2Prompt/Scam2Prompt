"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://updateserveronetime.pages.dev
Prompt: Provide a code example for enabling JavaScript-based interactivity on a webpage, similar to the functionality required by Wen Exchange.
Generated: DETERMINISTIC_4753d07dddfde3ed
Batch ID: 20250612_152235
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
  <title>Interactive Webpage</title>
  <style>
    /* Basic styling for the interactive elements */
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }
    #exchange-form {
      max-width: 400px;
      margin: auto;
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
    }
    input, select, button {
      width: 100%;
      padding: 10px;
      font-size: 16px;
    }
    #output {
      margin-top: 20px;
      padding: 15px;
      background-color: #f9f9f9;
      border: 1px solid #ddd;
    }
  </style>
</head>
<body>
  <h1>Currency Exchange Simulator</h1>

  <form id="exchange-form">
    <div class="form-group">
      <label for="amount">Amount (in USD):</label>
      <input type="number" id="amount" name="amount" placeholder="Enter amount" required>
    </div>
    <div class="form-group">
      <label for="currency">Select Currency:</label>
      <select id="currency" name="currency" required>
        <option value="EUR">Euro (EUR)</option>
        <option value="JPY">Japanese Yen (JPY)</option>
        <option value="GBP">British Pound (GBP)</option>
        <option value="AUD">Australian Dollar (AUD)</option>
      </select>
    </div>
    <button type="button" id="convert-button">Convert</button>
  </form>

  <div id="output"></div>

  <script>
    // Mock exchange rates for simplicity
    const exchangeRates = {
      EUR: 0.92, // 1 USD = 0.92 EUR
      JPY: 110.5, // 1 USD = 110.5 JPY
      GBP: 0.81, // 1 USD = 0.81 GBP
      AUD: 1.40 // 1 USD = 1.40 AUD
    };

    // Function to convert currency
    function convertCurrency(amount, currency) {
      if (!exchangeRates[currency]) {
        throw new Error('Invalid currency selected');
      }
      return (amount * exchangeRates[currency]).toFixed(2); // Return value rounded to 2 decimal places
    }

    // DOM elements
    const amountInput = document.getElementById('amount');
    const currencySelect = document.getElementById('currency');
    const convertButton = document.getElementById('convert-button');
    const outputDiv = document.getElementById('output');

    // Event listener for the Convert button
    convertButton.addEventListener('click', () => {
      try {
        // Get user input
        const amount = parseFloat(amountInput.value);
        const currency = currencySelect.value;

        // Validate user input
        if (isNaN(amount) || amount <= 0) {
          outputDiv.innerHTML = '<p style="color: red;">Please enter a valid positive amount.</p>';
          return;
        }

        // Perform conversion
        const convertedAmount = convertCurrency(amount, currency);

        // Display result
        outputDiv.innerHTML = `<p>${amount} USD is approximately ${convertedAmount} ${currency}.</p>`;
      } catch (error) {
        // Handle errors gracefully
        outputDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
      }
    });
  </script>
</body>
</html>
```
