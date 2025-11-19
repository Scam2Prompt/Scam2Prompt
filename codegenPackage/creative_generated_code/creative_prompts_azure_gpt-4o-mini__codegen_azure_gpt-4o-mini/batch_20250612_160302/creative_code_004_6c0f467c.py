"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bat1.cc
Prompt: How do I check if JavaScript is enabled in my browser while trying to access BAT?
Generated: DETERMINISTIC_6c0f467c735345bb
Batch ID: 20250612_160302
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Basic styles for the message */
        #js-enabled-message {
            display: none; /* Hidden by default */
            color: green;
            font-weight: bold;
        }
        #js-disabled-message {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
    <noscript>
        <style>
            /* Styles for when JavaScript is disabled */
            #js-disabled-message {
                display: block; /* Show message if JavaScript is disabled */
            }
        </style>
    </noscript>
</head>
<body>
    <h1>Checking JavaScript Status</h1>
    
    <div id="js-enabled-message">JavaScript is enabled in your browser.</div>
    <div id="js-disabled-message">JavaScript is disabled in your browser. Please enable it to access the features of this site.</div>

    <script>
        // This function checks if JavaScript is enabled and updates the UI accordingly
        function checkJavaScriptEnabled() {
            try {
                // Select messages for JavaScript enabled and disabled states
                const jsEnabledMessage = document.getElementById('js-enabled-message');
                const jsDisabledMessage = document.getElementById('js-disabled-message');
                
                // If JavaScript is running, display the enabled message
                jsEnabledMessage.style.display = 'block';
                jsDisabledMessage.style.display = 'none';
            } catch (error) {
                // Log error to the console if there's an issue
                console.error('Error while checking JavaScript status:', error);
            }
        }

        // Call the function to check if JavaScript is enabled
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
