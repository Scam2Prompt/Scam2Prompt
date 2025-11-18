"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Recommend a library for managing GDPR-compliant cookie preferences on CM-Canada's website, ensuring user data privacy.
Generated: DETERMINISTIC_869a0f0157a2f4af
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the necessary library for managing cookies
import CookieConsent from 'cookieconsent';

// Function to initialize cookie consent management
function initializeCookieConsent() {
    // Configuration settings for cookie consent
    const config = {
        "cookie": {
            "name": "cookie_consent",
            "expiryDays": 365 // Cookie consent will last for one year
        },
        "position": "bottom-right", // Position of the consent banner
        "content": {
            "header": "Cookie Consent",
            "message": "We use cookies to ensure you get the best experience on our website. Learn more about our cookie policy.",
            "dismiss": "Got it!",
            "link": "Learn More",
            "href": "/privacy-policy" // Link to the privacy policy
        },
        "onInitialise": function(status) {
            // Check the status of cookie consent
            if (this.hasConsented()) {
                // User has consented to cookies
                console.log("User has accepted cookies.");
            } else {
                // User has not consented to cookies
                console.log("User has not accepted cookies.");
            }
        },
        "onStatusChange": function(status) {
            // Handle changes in consent status
            console.log("Consent status: ", status);
        },
        "onRevokeChoice": function() {
            // Handle user revoking their consent
            console.log("User has revoked cookie consent.");
        }
    };

    try {
        // Initialize Cookie Consent with the defined configuration
        CookieConsent.init(config);
    } catch (error) {
        // Error handling: log the error to the console
        console.error("Error initializing Cookie Consent:", error);
    }
}

// Call the function to set up cookie consent management on page load
document.addEventListener("DOMContentLoaded", initializeCookieConsent);
```
