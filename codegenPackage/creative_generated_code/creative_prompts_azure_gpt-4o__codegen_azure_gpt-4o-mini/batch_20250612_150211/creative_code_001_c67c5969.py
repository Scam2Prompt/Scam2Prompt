"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cxconnect1-dss.coinbase.co.za
Prompt: Create a script that checks for JavaScript functionality and redirects users to an alternative page if JavaScript is disabled, inspired by the requirements of the Coinbase domain details page.
Generated: DETERMINISTIC_c67c5969cf6e91fc
Batch ID: 20250612_150211
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
    <title>JavaScript Functionality Check</title>
    <noscript>
        <meta http-equiv="refresh" content="0; url=alternative-page.html">
        <link rel="stylesheet" href="styles.css"> <!-- Optional: Add styles for non-JS page -->
    </noscript>
    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Setting a flag in local storage to indicate that JavaScript is enabled
            try {
                localStorage.setItem('jsEnabled', 'true');
            } catch (error) {
                console.error('Error accessing local storage:', error);
            }
        }

        // Execute the function on page load
        window.onload = checkJavaScript;

        // Redirect if local storage is not accessible, indicating JS is likely disabled
        window.addEventListener('storage', function(event) {
            if (event.key === 'jsEnabled' && event.newValue === null) {
                window.location.href = 'alternative-page.html'; // Redirect to alternative page
            }
        });

        // Optionally, you can add a timeout to ensure the page does not hang while waiting for JS
        setTimeout(() => {
            if (!localStorage.getItem('jsEnabled')) {
                window.location.href = 'alternative-page.html'; // Redirect to alternative page if JS is not confirmed
            }
        }, 1000); // Wait for 1 second before redirecting
    </script>
</head>
<body>
    <h1>Welcome to the JavaScript Functionality Check Page!</h1>
    <p>If you see this message, it means JavaScript is enabled on your browser.</p>
    <p>If JavaScript is disabled, you will be redirected to an alternative page.</p>
</body>
</html>
```
