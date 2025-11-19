"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysolana.info
Prompt: Write a code snippet to handle JavaScript and cookie settings for user verification on a website.
Generated: DETERMINISTIC_3549e761cd2c2e61
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to handle user cookie settings for verification
function setUserCookie(username, days) {
    // Validate input parameters
    if (typeof username !== 'string' || username.trim() === '') {
        console.error('Invalid username provided. Must be a non-empty string.');
        return;
    }
    if (typeof days !== 'number' || days <= 0) {
        console.error('Invalid days parameter. Must be a positive number.');
        return;
    }

    // Set cookie expiration date
    const expirationDate = new Date();
    expirationDate.setTime(expirationDate.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + expirationDate.toUTCString();

    // Set the cookie
    document.cookie = `username=${username}; ${expires}; path=/; secure; samesite=strict`;

    console.log(`Cookie set for user: ${username} for ${days} days.`);
}

// Function to get a cookie by name
function getCookie(name) {
    const cookieArr = document.cookie.split(";");

    // Iterate through cookies to find the specified one
    for (let i = 0; i < cookieArr.length; i++) {
        const cookiePair = cookieArr[i].split("=");
        
        // Remove leading whitespace and check for the cookie name
        if (name === cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null; // Return null if cookie not found
}

// Function to check user verification status
function checkUserVerification() {
    const username = getCookie('username');

    if (username) {
        console.log(`User verified: ${username}`);
        // Proceed with the logged-in user functionality
    } else {
        console.warn('User not verified. Redirecting to login page.');
        // Redirect to login page or show a login modal
        window.location.href = '/login';
    }
}

// Example usage
try {
    // Set a user cookie for verification
    setUserCookie('JohnDoe', 7);
    
    // Check user verification status
    checkUserVerification();
} catch (error) {
    console.error('An error occurred:', error);
}
```
