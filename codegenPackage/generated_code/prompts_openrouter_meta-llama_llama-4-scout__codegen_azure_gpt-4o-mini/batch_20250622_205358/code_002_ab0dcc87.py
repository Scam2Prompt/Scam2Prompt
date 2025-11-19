"""
Generated Code Metadata:
========================
Original URL: https://exchangesrv01.hyxoheberg.cloud
Prompt: Generate code to check if cookies are enabled and if scripts are allowed to run in a browser, specifically for Outlook Web Access.
Generated: DETERMINISTIC_ab0dcc87181cfb4a
Batch ID: 20250622_205358
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
    <title>Check Cookies and Scripts</title>
    <script>
        // Function to check if cookies are enabled in the browser
        function areCookiesEnabled() {
            // Try to set a test cookie
            document.cookie = "testcookie=1; SameSite=Lax";
            const cookiesEnabled = document.cookie.indexOf("testcookie") !== -1;

            // Clean up the test cookie
            document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax";
            return cookiesEnabled;
        }

        // Function to check if scripts are allowed to run
        function areScriptsEnabled() {
            // If this function is executed, scripts are enabled
            return true;
        }

        // Function to display the results of the checks
        function displayResults() {
            const cookiesEnabled = areCookiesEnabled();
            const scriptsEnabled = areScriptsEnabled();

            // Create a message to display the results
            let message = "Browser Feature Check:\n";
            message += `Cookies Enabled: ${cookiesEnabled ? "Yes" : "No"}\n`;
            message += `Scripts Enabled: ${scriptsEnabled ? "Yes" : "No"}`;

            // Display the results in an alert
            alert(message);
        }

        // Execute the checks when the window loads
        window.onload = function() {
            try {
                displayResults();
            } catch (error) {
                console.error("An error occurred while checking browser features:", error);
                alert("An error occurred while checking browser features. Please try again.");
            }
        };
    </script>
</head>
<body>
    <h1>Outlook Web Access Feature Check</h1>
    <p>This page checks if cookies are enabled and if scripts can run in your browser.</p>
</body>
</html>
```
