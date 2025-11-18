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
    <title>KSI Token Presale</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>KSI Token Presale</h1>
        <form id="presaleForm">
            <label for="ethAmount">Select ETH Amount:</label>
            <select id="ethAmount" required>
                <option value="" disabled selected>Select an amount</option>
                <option value="0.5">0.5 ETH</option>
                <option value="1">1 ETH</option>
                <option value="1.5">1.5 ETH</option>
                <option value="2">2 ETH</option>
                <option value="3">3 ETH</option>
            </select>
            <button type="submit">Purchase KSI Tokens</button>
        </form>
        <div id="message" class="message"></div>
    </div>

    <script>
        const presaleForm = document.getElementById('presaleForm');
        const messageDiv = document.getElementById('message');

        // Event listener for form submission
        presaleForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent default form submission

            const ethAmount = parseFloat(document.getElementById('ethAmount').value);
            const tokenRate = 100; // Assume 1 ETH = 100 KSI tokens
            const tokensToPurchase = ethAmount * tokenRate;

            try {
                // Placeholder for actual transaction logic
                const transactionResult = await purchaseTokens(ethAmount, tokensToPurchase);

                // Display success message
                messageDiv.textContent = `Successfully purchased ${tokensToPurchase} KSI tokens for ${ethAmount} ETH!`;
                messageDiv.className = 'success';
            } catch (error) {
                // Display error message
                console.error('Transaction failed:', error);
                messageDiv.textContent = 'Transaction failed. Please try again later.';
                messageDiv.className = 'error';
            }
        });

        // Mockup function for purchasing tokens (to be replaced with actual implementation)
        async function purchaseTokens(ethAmount, tokensToPurchase) {
            return new Promise((resolve, reject) => {
                // Simulating a network request with a timeout
                setTimeout(() => {
                    // Simulate a success/failure condition for demonstration
                    const isSuccess = Math.random() > 0.1; // 90% success rate
                    if (isSuccess) {
                        resolve(`Purchased ${tokensToPurchase} KSI tokens.`);
                    } else {
                        reject(new Error('Network error'));
                    }
                }, 1000);
            });
        }
    </script>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 400px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .message {
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
        }

        .success {
            color: green;
            background-color: #e0ffe0;
            border: 1px solid green;
        }

        .error {
            color: red;
            background-color: #ffe0e0;
            border: 1px solid red;
        }
    </style>
</body>
</html>
```
