"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-rho.vercel.app
Prompt: Write code to display a message to users if their browser is not Chrome, instructing them to switch to Chrome to connect their wallet.
Generated: DETERMINISTIC_9d53095d8e5f5458
Batch ID: 20250612_151003
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
    <title>Wallet Connection</title>
    <style>
        /* Basic styling for the message */
        #browser-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Border color */
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div id="browser-warning">
        To connect your wallet, please switch to Google Chrome.
    </div>

    <script>
        /**
         * Function to detect the user's browser.
         * @returns {string} - The name of the browser being used.
         */
        function getBrowser() {
            const userAgent = navigator.userAgent;

            if (userAgent.indexOf("Chrome") > -1 && userAgent.indexOf("Edg") === -1) {
                return "Chrome";
            } else if (userAgent.indexOf("Firefox") > -1) {
                return "Firefox";
            } else if (userAgent.indexOf("Safari") > -1) {
                return "Safari";
            } else if (userAgent.indexOf("Edg") > -1) {
                return "Edge";
            } else {
                return "Other";
            }
        }

        // Check the user's browser
        try {
            const browser = getBrowser();
            // Show warning message if the browser is not Chrome
            if (browser !== "Chrome") {
                document.getElementById("browser-warning").style.display = "block";
            }
        } catch (error) {
            console.error("Error checking browser: ", error);
            // Optionally log the error or inform the user
        }
    </script>
</body>
</html>
```
