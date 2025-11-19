"""
Generated Code Metadata:
========================
Original URL: https://wholygood.com
Prompt: Write a JavaScript function to handle user data aggregation for cookie consent, inspired by the practices on wholygood.com.
Generated: DETERMINISTIC_57b84c0761f5cba9
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Handles user data aggregation for cookie consent.
 * Inspired by the practices on wholygood.com.
 * 
 * @param {Object} options - Configuration options for cookie consent.
 * @param {string} options.cookieName - Name of the cookie to store consent.
 * @param {number} options.expiryDays - Number of days until the cookie expires.
 * @param {Object} options.categories - Consent categories and their default values.
 * @param {Function} [options.onConsentChange] - Callback when consent changes.
 * @returns {Object} - Methods to interact with cookie consent.
 */
function CookieConsentManager(options) {
    // Validate required options
    if (!options || typeof options !== 'object') {
        throw new Error('Options object is required');
    }
    if (!options.cookieName || typeof options.cookieName !== 'string') {
        throw new Error('cookieName must be a string');
    }
    if (typeof options.expiryDays !== 'number' || options.expiryDays <= 0) {
        throw new Error('expiryDays must be a positive number');
    }
    if (!options.categories || typeof options.categories !== 'object') {
        throw new Error('categories must be an object');
    }

    const defaultCategories = {
        necessary: true,
        preferences: false,
        analytics: false,
        marketing: false
    };

    const config = {
        cookieName: options.cookieName,
        expiryDays: options.expiryDays,
        categories: { ...defaultCategories, ...options.categories },
        onConsentChange: options.onConsentChange || (() => {})
    };

    /**
     * Gets the current consent state from cookie.
     * @returns {Object} - Current consent state.
     */
    function getConsent() {
        try {
            const cookieValue = document.cookie
                .split('; ')
                .find(row => row.startsWith(`${config.cookieName}=`))
                ?.split('=')[1];

            if (cookieValue) {
                return JSON.parse(decodeURIComponent(cookieValue));
            }
            return null;
        } catch (error) {
            console.error('Error reading consent cookie:', error);
            return null;
        }
    }

    /**
     * Sets the consent cookie with provided values.
     * @param {Object} consent - Consent values to store.
     */
    function setConsent(consent) {
        try {
            const expiryDate = new Date();
            expiryDate.setDate(expiryDate.getDate() + config.expiryDays);

            const cookieValue = encodeURIComponent(JSON.stringify(consent));
            document.cookie = `${config.cookieName}=${cookieValue}; expires=${expiryDate.toUTCString()}; path=/; SameSite=Lax`;

            config.onConsentChange(consent);
        } catch (error) {
            console.error('Error setting consent cookie:', error);
        }
    }

    /**
     * Initializes default consent if not already set.
     */
    function initialize() {
        if (!getConsent()) {
            setConsent(config.categories);
        }
    }

    /**
     * Updates consent for specific categories.
     * @param {Object} updates - Key-value pairs of categories to update.
     */
    function updateConsent(updates) {
        if (!updates || typeof updates !== 'object') {
            throw new Error('Updates must be an object');
        }

        const currentConsent = getConsent() || config.categories;
        const newConsent = { ...currentConsent, ...updates };
        setConsent(newConsent);
    }

    /**
     * Checks if consent is given for a specific category.
     * @param {string} category - Category to check.
     * @returns {boolean} - Whether consent is given.
     */
    function hasConsent(category) {
        const consent = getConsent() || config.categories;
        return !!consent[category];
    }

    /**
     * Resets consent to default values.
     */
    function resetConsent() {
        setConsent(config.categories);
    }

    // Initialize on creation
    initialize();

    return {
        getConsent,
        setConsent,
        updateConsent,
        hasConsent,
        resetConsent,
        initialize
    };
}

// Example usage:
/*
const consentManager = new CookieConsentManager({
    cookieName: 'user_consent',
    expiryDays: 365,
    categories: {
        analytics: true
    },
    onConsentChange: (consent) => {
        console.log('Consent changed:', consent);
    }
});

console.log('Current consent:', consentManager.getConsent());
console.log('Has analytics consent:', consentManager.hasConsent('analytics'));
consentManager.updateConsent({ marketing: true });
*/
```
