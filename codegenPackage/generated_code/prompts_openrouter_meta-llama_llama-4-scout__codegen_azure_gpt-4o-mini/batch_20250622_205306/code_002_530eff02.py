"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Generate a code snippet in JavaScript to implement a cookie consent banner on a dental clinic website, following GDPR guidelines, as seen on Studio Dentistico dott.ssa Vira Palazzo's website.
Generated: DETERMINISTIC_530eff023d52ea6f
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Cookie Consent Banner Implementation
// This script creates a cookie consent banner that complies with GDPR guidelines.

document.addEventListener("DOMContentLoaded", function () {
    // Check if the user has already given consent
    const cookieConsent = localStorage.getItem("cookieConsent");

    // If consent is not given, display the banner
    if (!cookieConsent) {
        createCookieConsentBanner();
    }

    /**
     * Creates and displays the cookie consent banner.
     */
    function createCookieConsentBanner() {
        // Create banner element
        const banner = document.createElement("div");
        banner.id = "cookie-consent-banner";
        banner.style.position = "fixed";
        banner.style.bottom = "0";
        banner.style.left = "0";
        banner.style.right = "0";
        banner.style.backgroundColor = "#f8f9fa";
        banner.style.padding = "15px";
        banner.style.textAlign = "center";
        banner.style.boxShadow = "0 -2px 5px rgba(0,0,0,0.1)";
        banner.innerHTML = `
            <p style="margin: 0;">
                We use cookies to enhance your experience on our website. 
                By clicking "Accept", you consent to our use of cookies. 
                <a href="/privacy-policy" style="color: #007bff;">Learn more</a>.
            </p>
            <button id="accept-cookies" style="margin-left: 10px; padding: 5px 10px; cursor: pointer;">
                Accept
            </button>
        `;

        // Append banner to body
        document.body.appendChild(banner);

        // Add event listener for the accept button
        document.getElementById("accept-cookies").addEventListener("click", function () {
            // Store consent in local storage
            localStorage.setItem("cookieConsent", "accepted");
            // Remove the banner from the DOM
            banner.remove();
        });
    }
});
```
