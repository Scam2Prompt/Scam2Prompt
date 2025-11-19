"""
Generated Code Metadata:
========================
Original URL: https://11tesorosibericos.com
Prompt: "Create a JavaScript function to implement a cookie consent banner for an e-commerce website, similar to the one on 11tesorosibericos.com."
Generated: DETERMINISTIC_3d0b3a53fccc00d1
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Consent Banner Implementation for E-commerce Websites
 * 
 * This script provides a customizable cookie consent banner that complies with GDPR and other privacy regulations.
 * It allows users to accept or reject cookies and stores their preference for future visits.
 */

class CookieConsentBanner {
    /**
     * Initialize the cookie consent banner with default options.
     * @param {Object} options - Configuration options for the banner
     * @param {string} options.message - The message to display on the banner
     * @param {string} options.acceptButtonText - Text for the accept button
     * @param {string} options.rejectButtonText - Text for the reject button
     * @param {string} options.cookieName - Name of the cookie to store consent
     * @param {number} options.cookieExpiryDays - Number of days until the cookie expires
     * @param {string} options.bannerPosition - CSS position of the banner ('top' or 'bottom')
     * @param {string} options.bannerColor - Background color of the banner
     * @param {string} options.textColor - Text color of the banner
     * @param {string} options.buttonColor - Background color of the buttons
     * @param {string} options.buttonTextColor - Text color of the buttons
     */
    constructor(options = {}) {
        this.options = {
            message: 'We use cookies to enhance your experience on our website. By continuing to browse, you agree to our use of cookies.',
            acceptButtonText: 'Accept',
            rejectButtonText: 'Reject',
            cookieName: 'cookieConsent',
            cookieExpiryDays: 365,
            bannerPosition: 'bottom',
            bannerColor: '#f8f9fa',
            textColor: '#333333',
            buttonColor: '#007bff',
            buttonTextColor: '#ffffff',
            ...options
        };

        this.banner = null;
        this.initialized = false;

        this.init();
    }

    /**
     * Initialize the cookie consent banner
     */
    init() {
        if (this.initialized) return;

        // Check if consent has already been given
        if (this.getCookie(this.options.cookieName)) {
            return;
        }

        this.createBanner();
        this.initialized = true;
    }

    /**
     * Create and display the cookie consent banner
     */
    createBanner() {
        // Create banner element
        this.banner = document.createElement('div');
        this.banner.id = 'cookie-consent-banner';
        this.banner.style.cssText = `
            position: fixed;
            ${this.options.bannerPosition}: 0;
            left: 0;
            right: 0;
            padding: 20px;
            background-color: ${this.options.bannerColor};
            color: ${this.options.textColor};
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
            z-index: 9999;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            gap: 15px;
        `;

        // Create message element
        const message = document.createElement('p');
        message.textContent = this.options.message;
        message.style.margin = '0';
        message.style.maxWidth = '800px';
        message.style.textAlign = 'center';

        // Create buttons container
        const buttonsContainer = document.createElement('div');
        buttonsContainer.style.display = 'flex';
        buttonsContainer.style.gap = '10px';

        // Create accept button
        const acceptButton = document.createElement('button');
        acceptButton.textContent = this.options.acceptButtonText;
        acceptButton.style.cssText = `
            padding: 8px 16px;
            background-color: ${this.options.buttonColor};
            color: ${this.options.buttonTextColor};
            border: none;
            border-radius: 4px;
            cursor: pointer;
        `;
        acceptButton.addEventListener('click', () => this.handleAccept());

        // Create reject button
        const rejectButton = document.createElement('button');
        rejectButton.textContent = this.options.rejectButtonText;
        rejectButton.style.cssText = `
            padding: 8px 16px;
            background-color: transparent;
            color: ${this.options.buttonColor};
            border: 1px solid ${this.options.buttonColor};
            border-radius: 4px;
            cursor: pointer;
        `;
        rejectButton.addEventListener('click', () => this.handleReject());

        // Append elements
        buttonsContainer.appendChild(acceptButton);
        buttonsContainer.appendChild(rejectButton);
        this.banner.appendChild(message);
        this.banner.appendChild(buttonsContainer);

        // Add banner to the document
        document.body.appendChild(this.banner);
    }

    /**
     * Handle accept button click
     */
    handleAccept() {
        this.setCookie(this.options.cookieName, 'accepted', this.options.cookieExpiryDays);
        this.removeBanner();
    }

    /**
     * Handle reject button click
     */
    handleReject() {
        this.setCookie(this.options.cookieName, 'rejected', this.options.cookieExpiryDays);
        this.removeBanner();
    }

    /**
     * Remove the banner from the DOM
     */
    removeBanner() {
        if (this.banner && this.banner.parentNode) {
            this.banner.parentNode.removeChild(this.banner);
        }
    }

    /**
     * Set a cookie with the given name, value, and expiration days
     * @param {string} name - Cookie name
     * @param {string} value - Cookie value
     * @param {number} days - Number of days until expiration
     */
    setCookie(name, value, days) {
        try {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            const expires = `expires=${date.toUTCString()}`;
            document.cookie = `${name}=${value};${expires};path=/;SameSite=Lax`;
        } catch (error) {
            console.error('Error setting cookie:', error);
        }
    }

    /**
     * Get the value of a cookie by name
     * @param {string} name - Cookie name
     * @returns {string|null} Cookie value or null if not found
     */
    getCookie(name) {
        try {
            const cookieName = `${name}=`;
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.indexOf(cookieName) === 0) {
                    return cookie.substring(cookieName.length, cookie.length);
                }
            }
            return null;
        } catch (error) {
            console.error('Error getting cookie:', error);
            return null;
        }
    }
}

// Example usage:
// document.addEventListener('DOMContentLoaded', () => {
//     new CookieConsentBanner({
//         message: 'We use cookies to improve your experience...',
//         acceptButtonText: 'I Accept',
//         rejectButtonText: 'I Reject',
//         bannerPosition: 'bottom',
//         bannerColor: '#ffffff',
//         textColor: '#333333',
//         buttonColor: '#4CAF50',
//         buttonTextColor: '#ffffff'
//     });
// });
```
