"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Create a frontend HTML/JavaScript interface for a cryptocurrency presale, allowing users to select ETH amounts (0.5, 1, 1.5, 2, or 3 ETH) and purchase KSI tokens at the specified rate.
Generated: DETERMINISTIC_8cf408c650eba6d5
Batch ID: 20250612_152827
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
  <title>Cryptocurrency Presale</title>
  <!-- Link to a CSS file for styling (optional) -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>KSI Token Presale</h1>
    <p>Purchase KSI tokens using ETH.</p>
  </header>

  <!-- Presale Form -->
  <main>
    <form id="presaleForm">
      <h2>Select ETH Amount</h2>
      <label>
        <input type="radio" name="ethAmount" value="0.5" required> 0.5 ETH
      </label>
      <label>
        <input type="radio" name="ethAmount" value="1"> 1 ETH
      </label>
      <label>
        <input type="radio" name="ethAmount" value="1.5"> 1.5 ETH
      </label>
      <label>
        <input type="radio" name="ethAmount" value="2"> 2 ETH
      </label>
      <label>
        <input type="radio" name="ethAmount" value="3"> 3 ETH
      </label>

      <button type="button" id="purchaseButton">Purchase KSI Tokens</button>
    </form>
    <div id="confirmationMessage"></div>
  </main>

  <!-- JavaScript Code -->
  <script>
    // Constants
    const KSI_RATE = 1000; // Tokens per ETH

    // Event Listener for the Purchase Button
    document.getElementById('purchaseButton').addEventListener('click', () => {
      const form = document.getElementById('presaleForm');
      const selectedEthAmount = form.ethAmount.value;

      // Error Handling: Check if an ETH amount is selected
      if (!selectedEthAmount) {
        alert('Please select an ETH amount.');
        return;
      }

      // Calculate the KSI tokens to be received
      const ethAmount = parseFloat(selectedEthAmount);
      const ksiTokens = ethAmount * KSI_RATE;

      // Display Confirmation Message
      const confirmationMessage = `You have purchased ${ksiTokens} KSI tokens for ${ethAmount} ETH.`;
      document.getElementById('confirmationMessage').innerText = confirmationMessage;
    });
  </script>
</body>
</html>
```
