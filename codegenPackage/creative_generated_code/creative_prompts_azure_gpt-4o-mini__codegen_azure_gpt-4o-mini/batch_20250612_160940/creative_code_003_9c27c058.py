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
    <title>ETH to ALIEN Token Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        .container {
            max-width: 400px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        input[type="number"], button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>ETH to ALIEN Token Calculator</h1>
        <form id="ethForm">
            <label for="ethAmount">Enter ETH Amount:</label>
            <input type="number" id="ethAmount" step="0.01" min="0" required>
            <button type="submit">Calculate ALIEN Tokens</button>
        </form>
        <div class="result" id="result"></div>
    </div>

    <script>
        // Define the ALIEN token conversion rate
        const ALIEN_RATE = 500; // 1 ETH = 500 ALIEN tokens

        // Get references to the form and result output
        const form = document.getElementById('ethForm');
        const resultDiv = document.getElementById('result');

        // Function to handle form submission
        form.addEventListener('submit', function(event) {
            // Prevent the default form submission behavior
            event.preventDefault();
            
            // Get the input value for ETH amount
            const ethAmount = parseFloat(document.getElementById('ethAmount').value);
            
            // Check if the ETH amount is valid
            if (isNaN(ethAmount) || ethAmount < 0) {
                resultDiv.textContent = 'Please enter a valid ETH amount.';
                return;
            }

            // Calculate the corresponding ALIEN tokens
            const alienTokens = ethAmount * ALIEN_RATE;

            // Display the result
            resultDiv.textContent = `${ethAmount} ETH can purchase ${alienTokens} ALIEN tokens.`;
        });
    </script>
</body>
</html>
```
