"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starnket.cc
Prompt: Generate a JavaScript function that checks for cookie consent before loading a webpage.
Generated: DETERMINISTIC_c58a8ba4c55001f2
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks for cookie consent before proceeding with the webpage loading.
 * If consent is not given, it displays a consent message and prevents
 * further actions until consent is granted.
 */
function checkCookieConsent() {
    // Check if the consent cookie exists
    const consentCookie = document.cookie.split('; ').find(row => row.startsWith('cookieConsent='));

    // If consent is found, allow the webpage to load normally
    if (consentCookie && consentCookie.split('=')[1] === 'true') {
        console.log("Cookie consent granted.");
        // Proceed with the rest of the webpage loading process
        loadWebpageContent();
    } else {
        // If there is no consent, show a consent message to the user
        showConsentMessage();
    }
}

/**
 * Loads the main content of the webpage.
 * This function can be expanded to include additional loading logic.
 */
function loadWebpageContent() {
    // Example logic to load the main content
    console.log("Loading webpage content...");
    // Insert content loading code here
}

/**
 * Displays a cookie consent message to the user.
 * The user can accept or decline cookie usage.
 */
function showConsentMessage() {
    const consentMessage = document.createElement('div');
    consentMessage.style.position = 'fixed';
    consentMessage.style.bottom = '20px';
    consentMessage.style.left = '20px';
    consentMessage.style.backgroundColor = '#f8d7da';
    consentMessage.style.color = '#721c24';
    consentMessage.style.padding = '10px';
    consentMessage.style.border = '1px solid #f5c6cb';
    consentMessage.innerText = 'This website uses cookies to enhance the user experience.';

    const acceptButton = document.createElement('button');
    acceptButton.innerText = 'Accept';
    acceptButton.onclick = () => {
        setCookieConsent(true);
        consentMessage.remove();
        loadWebpageContent();
    };

    const declineButton = document.createElement('button');
    declineButton.innerText = 'Decline';
    declineButton.onclick = () => {
        setCookieConsent(false);
        consentMessage.remove();
        console.log("Cookie consent declined.");
    };

    consentMessage.appendChild(acceptButton);
    consentMessage.appendChild(declineButton);
    document.body.appendChild(consentMessage);
}

/**
 * Sets the cookie consent status.
 * @param {boolean} consent - True for consent granted, false for declined.
 */
function setCookieConsent(consent) {
    const consentValue = consent ? 'true' : 'false';
    const expiryDate = new Date();
    expiryDate.setFullYear(expiryDate.getFullYear() + 1); // Cookie expires in 1 year
    document.cookie = `cookieConsent=${consentValue}; expires=${expiryDate.toUTCString()}; path=/`;
}

// Run the cookie consent check on page load
window.onload = () => {
    try {
        checkCookieConsent();
    } catch (error) {
        console.error("An error occurred while checking cookie consent:", error);
    }
};
```
