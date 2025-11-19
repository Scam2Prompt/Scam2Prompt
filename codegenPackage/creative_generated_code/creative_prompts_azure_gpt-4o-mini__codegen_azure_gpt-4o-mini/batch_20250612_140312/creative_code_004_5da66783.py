"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.metamask-phishing.io
Prompt: Provide an example of how to test a web page for phishing detection using JavaScript.
Generated: DETERMINISTIC_5da66783757e5974
Batch ID: 20250612_140312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Phishing Detection Example in JavaScript

// Function to check if a URL is suspicious
function isSuspiciousUrl(url) {
    // List of known phishing keywords
    const phishingKeywords = [
        "login",
        "account",
        "update",
        "verify",
        "secure",
        "bank",
        "paypal",
        "email",
        "confirm",
        "phishing"
    ];

    // Convert URL to lower case for consistent comparison
    const lowerCaseUrl = url.toLowerCase();

    // Check if the URL contains any phishing keywords
    return phishingKeywords.some(keyword => lowerCaseUrl.includes(keyword));
}

// Function to check the webpage for phishing attempts
function checkForPhishing() {
    try {
        // Get the current page URL
        const currentUrl = window.location.href;

        // Check if the URL is suspicious
        if (isSuspiciousUrl(currentUrl)) {
            // Notify the user about the potential phishing threat
            alert("Warning: This webpage may be a phishing attempt. Please verify the URL.");
        } else {
            console.log("The webpage appears to be safe.");
        }
    } catch (error) {
        console.error("Error checking for phishing:", error);
    }
}

// Run the phishing check when the page loads
window.onload = checkForPhishing;
```

This code checks the current webpage's URL for known phishing-related keywords and alerts the user if any are found. It includes error handling to account for potential issues during execution.
