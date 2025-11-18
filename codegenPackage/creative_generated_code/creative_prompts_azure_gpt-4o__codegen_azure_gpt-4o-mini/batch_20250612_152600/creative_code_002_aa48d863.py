"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradezc.com
Prompt: Create a JavaScript-based interface for a Bitcoin pledge platform, ensuring compatibility with mobile devices.
Generated: DETERMINISTIC_aa48d863ebeda7b6
Batch ID: 20250612_152600
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.6.0.min.js": {
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
    <title>Bitcoin Pledge Platform</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <div class="container">
        <h1>Bitcoin Pledge Platform</h1>
        <form id="pledgeForm">
            <label for="amount">Pledge Amount (BTC):</label>
            <input type="number" id="amount" name="amount" min="0.0001" step="0.0001" required>
            <button type="submit">Pledge</button>
        </form>
        <div id="message"></div>
    </div>

    <script>
        $(document).ready(function() {
            // Handle form submission
            $('#pledgeForm').on('submit', function(event) {
                event.preventDefault(); // Prevent default form submission
                
                // Get the pledge amount from input
                const amount = parseFloat($('#amount').val());
                
                // Validate the amount
                if (isNaN(amount) || amount <= 0) {
                    showMessage('Please enter a valid amount.', 'error');
                    return;
                }

                // Simulate pledge submission
                submitPledge(amount);
            });

            // Function to display messages
            function showMessage(message, type) {
                const messageDiv = $('#message');
                messageDiv.text(message);
                messageDiv.attr('class', type); // Assign class for styling
                setTimeout(() => messageDiv.text(''), 3000); // Clear message after 3 seconds
            }

            // Function to simulate pledge submission
            function submitPledge(amount) {
                // Simulating an async operation (e.g., API call)
                try {
                    // Here you would normally send the amount to your backend API
                    console.log(`Pledging ${amount} BTC...`);

                    // Simulate success response
                    showMessage(`Successfully pledged ${amount} BTC!`, 'success');
                } catch (error) {
                    console.error('Error during pledge submission:', error);
                    showMessage('An error occurred while pledging. Please try again.', 'error');
                }
            }
        });
    </script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        label {
            margin-top: 10px;
            display: block;
        }
        input[type="number"] {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 15px;
        }
        button:hover {
            background-color: #218838;
        }
        #message {
            margin-top: 15px;
            font-weight: bold;
            text-align: center;
        }
        .success {
            color: #28a745;
        }
        .error {
            color: #dc3545;
        }
    </style>
</body>
</html>
```
