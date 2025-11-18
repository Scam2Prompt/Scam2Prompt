"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imqbo.com
Prompt: Write a script that checks if a user's browser supports JavaScript and Web3 functionality, and prompts them to enable JavaScript for interacting with an ETH pledge system.
Generated: DETERMINISTIC_ac7e7417fdec1465
Batch ID: 20250612_145619
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
    <title>ETH Pledge System</title>
    <style>
        /* Basic styling for the message prompt */
        #js-warning {
            display: none;
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding */
            margin: 20px 0; /* Margin */
            border-radius: 5px; /* Rounded corners */
            text-align: center; /* Centered text */
        }
    </style>
</head>
<body>
    <div id="js-warning">
        JavaScript is disabled in your browser. Please enable JavaScript to interact with the ETH pledge system.
    </div>

    <script>
        // Check if JavaScript is enabled
        document.getElementById('js-warning').style.display = 'none'; // Hide warning by default

        // Function to check for Web3 support
        function checkWeb3Support() {
            // Check for Ethereum provider (Web3)
            if (typeof window.ethereum !== 'undefined' || (typeof window.web3 !== 'undefined')) {
                return true; // Web3 is supported
            } else {
                alert('Web3 is not supported. Please install a compatible wallet like MetaMask.');
                return false; // Web3 is not supported
            }
        }

        // Function to initialize the script
        function init() {
            // Check if JavaScript is enabled
            if (typeof window === 'undefined' || !window.document) {
                document.getElementById('js-warning').style.display = 'block'; // Show warning
            } else {
                // If JavaScript is enabled, check for Web3 support
                if (!checkWeb3Support()) {
                    document.getElementById('js-warning').style.display = 'block'; // Show warning if Web3 is not supported
                }
            }
        }

        // Run the initialization function
        try {
            init();
        } catch (error) {
            console.error('An error occurred during initialization:', error); // Log any errors during initialization
        }
    </script>
</body>
</html>
```
