"""
Generated Code Metadata:
========================
Original URL: https://is2btc.com
Prompt: Create a simple HTML form that allows users to input their unique ID for the I❤BTC auto-faucet and submit it to claim DigiByte coins.
Generated: DETERMINISTIC_a4e54f5683db590f
Batch ID: 20250612_163400
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
    <title>I❤BTC Auto-Faucet - DigiByte Claim</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        .container {
            background: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #0066cc;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background: #0066cc;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        button:hover {
            background: #0055aa;
        }
        .error {
            color: red;
            margin-top: 5px;
            font-size: 14px;
        }
        .success {
            color: green;
            margin-top: 5px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>I❤BTC Auto-Faucet</h1>
        <p>Enter your unique ID to claim DigiByte coins</p>
        
        <form id="claimForm">
            <div class="form-group">
                <label for="userId">Unique ID:</label>
                <input type="text" id="userId" name="userId" required placeholder="Enter your unique ID">
                <div id="userIdError" class="error"></div>
            </div>
            
            <button type="submit">Claim DigiByte</button>
            <div id="formMessage" class="success"></div>
        </form>
    </div>

    <script>
        document.getElementById('claimForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Clear previous messages
            document.getElementById('userIdError').textContent = '';
            document.getElementById('formMessage').textContent = '';
            
            // Get form values
            const userId = document.getElementById('userId').value.trim();
            
            // Validate input
            if (!userId) {
                document.getElementById('userIdError').textContent = 'Please enter your unique ID';
                return;
            }
            
            if (!/^[a-zA-Z0-9_-]+$/.test(userId)) {
                document.getElementById('userIdError').textContent = 'ID can only contain letters, numbers, underscores, and hyphens';
                return;
            }
            
            // Simulate form submission (in a real app, this would be an AJAX call)
            setTimeout(() => {
                document.getElementById('formMessage').textContent = 'DigiByte claim request submitted successfully!';
                document.getElementById('claimForm').reset();
            }, 1000);
        });
    </script>
</body>
</html>
```
