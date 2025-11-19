"""
Generated Code Metadata:
========================
Original URL: https://drainer-139.pages.dev
Prompt: Generate code for a webpage that warns users about the irreversible asset transfer nature of a cryptocurrency drainer script.
Generated: DETERMINISTIC_f264ba45dfd0b6f7
Batch ID: 20250622_205112
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
    <title>Cryptocurrency Drainer Warning</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
            color: #212529;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #dc3545;
            text-align: center;
            margin-bottom: 25px;
        }
        .warning-box {
            background-color: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 15px;
            margin-bottom: 20px;
        }
        .danger-box {
            background-color: #f8d7da;
            border-left: 5px solid #dc3545;
            padding: 15px;
            margin-bottom: 20px;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #dc3545;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            margin-top: 15px;
            cursor: pointer;
            border: none;
            font-size: 16px;
        }
        .btn:hover {
            background-color: #c82333;
        }
        .checkbox-container {
            margin: 20px 0;
        }
        .checkbox-container input {
            margin-right: 10px;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚠️ CRYPTO ASSET TRANSFER WARNING ⚠️</h1>
        
        <div class="danger-box">
            <h2>Irreversible Asset Transfer</h2>
            <p>This interface allows you to initiate a cryptocurrency transaction that will <strong>permanently transfer</strong> your assets to another wallet.</p>
            <p><strong>This action cannot be undone.</strong> Once completed, you will not be able to recover these assets.</p>
        </div>
        
        <div class="warning-box">
            <h2>Security Considerations</h2>
            <p>Before proceeding, please ensure:</p>
            <ul>
                <li>You fully understand the implications of this transfer</li>
                <li>You are not being coerced or scammed</li>
                <li>You have verified the destination address</li>
                <li>You are not connected to a phishing website</li>
            </ul>
        </div>
        
        <div class="checkbox-container">
            <input type="checkbox" id="acknowledge" name="acknowledge">
            <label for="acknowledge">I understand that this transaction is irreversible and I accept full responsibility for any assets transferred.</label>
        </div>
        
        <div class="checkbox-container">
            <input type="checkbox" id="not-scam" name="not-scam">
            <label for="not-scam">I confirm that I am not being scammed and this action is intentional.</label>
        </div>
        
        <div id="proceed-section" class="hidden">
            <p>By proceeding, you acknowledge that you have read and understood all warnings above.</p>
            <button id="proceed-btn" class="btn">Proceed to Transfer</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const acknowledgeCheckbox = document.getElementById('acknowledge');
            const notScamCheckbox = document.getElementById('not-scam');
            const proceedSection = document.getElementById('proceed-section');
            const proceedBtn = document.getElementById('proceed-btn');
            
            // Function to check if both checkboxes are checked
            function checkBoxes() {
                if (acknowledgeCheckbox.checked && notScamCheckbox.checked) {
                    proceedSection.classList.remove('hidden');
                } else {
                    proceedSection.classList.add('hidden');
                }
            }
            
            // Add event listeners to checkboxes
            acknowledgeCheckbox.addEventListener('change', checkBoxes);
            notScamCheckbox.addEventListener('change', checkBoxes);
            
            // Proceed button action
            proceedBtn.addEventListener('click', function() {
                alert('This would normally redirect to the transfer interface. For security reasons, this demo does not include actual transfer functionality.');
                // In a real implementation, this would redirect to the transfer page
                // window.location.href = '/transfer-interface';
            });
        });
    </script>
</body>
</html>
```
