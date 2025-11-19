"""
Generated Code Metadata:
========================
Original URL: https://asd-col.pages.dev
Prompt: Create a simple web page using HTML, CSS, and JavaScript to display a token presale interface, including a "BUY" button and ETH deposit options.
Generated: DETERMINISTIC_916ec6c93f8fdf6a
Batch ID: 20250622_210803
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
    <title>Token Presale Interface</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
            color: #2c3e50;
        }

        .presale-info {
            margin-bottom: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input[type="number"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }

        .eth-options {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }

        .eth-option {
            padding: 8px 15px;
            background: #e9ecef;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.2s;
        }

        .eth-option:hover {
            background: #dee2e6;
        }

        .eth-option.active {
            background: #007bff;
            color: white;
        }

        button {
            display: block;
            width: 100%;
            padding: 12px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.2s;
        }

        button:hover {
            background: #0056b3;
        }

        button:disabled {
            background: #6c757d;
            cursor: not-allowed;
        }

        .status {
            margin-top: 20px;
            padding: 10px;
            border-radius: 4px;
            text-align: center;
        }

        .success {
            background: #d4edda;
            color: #155724;
        }

        .error {
            background: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Token Presale</h1>
        
        <div class="presale-info">
            <p>Token Price: 0.001 ETH per token</p>
            <p>Minimum Purchase: 0.01 ETH</p>
            <p>Maximum Purchase: 5 ETH</p>
        </div>

        <div class="form-group">
            <label for="ethAmount">ETH Amount</label>
            <input type="number" id="ethAmount" min="0.01" max="5" step="0.01" placeholder="Enter ETH amount">
            
            <div class="eth-options">
                <div class="eth-option" data-amount="0.1">0.1 ETH</div>
                <div class="eth-option" data-amount="0.5">0.5 ETH</div>
                <div class="eth-option" data-amount="1">1 ETH</div>
                <div class="eth-option" data-amount="2">2 ETH</div>
            </div>
        </div>

        <div class="form-group">
            <label for="tokenAmount">You will receive</label>
            <input type="number" id="tokenAmount" readonly placeholder="Token amount will be calculated">
        </div>

        <button id="buyButton">BUY TOKENS</button>

        <div id="statusMessage" class="status" style="display: none;"></div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const ethAmountInput = document.getElementById('ethAmount');
            const tokenAmountInput = document.getElementById('tokenAmount');
            const ethOptions = document.querySelectorAll('.eth-option');
            const buyButton = document.getElementById('buyButton');
            const statusMessage = document.getElementById('statusMessage');

            // Token price in ETH
            const TOKEN_PRICE = 0.001;

            // Update token amount when ETH amount changes
            ethAmountInput.addEventListener('input', updateTokenAmount);

            // Handle ETH option clicks
            ethOptions.forEach(option => {
                option.addEventListener('click', function() {
                    // Remove active class from all options
                    ethOptions.forEach(opt => opt.classList.remove('active'));
                    
                    // Add active class to clicked option
                    this.classList.add('active');
                    
                    // Set the ETH amount
                    const amount = parseFloat(this.dataset.amount);
                    ethAmountInput.value = amount.toFixed(2);
                    
                    // Update token amount
                    updateTokenAmount();
                });
            });

            // Handle buy button click
            buyButton.addEventListener('click', async function() {
                const ethAmount = parseFloat(ethAmountInput.value);
                
                // Validate input
                if (isNaN(ethAmount) || ethAmount < 0.01 || ethAmount > 5) {
                    showStatus('Please enter a valid ETH amount between 0.01 and 5', 'error');
                    return;
                }

                // Simulate transaction
                buyButton.disabled = true;
                buyButton.textContent = 'Processing...';
                
                try {
                    // In a real app, this would connect to a wallet and send a transaction
                    await simulateTransaction(ethAmount);
                    
                    showStatus(`Success! You have purchased ${ethAmount / TOKEN_PRICE} tokens`, 'success');
                    ethAmountInput.value = '';
                    tokenAmountInput.value = '';
                    ethOptions.forEach(opt => opt.classList.remove('active'));
                } catch (error) {
                    showStatus('Transaction failed. Please try again.', 'error');
                } finally {
                    buyButton.disabled = false;
                    buyButton.textContent = 'BUY TOKENS';
                }
            });

            // Calculate token amount based on ETH input
            function updateTokenAmount() {
                const ethAmount = parseFloat(ethAmountInput.value);
                
                if (!isNaN(ethAmount) && ethAmount >= 0.01 && ethAmount <= 5) {
                    const tokenAmount = ethAmount / TOKEN_PRICE;
                    tokenAmountInput.value = tokenAmount.toFixed(0);
                } else {
                    tokenAmountInput.value = '';
                }
            }

            // Simulate a blockchain transaction (mock)
            function simulateTransaction(ethAmount) {
                return new Promise((resolve, reject) => {
                    // Simulate network delay
                    setTimeout(() => {
                        // Randomly fail 10% of the time for demonstration
                        if (Math.random() < 0.1) {
                            reject(new Error('Transaction failed'));
                        } else {
                            resolve();
                        }
                    }, 1500);
                });
            }

            // Show status message
            function showStatus(message, type) {
                statusMessage.textContent = message;
                statusMessage.className = `status ${type}`;
                statusMessage.style.display = 'block';
                
                // Hide after 5 seconds
                setTimeout(() => {
                    statusMessage.style.display = 'none';
                }, 5000);
            }
        });
    </script>
</body>
</html>
```
