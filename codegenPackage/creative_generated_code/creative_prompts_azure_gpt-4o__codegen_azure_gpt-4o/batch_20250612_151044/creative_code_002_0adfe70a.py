"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange24h.com
Prompt: Generate code in JavaScript to create a responsive user interface for slot deposit transactions, incorporating features like "promo khusus" and "modal kecil" as described on the site.
Generated: DETERMINISTIC_0adfe70af8688527
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Slot Deposit Transactions UI - Responsive and User-Friendly

// HTML structure for the responsive UI
const htmlTemplate = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Slot Deposit Transactions</title>
  <style>
    /* Basic styling for the responsive UI */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
      color: #333;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }

    .header {
      text-align: center;
      background-color: #4CAF50;
      color: white;
      padding: 10px;
    }

    .promo, .deposit {
      margin-top: 20px;
      padding: 15px;
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .promo h2, .deposit h2 {
      margin: 0 0 10px;
    }

    .promo input, .deposit input, .deposit button {
      display: block;
      width: 100%;
      margin: 10px 0;
      padding: 10px;
      font-size: 16px;
    }

    .deposit button {
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }

    .deposit button:hover {
      background-color: #45a049;
    }

    @media (max-width: 768px) {
      .promo, .deposit {
        padding: 10px;
      }

      .promo h2, .deposit h2 {
        font-size: 20px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>Responsive Slot Deposit Transactions</h1>
    </div>
    <!-- Promo Section -->
    <div class="promo">
      <h2>Promo Khusus</h2>
      <input type="text" id="promoCode" placeholder="Enter your promo code here">
      <button id="applyPromo">Apply Promo</button>
      <p id="promoMessage"></p>
    </div>

    <!-- Deposit Section -->
    <div class="deposit">
      <h2>Modal Kecil</h2>
      <input type="number" id="depositAmount" placeholder="Enter deposit amount">
      <button id="submitDeposit">Submit Deposit</button>
      <p id="depositMessage"></p>
    </div>
  </div>

  <script>
    // JavaScript for functionality

    // Select DOM elements
    const promoCodeInput = document.getElementById('promoCode');
    const applyPromoButton = document.getElementById('applyPromo');
    const promoMessage = document.getElementById('promoMessage');

    const depositAmountInput = document.getElementById('depositAmount');
    const submitDepositButton = document.getElementById('submitDeposit');
    const depositMessage = document.getElementById('depositMessage');

    // Error handling helper function
    function handleError(message) {
      return { success: false, message };
    }

    // Success handling helper function
    function handleSuccess(message) {
      return { success: true, message };
    }

    // Apply promo button click event
    applyPromoButton.addEventListener('click', () => {
      const promoCode = promoCodeInput.value.trim();

      if (!promoCode) {
        const error = handleError('Promo code cannot be empty.');
        promoMessage.textContent = error.message;
        promoMessage.style.color = 'red';
        return;
      }

      // Simulate promo code validation
      if (promoCode === 'PROMO50') {
        const success = handleSuccess('Promo applied successfully! You get 50% off.');
        promoMessage.textContent = success.message;
        promoMessage.style.color = 'green';
      } else {
        const error = handleError('Invalid promo code.');
        promoMessage.textContent = error.message;
        promoMessage.style.color = 'red';
      }
    });

    // Submit deposit button click event
    submitDepositButton.addEventListener('click', () => {
      const depositAmount = parseFloat(depositAmountInput.value);

      if (isNaN(depositAmount) || depositAmount <= 0) {
        const error = handleError('Please enter a valid deposit amount.');
        depositMessage.textContent = error.message;
        depositMessage.style.color = 'red';
        return;
      }

      // Simulate deposit submission
      const success = handleSuccess(`Deposit of $${depositAmount.toFixed(2)} submitted successfully.`);
      depositMessage.textContent = success.message;
      depositMessage.style.color = 'green';
    });
  </script>
</body>
</html>
```
