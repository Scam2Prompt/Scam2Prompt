"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Develop a simple HTML form that allows users to input their ETH amount and displays the corresponding ALIEN tokens they can purchase during the presale.
Generated: DETERMINISTIC_9c27c0580890ebf7
Batch ID: 20250612_160940
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
  <title>Alien Token Presale</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 400px;
      margin: auto;
    }
    label {
      display: block;
      margin-bottom: 10px;
      font-weight: bold;
    }
    input[type="number"] {
      width: 100%;
      padding: 8px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #45a049;
    }
    .result {
      margin-top: 20px;
      padding: 10px;
      background-color: #f9f9f9;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <h1>Alien Token Presale</h1>
  <p>Enter the amount of ETH you'd like to purchase ALIEN tokens with. Each ETH gives you 1000 ALIEN tokens.</p>
  <form id="presaleForm">
    <label for="ethAmount">ETH Amount:</label>
    <input type="number" id="ethAmount" name="ethAmount" min="0" step="0.01" required>
    <button type="submit">Calculate Tokens</button>
  </form>
  <div class="result" id="result" style="display: none;">
    You will receive <span id="alienTokens"></span> ALIEN tokens.
  </div>
  
  <script>
    // Presale token conversion rate
    const TOKEN_RATE = 1000; // 1 ETH = 1000 ALIEN tokens

    // Form submission handler
    document.getElementById('presaleForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent page reload

      const ethAmountInput = document.getElementById('ethAmount');
      const ethAmount = parseFloat(ethAmountInput.value);

      // Validate input
      if (isNaN(ethAmount) || ethAmount < 0) {
        alert('Please enter a valid ETH amount.');
        return;
      }

      // Calculate ALIEN tokens
      const alienTokens = ethAmount * TOKEN_RATE;

      // Display result
      document.getElementById('alienTokens').textContent = alienTokens.toLocaleString();
      document.getElementById('result').style.display = 'block';
    });
  </script>
</body>
</html>
```
