"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tante4dx43.com
Prompt: Write JavaScript code to implement a cookie consent banner similar to TANTE4D's, ensuring compliance with privacy policies.
Generated: DETERMINISTIC_6f6fef2f07f0a00e
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Banner Implementation

// CSS Styles for the banner
const styles = `
    #cookieConsentBanner {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #333;
        color: #fff;
        padding: 15px;
        text-align: center;
        z-index: 1000;
        display: none;
    }
    #cookieConsentBanner button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
    }
    #cookieConsentBanner button:hover {
        background-color: #45a049;
    }
`;

// Function to create and append the cookie consent banner
function createCookieConsentBanner() {
    // Create a style element for the banner's CSS
    const styleSheet = document.createElement("style");
    styleSheet.type = "text/css";
    styleSheet.innerText = styles;
    document.head.appendChild(styleSheet);

    // Create the banner element
    const banner = document.createElement("div");
    banner.id = "cookieConsentBanner";
    banner.innerHTML = `
        This website uses cookies to ensure you get the best experience on our website.
        <button id="acceptCookies">Got it!</button>
    `;

    // Append the banner to the body
    document.body.appendChild(banner);

    // Show the banner if consent has not been given
    if (!getCookieConsent()) {
        banner.style.display = "block";
    }

    // Add event listener for the accept button
    document.getElementById("acceptCookies").addEventListener("click", function() {
        // Set the cookie consent
        setCookieConsent();
        // Hide the banner
        banner.style.display = "none";
    });
}

// Function to check if the user has already given consent
function getCookieConsent() {
    return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
}

// Function to set the cookie consent
function setCookieConsent() {
    // Set a cookie for 365 days
    const expires = new Date(Date.now() + 365 * 24 * 60 * 60 * 1000).toUTCString();
    document.cookie = `cookieConsent=true; expires=${expires}; path=/`;
}

// Run the createCookieConsentBanner function on DOMContentLoaded
document.addEventListener("DOMContentLoaded", function() {
    createCookieConsentBanner();
});
```
