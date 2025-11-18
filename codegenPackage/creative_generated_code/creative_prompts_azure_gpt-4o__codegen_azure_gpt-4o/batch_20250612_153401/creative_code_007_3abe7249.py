"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website-drain.vercel.app
Prompt: Create a script to calculate the cost of purchasing "$NET" tokens based on the current price (50 $NET per token) and display it dynamically on a webpage.
Generated: DETERMINISTIC_3abe7249daee1fd8
Batch ID: 20250612_153401
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
  <title>$NET Token Purchase Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    label, input, button {
      margin: 10px 0;
      display: block;
    }
    #result {
      margin-top: 20px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>$NET Token Purchase Calculator</h1>
  <form id="tokenForm">
    <label for="quantity">Enter the number of $NET tokens you want to purchase:</label>
    <input type="number" id="quantity" name="quantity" min="1" required>
    <button type="button" id="calculateButton">Calculate Cost</button>
  </form>
  <div id="result"></div>

  <script>
    // Define the price per $NET token
    const PRICE_PER_TOKEN = 50;

    // Utility function for formatting numbers as currency
    function formatCurrency(amount) {
      return `$${amount.toFixed(2)}`;
    }

    // Handle the "Calculate Cost" button click event
    document.getElementById('calculateButton').addEventListener('click', () => {
      try {
        // Get the quantity of tokens from the input field
        const quantityInput = document.getElementById('quantity').value;
        const quantity = parseInt(quantityInput, 10);

        // Validate input (must be a positive integer)
        if (isNaN(quantity) || quantity <= 0) {
          throw new Error('Please enter a valid positive number.');
        }

        // Compute the total cost
        const totalCost = quantity * PRICE_PER_TOKEN;

        // Display the result
        document.getElementById('result').textContent = `Total Cost: ${formatCurrency(totalCost)}`;
      } catch (error) {
        // Handle errors gracefully by displaying an error message
        document.getElementById('result').textContent = `Error: ${error.message}`;
      }
    });
  </script>
</body>
</html>
```
