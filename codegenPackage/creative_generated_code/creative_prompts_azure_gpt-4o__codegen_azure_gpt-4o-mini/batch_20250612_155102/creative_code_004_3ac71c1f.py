"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kriptmart.com
Prompt: Suggest a secure method to implement "Not your device? Use a private window" functionality in a web application login page.
Generated: DETERMINISTIC_3ac71c1f0333ac54
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if the user is on a private window (incognito mode)
async function isIncognitoMode() {
    // Use the FileSystem API to determine if the browser is in incognito mode
    try {
        await window.requestFileSystem(window.TEMPORARY, 100, 
            function () {
                // If the request succeeds, the browser is not in incognito mode
                return false;
            }, 
            function () {
                // If the request fails, the browser is in incognito mode
                return true;
            });
    } catch (e) {
        // If the browser doesn't support the FileSystem API, assume it's not in incognito mode
        console.error('Error checking incognito mode:', e);
        return false;
    }
}

// Function to display a security warning if the user is not on a private window
async function checkPrivateWindow() {
    const isPrivate = await isIncognitoMode();

    if (!isPrivate) {
        document.getElementById('warning-message').innerText = 
            'For security reasons, please use a private window for logging in.';
        document.getElementById('warning-message').style.display = 'block';
    } else {
        document.getElementById('warning-message').style.display = 'none';
    }
}

// Add an event listener to check for private window when the page loads
window.addEventListener('load', checkPrivateWindow);
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <style>
        #warning-message {
            color: red;
            display: none; /* Hidden by default */
        }
    </style>
</head>
<body>
    <h1>Login to Your Account</h1>
    <div id="warning-message"></div>
    <form id="login-form" action="/login" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>

    <script src="path/to/your/script.js"></script>
</body>
</html>
```

This code consists of JavaScript for detecting incognito mode and an HTML structure for the login page, including a warning message. The warning message prompts users to use a private window for enhanced security when logging in.
