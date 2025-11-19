"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ionetsol.net
Prompt: How do I enable human verification on my site using JavaScript and cookies effectively?
Generated: DETERMINISTIC_3f6cef119ef224f9
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Human Verification with JavaScript and Cookies
// This script enables human verification by using a simple math challenge.
// If the user passes the challenge, a cookie is set to remember their response.

(function() {
    // Function to set a cookie
    function setCookie(name, value, days) {
        const d = new Date();
        d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + d.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    // Function to get a cookie value by name
    function getCookie(name) {
        const nameEQ = name + "=";
        const ca = document.cookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    // Function to prompt the user with a simple math challenge
    function showVerificationChallenge() {
        const num1 = Math.floor(Math.random() * 10);
        const num2 = Math.floor(Math.random() * 10);
        const correctAnswer = num1 + num2;

        const userAnswer = prompt(`Please solve this: ${num1} + ${num2} = ?`);

        // Check if the answer is correct
        if (parseInt(userAnswer) === correctAnswer) {
            // Set a cookie to remember that the user passed the verification
            setCookie("humanVerification", "true", 7); // expires in 7 days
            alert("Verification successful!");
        } else {
            alert("Verification failed. Please try again.");
        }
    }

    // Check if the verification cookie is already set
    const verificationCookie = getCookie("humanVerification");
    if (!verificationCookie) {
        showVerificationChallenge();
    } else {
        alert("You are already verified as a human.");
    }
})();
```
