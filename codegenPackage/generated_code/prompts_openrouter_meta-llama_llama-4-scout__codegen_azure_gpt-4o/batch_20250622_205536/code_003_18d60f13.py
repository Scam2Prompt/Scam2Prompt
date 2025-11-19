"""
Generated Code Metadata:
========================
Original URL: https://swaplab.io
Prompt: Design a simple cryptocurrency exchange interface using HTML, CSS, and JavaScript, inspired by SWAPLAB's user-friendly design and featuring a float rate and fixed rate exchange option.
Generated: DETERMINISTIC_18d60f136c83097f
Batch ID: 20250622_205536
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
  <title>Cryptocurrency Exchange</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Crypto Exchange</h1>
  </header>
  <main>
    <section class="exchange-form">
      <h2>Exchange Cryptocurrency</h2>
      <form id="exchangeForm">
        <!-- Select cryptocurrency to send -->
        <label for="sendCurrency">Send:</label>
        <select id="sendCurrency" name="sendCurrency" required>
          <option value="BTC">Bitcoin (BTC)</option>
          <option value="ETH">Ethereum (ETH)</option>
          <option value="LTC">Litecoin (LTC)</option>
        </select>

        <!-- Input amount to send -->
        <label for="sendAmount">Amount:</label>
        <input type="number" id="sendAmount" name="sendAmount" min="0.0001" step="0.0001" required>

        <!-- Select cryptocurrency to receive -->
        <label for="receiveCurrency">Receive:</label>
        <select id="receiveCurrency" name="receiveCurrency" required>
          <option value="BTC">Bitcoin (BTC)</option>
          <option value="ETH">Ethereum (ETH)</option>
          <option value="LTC">Litecoin (LTC)</option>
        </select>

        <!-- Input recipient address -->
        <label for="recipientAddress">Recipient Address:</label>
        <input type="text" id="recipientAddress" name="recipientAddress" required>

        <!-- Exchange rate options -->
        <fieldset>
          <legend>Exchange Rate</legend>
          <label>
            <input type="radio" name="rateType" value="float" checked>
            Float Rate
          </label>
          <label>
            <input type="radio" name="rateType" value="fixed">
            Fixed Rate
          </label>
        </fieldset>

        <!-- Submit button -->
        <button type="submit">Exchange</button>
      </form>
    </section>
    <section id="result" class="result">
      <!-- Result will be displayed here -->
    </section>
  </main>
  <footer>
    <p>&copy; 2023 Crypto Exchange</p>
  </footer>
  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
  color: #333;
}

header {
  background-color: #4CAF50;
  color: white;
  padding: 1rem;
  text-align: center;
}

main {
  padding: 2rem;
}

footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 1rem;
  position: fixed;
  bottom: 0;
  width: 100%;
}

/* Exchange form styles */
.exchange-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  margin: 0 auto;
}

.exchange-form h2 {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin: 0.5rem 0 0.2rem;
}

input, select, button {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

/* Result section styles */
.result {
  margin-top: 2rem;
  text-align: center;
}
```

```javascript
// script.js

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
  const exchangeForm = document.getElementById('exchangeForm');
  const resultSection = document.getElementById('result');

  // Handle form submission
  exchangeForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Gather form data
    const sendCurrency = document.getElementById('sendCurrency').value;
    const sendAmount = parseFloat(document.getElementById('sendAmount').value);
    const receiveCurrency = document.getElementById('receiveCurrency').value;
    const recipientAddress = document.getElementById('recipientAddress').value;
    const rateType = document.querySelector('input[name="rateType"]:checked').value;

    // Validate input
    if (sendCurrency === receiveCurrency) {
      alert('Send and Receive currencies must be different.');
      return;
    }

    if (sendAmount <= 0) {
      alert('Amount must be greater than zero.');
      return;
    }

    // Simulate API call to calculate exchange rate
    try {
      const exchangeRate = await getExchangeRate(sendCurrency, receiveCurrency, rateType);
      const receiveAmount = (sendAmount * exchangeRate).toFixed(8);

      // Display result
      resultSection.innerHTML = `
        <h3>Exchange Summary</h3>
        <p>Send: ${sendAmount} ${sendCurrency}</p>
        <p>Receive: ${receiveAmount} ${receiveCurrency}</p>
        <p>Recipient Address: ${recipientAddress}</p>
        <p>Rate Type: ${rateType}</p>
      `;
    } catch (error) {
      console.error('Error fetching exchange rate:', error);
      alert('Failed to fetch exchange rate. Please try again later.');
    }
  });

  // Mock function to simulate fetching exchange rate from an API
  async function getExchangeRate(sendCurrency, receiveCurrency, rateType) {
    // Simulate network delay
    await new Promise((resolve) => setTimeout(resolve, 1000));

    // Mock exchange rates (for demonstration purposes)
    const mockRates = {
      BTC_ETH: 15.0,
      ETH_BTC: 0.0667,
      BTC_LTC: 200.0,
      LTC_BTC: 0.005,
      ETH_LTC: 13.33,
      LTC_ETH: 0.075,
    };

    const key = `${sendCurrency}_${receiveCurrency}`;
    const rate = mockRates[key];

    if (!rate) {
      throw new Error('Exchange rate not available for selected currencies.');
    }

    // Adjust rate based on rate type
    return rateType === 'fixed' ? rate : rate * (1 + Math.random() * 0.02 - 0.01); // Float rate with slight variation
  }
});
```
