"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoz999.pages.dev
Prompt: Provide a code snippet that prompts users to enable JavaScript and cookies if they are disabled.
Generated: DETERMINISTIC_95f1c559d8b4e3c7
Batch ID: 20250612_155905
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
    <title>Enable JavaScript and Cookies</title>
    <style>
        /* Basic styling for the message */
        #message {
            display: none; /* Initially hidden */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Border color */
            padding: 20px; /* Padding for better appearance */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
    <noscript>
        <style>
            /* Styles for when JavaScript is disabled */
            #message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>
</head>
<body>
    <div id="message">
        <p>JavaScript and cookies are required for this site to function properly. Please enable them in your browser settings.</p>
    </div>

    <script>
        // Function to check if cookies are enabled
        function areCookiesEnabled() {
            // Try to set a test cookie
            document.cookie = "testcookie=1; max-age=1"; // Set a test cookie for 1 second
            const cookiesEnabled = document.cookie.indexOf("testcookie") !== -1; // Check if the cookie was set
            
            // Clean up by deleting the test cookie
            document.cookie = "testcookie=; max-age=0";
            return cookiesEnabled; // Return the result
        }

        // Check for cookies when the DOM is fully loaded
        document.addEventListener("DOMContentLoaded", function () {
            if (!areCookiesEnabled()) {
                // Alert user if cookies are disabled
                alert("Cookies are disabled. Please enable cookies for a better experience.");
            }
        });
    </script>
</body>
</html>
```
