"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pineappledex.org
Prompt: Write a code snippet that enables JavaScript and cookies for a web application, referencing the security measures mentioned on PineappleDex.
Generated: DETERMINISTIC_d8e03925c10180b6
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure the document is fully loaded before executing the code
document.addEventListener('DOMContentLoaded', (event) => {
    // Function to enable cookies in the web application
    function enableCookies() {
        // Check if cookies are enabled in the browser
        if (navigator.cookieEnabled) {
            console.log("Cookies are enabled.");
            // Function to set a cookie
            function setCookie(name, value, days) {
                const expires = new Date(Date.now() + days * 864e5).toUTCString();
                document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/; Secure; SameSite=Strict`;
            }

            // Function to get a cookie value by name
            function getCookie(name) {
                return document.cookie.split('; ')
                    .reduce((acc, cookie) => {
                        const [key, val] = cookie.split('=');
                        return key === name ? decodeURIComponent(val) : acc;
                    }, null);
            }

            // Function to delete a cookie
            function deleteCookie(name) {
                setCookie(name, '', -1);
            }

            // Example: Set a test cookie
            setCookie('testCookie', 'testValue', 7);
            console.log("Test cookie set.");

            // Example: Retrieve and log the cookie
            const testCookieValue = getCookie('testCookie');
            console.log(`Retrieved testCookie: ${testCookieValue}`);

            // Example: Delete the test cookie
            deleteCookie('testCookie');
            console.log("Test cookie deleted.");
        } else {
            console.error("Cookies are not enabled in this browser. Please enable cookies for full functionality.");
        }
    }

    // Execute the function to enable cookies
    enableCookies();

    // Security measures as per PineappleDex recommendations
    // Ensure that cookies are set with Secure and SameSite attributes to enhance security
    // This prevents cross-site request forgery (CSRF) attacks and ensures cookies are sent only over HTTPS
});
```

This code snippet checks if cookies are enabled, provides functions to set, get, and delete cookies, and adheres to security best practices by setting the `Secure` and `SameSite` attributes on cookies.
