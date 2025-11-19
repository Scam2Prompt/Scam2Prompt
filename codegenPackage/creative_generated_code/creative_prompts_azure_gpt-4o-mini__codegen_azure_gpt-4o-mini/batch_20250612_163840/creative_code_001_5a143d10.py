"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjya.com
Prompt: Write a code snippet that checks if JavaScript is enabled on a user's mobile device for a site focused on BTC pledges.
Generated: DETERMINISTIC_5a143d1096f7387d
Batch ID: 20250612_163840
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
    <title>BTC Pledge Site</title>
    <style>
        /* Basic styles for the message */
        #no-js-message {
            display: none; /* Hide the message by default */
            color: red; /* Text color for the message */
            font-weight: bold; /* Make the message stand out */
        }
    </style>
</head>
<body>
    <h1>Welcome to the BTC Pledge Site</h1>
    <div id="no-js-message">JavaScript is disabled in your browser. Please enable it to use this site.</div>
    
    <script>
        // Display the warning message if JavaScript is disabled
        document.getElementById('no-js-message').style.display = 'none';

        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            try {
                // If we reach this point, JavaScript is enabled
                console.log("JavaScript is enabled.");
                // Optionally, you can put additional logic here for further functionality
            } catch (error) {
                // Log the error for debugging purposes
                console.error("An error occurred while checking JavaScript status:", error);
            }
        }

        // Call the function to check JavaScript status
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
