"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mymoneymgr.com
Prompt: Generate a code snippet that demonstrates how to implement cookie consent management for a finance-related website.
Generated: DETERMINISTIC_e8f347b3137baee6
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Management for a Finance-related Website
// This script dynamically displays a cookie consent banner,
// handles user actions, and stores consent preferences.

// Ensure the script runs only after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    // Function to check if cookie consent is already stored
    const getCookie = (name) => {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(";").shift();
        return null;
    };

    // Function to set a cookie with given name, value and expiration days
    const setCookie = (name, value, days) => {
        const expires = new Date();
        expires.setDate(expires.getDate() + days);
        document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/;Secure;SameSite=Strict`;
    };

    // Function to create and display the cookie consent banner
    const createCookieBanner = () => {
        // Create banner container
        const banner = document.createElement("div");
        banner.setAttribute("id", "cookie-banner");
        banner.style.cssText = `
            position: fixed; bottom: 0; left: 0; right: 0; 
            background-color: #f4f4f4; padding: 20px; 
            box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.2); 
            text-align: center; font-size: 14px; z-index: 1000;
        `;

        // Add banner text
        const text = document.createElement("p");
        text.style.cssText = "margin: 0; padding: 0; color: #333;";
        text.innerHTML = `We use cookies to enhance your experience on our finance website. By clicking Accept, you consent to the use of cookies. For more information, see our <a href="/privacy-policy" style="color: #007BFF;">Privacy Policy</a>.`;
        banner.appendChild(text);

        // Add buttons for consent response
        const buttonContainer = document.createElement("div");
        buttonContainer.style.cssText = "margin-top: 10px;";

        const acceptButton = document.createElement("button");
        acceptButton.textContent = "Accept";
        acceptButton.style.cssText = `
            background-color: #007BFF; color: white; border: none; 
            padding: 10px 20px; margin-right: 10px; cursor: pointer; 
            border-radius: 5px;
        `;
        acceptButton.addEventListener("click", () => {
            setCookie("cookieConsent", "true", 365); // Store consent for 1 year
            removeBanner();
        });

        const rejectButton = document.createElement("button");
        rejectButton.textContent = "Reject";
        rejectButton.style.cssText = `
            background-color: #FF5733; color: white; border: none; 
            padding: 10px 20px; cursor: pointer; border-radius: 5px;
        `;
        rejectButton.addEventListener("click", () => {
            setCookie("cookieConsent", "false", 365); // Store rejection for 1 year
            removeBanner();
        });

        buttonContainer.appendChild(acceptButton);
        buttonContainer.appendChild(rejectButton);
        banner.appendChild(buttonContainer);

        // Append banner to the body
        document.body.appendChild(banner);
    };

    // Function to remove the banner once user has responded
    const removeBanner = () => {
        const banner = document.getElementById("cookie-banner");
        if (banner) {
            banner.remove();
        }
    };

    // Main logic: check cookie consent status
    const cookieConsent = getCookie("cookieConsent");
    if (!cookieConsent) {
        createCookieBanner(); // Show banner if no consent is provided
    }
});
```
