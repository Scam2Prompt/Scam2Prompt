"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpadxz.com
Prompt: Create a JavaScript code that displays a warning message for users with outdated browsers when they attempt to log in.
Generated: DETERMINISTIC_16cfcca05d06fef6
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if the user's browser is outdated and display a warning message during login

// Define a function to check for outdated browsers
function isOutdatedBrowser() {
  // Get the user agent string
  const userAgent = navigator.userAgent;

  // Define a list of outdated browser user agents (simple example)
  // In real-world scenarios, consider using libraries like `browser-detect` or more detailed checks
  const outdatedBrowsers = [
    /MSIE \d/, // Internet Explorer
    /Trident\/\d/, // Internet Explorer (modern engines)
    /Firefox\/[1-9]\d?\.\d*/, // Firefox version less than 60
    /Chrome\/[1-5]\d?\.\d*/, // Chrome version less than 60
    /Safari\/[1-6]\d?\.\d*/, // Safari version less than 12
    /Opera\/[1-9]\d?\.\d*/, // Opera version less than 50
  ];

  // Check if the user agent matches any outdated browser regex
  for (const browserRegex of outdatedBrowsers) {
    if (browserRegex.test(userAgent)) {
      return true;
    }
  }

  return false;
}

// Function to display a warning message
function showWarningMessage() {
  alert("Warning: Your browser is outdated. Please update to a modern browser for a better login experience.");
}

// Attach an event listener to the login button
document.addEventListener("DOMContentLoaded", () => {
  const loginButton = document.getElementById("loginButton");

  if (!loginButton) {
    console.error("Login button not found in the DOM.");
    return;
  }

  loginButton.addEventListener("click", (event) => {
    // Check for outdated browsers
    if (isOutdatedBrowser()) {
      // Display warning message
      showWarningMessage();

      // Prevent login action (optional, depending on use case)
      event.preventDefault();
    }
  });
});
```

### HTML Example (to complement the JS):
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Page</title>
</head>
<body>
  <form id="loginForm">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    <br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <br>
    <button id="loginButton" type="submit">Login</button>
  </form>
  <script src="script.js"></script> <!-- Link to your JS file -->
</body>
</html>
```
