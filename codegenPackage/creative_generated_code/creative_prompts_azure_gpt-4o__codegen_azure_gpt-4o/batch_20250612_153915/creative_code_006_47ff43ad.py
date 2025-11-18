"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pikmisobakilive.com
Prompt: Write HTML and JavaScript code to create a "Claim Reward" button that connects to a TON wallet and confirms the transaction upon user interaction.
Generated: DETERMINISTIC_47ff43ad1b47ce52
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/@tonconnect/sdk": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Claim Reward</title>
  <!-- Add TON Connect SDK -->
  <script src="https://cdn.jsdelivr.net/npm/@tonconnect/sdk"></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background-color: #f4f4f9;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      border: none;
      border-radius: 5px;
      background-color: #4CAF50; /* Green */
      color: white;
    }
    button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <!-- Claim Reward Button -->
  <button id="claimRewardButton">Claim Reward</button>

  <script>
    // Initialize TON Connect
    (async () => {
      try {
        const TONConnect = new TonConnect();

        // Set up the button click handler
        document.getElementById('claimRewardButton').addEventListener('click', async () => {
          try {
            // Connect to the TON wallet
            const wallet = await TONConnect.connect();

            if (!wallet) {
              alert('Wallet connection failed.');
              return;
            }

            // Create the transaction payload
            const transaction = {
              to: 'EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c', // Replace with the recipient address
              value: '1000000000', // Amount to transfer in nanograms (1 TON = 1e9 nanograms)
              stateInit: undefined, // Optional: state initialization data
              payload: undefined, // Optional: additional payload data
            };

            // Send the transaction
            const result = await wallet.sendTransaction(transaction);

            if (result) {
              alert('Reward has been claimed successfully!');
            } else {
              alert('Transaction failed.');
            }
          } catch (error) {
            console.error(error);
            alert('An error occurred while processing the transaction.');
          }
        });
      } catch (error) {
        console.error('Error initializing TON Connect:', error);
        alert('Failed to initialize TON Connect.');
      }
    })();
  </script>
</body>
</html>
```
