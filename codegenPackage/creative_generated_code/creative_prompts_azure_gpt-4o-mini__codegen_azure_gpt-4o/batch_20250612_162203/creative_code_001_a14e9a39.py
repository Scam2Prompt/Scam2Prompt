"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masalaunch.pages.dev
Prompt: Write a code snippet that uses cookies to track user consent preferences, inspired by the cookie management features on the Masa website.
Generated: DETERMINISTIC_a14e9a3963db075b
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Code snippet to manage user consent preferences using cookies
// Language: JavaScript

// Function to set a cookie with a specified name, value, and expiration days
function setCookie(name, value, days) {
    // Calculate the expiration date for the cookie
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = `${name}=${value}; ${expires}; path=/; SameSite=Strict`;
}

// Function to get the value of a cookie by name
function getCookie(name) {
    const nameEQ = name + "=";
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.indexOf(nameEQ) === 0) {
            return cookie.substring(nameEQ.length);
        }
    }
    return null; // Return null if the cookie is not found
}

// Function to check if the user has provided consent preferences
function hasUserConsented() {
    const consentCookie = getCookie("userConsent");
    return consentCookie !== null; // Returns true if the "userConsent" cookie exists
}

// Function to display a consent banner to the user if no consent is found
function displayConsentBanner() {
    if (!hasUserConsented()) {
        // Create a simple consent banner
        const banner = document.createElement("div");
        banner.id = "consent-banner";
        banner.style.position = "fixed";
        banner.style.bottom = "0";
        banner.style.width = "100%";
        banner.style.backgroundColor = "#f4f4f4";
        banner.style.borderTop = "1px solid #ccc";
        banner.style.padding = "10px";
        banner.style.textAlign = "center";
        banner.style.zIndex = "1000";

        const message = document.createElement("span");
        message.textContent = "We use cookies to improve your experience. By continuing, you agree to our cookie policy.";
        
        const acceptBtn = document.createElement("button");
        acceptBtn.textContent = "Accept";
        acceptBtn.style.marginLeft = "10px";
        acceptBtn.onclick = function() {
            setCookie("userConsent", "true", 365); // Set "userConsent" cookie for 1 year
            document.body.removeChild(banner); // Remove the banner after consent
        };

        const declineBtn = document.createElement("button");
        declineBtn.textContent = "Decline";
        declineBtn.style.marginLeft = "5px";
        declineBtn.onclick = function() {
            setCookie("userConsent", "false", 365); // Set "userConsent" cookie for 1 year
            document.body.removeChild(banner); // Remove the banner after declining
        };

        banner.appendChild(message);
        banner.appendChild(acceptBtn);
        banner.appendChild(declineBtn);
        document.body.appendChild(banner);
    }
}

// Initialize consent management on page load
window.onload = function() {
    displayConsentBanner(); // Display the consent banner if needed
};
```
