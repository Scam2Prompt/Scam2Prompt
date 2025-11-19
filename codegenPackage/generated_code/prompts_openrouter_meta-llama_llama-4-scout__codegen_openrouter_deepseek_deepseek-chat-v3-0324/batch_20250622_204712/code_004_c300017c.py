"""
Generated Code Metadata:
========================
Original URL: https://smartnetrewardls.pages.dev
Prompt: Create a simple webpage using HTML and CSS that allows users to claim rewards, including a button to claim $500 worth of tokens.
Generated: DETERMINISTIC_c300017ca089aebf
Batch ID: 20250622_204712
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
    <title>Reward Claim Portal</title>
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
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
            color: #2c3e50;
        }

        .reward-card {
            background: linear-gradient(135deg, #3498db, #2ecc71);
            color: white;
            padding: 25px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
        }

        .reward-card h2 {
            margin-bottom: 15px;
            font-size: 24px;
        }

        .reward-card p {
            margin-bottom: 20px;
            font-size: 16px;
        }

        .claim-btn {
            background-color: #f39c12;
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 18px;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: bold;
            display: inline-block;
        }

        .claim-btn:hover {
            background-color: #e67e22;
            transform: translateY(-2px);
        }

        .reward-list {
            margin-top: 30px;
        }

        .reward-item {
            background: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .reward-item .value {
            font-weight: bold;
            color: #27ae60;
        }

        footer {
            text-align: center;
            margin-top: 30px;
            color: #7f8c8d;
            font-size: 14px;
        }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            .container {
                padding: 15px;
            }
            
            .reward-card {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Reward Claim Portal</h1>
        
        <div class="reward-card">
            <h2>Special Bonus Reward</h2>
            <p>Claim your $500 worth of tokens today!</p>
            <button class="claim-btn" id="mainClaimBtn">Claim $500 Tokens</button>
        </div>

        <div class="reward-list">
            <h2>Available Rewards</h2>
            <div class="reward-item">
                <span>Welcome Bonus</span>
                <span class="value">$50 Tokens</span>
            </div>
            <div class="reward-item">
                <span>Referral Bonus</span>
                <span class="value">$100 Tokens</span>
            </div>
            <div class="reward-item">
                <span>Loyalty Reward</span>
                <span class="value">$200 Tokens</span>
            </div>
        </div>

        <footer>
            <p>© 2023 Reward Portal. All rights reserved.</p>
        </footer>
    </div>

    <script>
        document.getElementById('mainClaimBtn').addEventListener('click', function() {
            // In a real application, this would connect to a backend service
            alert('$500 worth of tokens claimed successfully!');
            
            // Disable the button after claiming
            this.disabled = true;
            this.textContent = 'Claimed!';
            this.style.backgroundColor = '#95a5a6';
        });
    </script>
</body>
</html>
```
