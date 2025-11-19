"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnetarnask-portfolio.xyz
Prompt: What steps should I take to ensure cookies are enabled in my browser for accessing a site with DDoS protection?
Generated: DETERMINISTIC_0c5e0401ab96a962
Batch ID: 20250612_162554
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
    <title>Check Cookies Enabled</title>
    <script>
        /**
         * Function to check if cookies are enabled in the browser.
         * If cookies are enabled, a confirmation message is displayed.
         * If cookies are disabled, the user is alerted to enable them.
         */
        function checkCookiesEnabled() {
            try {
                // Attempt to set and read a test cookie
                document.cookie = "test_cookie=enabled; path=/";
                const cookiesEnabled = document.cookie.includes("test_cookie=enabled");

                // Display appropriate message based on cookie status
                if (cookiesEnabled) {
                    document.getElementById("status").innerText = "Cookies are enabled in your browser.";
                } else {
                    document.getElementById("status").innerText = "Cookies are disabled. Please enable cookies to access the site properly.";
                }

                // Clean up the test cookie after the check
                document.cookie = "test_cookie=enabled; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
            } catch (error) {
                // Handle potential errors gracefully
                console.error("An error occurred while checking cookies:", error);
                document.getElementById("status").innerText = "An error occurred while checking cookies. Please verify your browser settings.";
            }
        }

        // Run the check when the page loads
        window.onload = checkCookiesEnabled;
    </script>
</head>
<body>
    <h1>Cookie Check</h1>
    <p id="status">Checking if cookies are enabled...</p>

    <!-- Instructions for users to enable cookies -->
    <p>
        If cookies are disabled, you can enable them by following the steps below:
    </p>
    <ul>
        <li>Go to your browser's settings or preferences.</li>
        <li>Search for "Cookies" or "Privacy" settings.</li>
        <li>Enable cookies for all or specific websites.</li>
        <li>Refresh the page after enabling cookies.</li>
    </ul>
</body>
</html>
```
