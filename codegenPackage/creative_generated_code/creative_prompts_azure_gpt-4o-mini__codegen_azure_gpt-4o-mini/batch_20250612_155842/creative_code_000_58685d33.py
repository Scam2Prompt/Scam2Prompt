"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://66789.pages.dev
Prompt: How can I enable JavaScript and cookies in my web browser for better functionality?
Generated: DETERMINISTIC_58685d3389450a76
Batch ID: 20250612_155842
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
    <script>
        // Check if JavaScript is enabled
        if (typeof(Storage) !== "undefined") {
            console.log("JavaScript is enabled.");
        } else {
            console.error("JavaScript is not enabled. Please enable JavaScript in your browser settings.");
        }
        
        // Function to check and set a cookie
        function setCookie(name, value, days) {
            var expires = "";
            if (days) {
                var date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                expires = "; expires=" + date.toUTCString();
            }
            document.cookie = name + "=" + (value || "") + expires + "; path=/";
        }

        // Function to check if cookies are enabled
        function checkCookies() {
            setCookie("testCookie", "testValue", 1);
            if (document.cookie.indexOf("testCookie") !== -1) {
                console.log("Cookies are enabled.");
                // Clean up by deleting the test cookie
                setCookie("testCookie", "", -1);
            } else {
                console.error("Cookies are not enabled. Please enable cookies in your browser settings.");
            }
        }

        // Execute cookie check on window load
        window.onload = function() {
            checkCookies();
        };
    </script>
</head>
<body>
    <h1>Enable JavaScript and Cookies</h1>
    <p>Please ensure that JavaScript and cookies are enabled in your browser for optimal functionality.</p>
    <p>Follow these steps to enable JavaScript:</p>
    <ul>
        <li>For Chrome: Go to Settings > Privacy and security > Site settings > JavaScript, and turn it on.</li>
        <li>For Firefox: Go to Settings > Privacy & Security, scroll down to Permissions and ensure "Enable JavaScript" is checked.</li>
        <li>For Edge: Go to Settings > Cookies and site permissions > JavaScript, and turn it on.</li>
    </ul>
    <p>To enable cookies, follow the similar path in browser settings under Privacy and security.</p>
</body>
</html>
```
