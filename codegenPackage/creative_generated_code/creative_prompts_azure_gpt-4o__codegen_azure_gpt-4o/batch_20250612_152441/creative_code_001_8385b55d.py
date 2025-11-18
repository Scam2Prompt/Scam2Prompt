"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.dexodoor.com
Prompt: Create a script that checks for Internet Explorer 11 usage and displays a message recommending users to switch browsers, as mentioned on the Dexodoor Webmail login page.
Generated: DETERMINISTIC_8385b55d999fa969
Batch ID: 20250612_152441
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
    <title>Browser Check</title>
    <style>
        /* Basic styling for the warning message */
        #browser-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 1rem;
            margin: 1rem 0;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <div id="browser-warning">
        <strong>Warning:</strong> You appear to be using Internet Explorer 11. 
        For the best experience, please switch to a modern browser such as Google Chrome, Mozilla Firefox, or Microsoft Edge.
    </div>

    <script>
        /**
         * Function to check if the browser is Internet Explorer 11.
         * IE11 can be identified by checking the user-agent string and certain window properties.
         */
        function isInternetExplorer11() {
            try {
                // Check for the specific user-agent string and window properties unique to IE11
                return (
                    !!window.MSInputMethodContext && !!document.documentMode
                );
            } catch (error) {
                console.error("Error while detecting browser:", error);
                return false; // Default to false in case of an error
            }
        }

        /**
         * If the browser is IE11, display a warning message recommending switching browsers.
         */
        function displayBrowserWarning() {
            const browserWarningDiv = document.getElementById("browser-warning");
            if (isInternetExplorer11()) {
                browserWarningDiv.style.display = "block"; // Show the warning message
            }
        }

        // Run the browser check on page load
        displayBrowserWarning();
    </script>
</body>
</html>
```
