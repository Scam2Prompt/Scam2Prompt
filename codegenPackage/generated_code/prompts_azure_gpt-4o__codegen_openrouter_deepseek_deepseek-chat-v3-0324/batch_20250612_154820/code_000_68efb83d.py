"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Write code to implement cookie consent management similar to the GDPR Cookie Consent plugin described on the Health Insurance Shop website, including categories like "Analytics," "Functional," and "Necessary."
Generated: DETERMINISTIC_68efb83d4aeed834
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieConsentManager.js
class CookieConsentManager {
    constructor() {
        this.cookieName = 'cookie_consent_preferences';
        this.cookieExpiryDays = 365;
        this.categories = {
            necessary: {
                title: 'Necessary',
                description: 'These cookies are essential for the website to function properly.',
                required: true,
                enabled: true
            },
            functional: {
                title: 'Functional',
                description: 'These cookies enable enhanced functionality and personalization.',
                required: false,
                enabled: false
            },
            analytics: {
                title: 'Analytics',
                description: 'These cookies help us understand how visitors interact with our website.',
                required: false,
                enabled: false
            }
        };
        
        this.init();
    }

    /**
     * Initialize the cookie consent manager
     */
    init() {
        this.loadPreferences();
        if (!this.getPreferences()) {
            this.showBanner();
        }
    }

    /**
     * Show the consent banner
     */
    showBanner() {
        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.style.position = 'fixed';
        banner.style.bottom = '0';
        banner.style.left = '0';
        banner.style.right = '0';
        banner.style.backgroundColor = '#f8f9fa';
        banner.style.padding = '20px';
        banner.style.boxShadow = '0 -2px 10px rgba(0,0,0,0.1)';
        banner.style.zIndex = '1000';

        const content = document.createElement('div');
        content.style.maxWidth = '1200px';
        content.style.margin = '0 auto';
        content.style.display = 'flex';
        content.style.flexDirection = 'column';
        content.style.gap = '15px';

        const title = document.createElement('h3');
        title.textContent = 'Cookie Preferences';
        title.style.margin = '0';
        title.style.fontSize = '18px';

        const description = document.createElement('p');
        description.textContent = 'We use cookies to enhance your experience. Choose which cookies you allow:';
        description.style.margin = '0';
        description.style.fontSize = '14px';

        const preferencesContainer = document.createElement('div');
        preferencesContainer.style.display = 'flex';
        preferencesContainer.style.flexDirection = 'column';
        preferencesContainer.style.gap = '10px';

        // Add cookie category toggles
        for (const [key, category] of Object.entries(this.categories)) {
            if (category.required) continue;

            const preference = document.createElement('div');
            preference.style.display = 'flex';
            preference.style.alignItems = 'center';
            preference.style.gap = '10px';

            const toggle = document.createElement('input');
            toggle.type = 'checkbox';
            toggle.id = `cookie-consent-${key}`;
            toggle.checked = category.enabled;
            toggle.disabled = category.required;
            toggle.addEventListener('change', () => {
                this.categories[key].enabled = toggle.checked;
            });

            const label = document.createElement('label');
            label.htmlFor = `cookie-consent-${key}`;
            label.style.display = 'flex';
            label.style.flexDirection = 'column';

            const labelTitle = document.createElement('span');
            labelTitle.textContent = category.title;
            labelTitle.style.fontWeight = 'bold';

            const labelDesc = document.createElement('span');
            labelDesc.textContent = category.description;
            labelDesc.style.fontSize = '12px';
            labelDesc.style.color = '#666';

            label.appendChild(labelTitle);
            label.appendChild(labelDesc);
            preference.appendChild(toggle);
            preference.appendChild(label);
            preferencesContainer.appendChild(preference);
        }

        const buttonsContainer = document.createElement('div');
        buttonsContainer.style.display = 'flex';
        buttonsContainer.style.gap = '10px';
        buttonsContainer.style.justifyContent = 'flex-end';

        const acceptAllButton = document.createElement('button');
        acceptAllButton.textContent = 'Accept All';
        acceptAllButton.style.padding = '8px 16px';
        acceptAllButton.style.backgroundColor = '#007bff';
        acceptAllButton.style.color = 'white';
        acceptAllButton.style.border = 'none';
        acceptAllButton.style.borderRadius = '4px';
        acceptAllButton.style.cursor = 'pointer';
        acceptAllButton.addEventListener('click', () => {
            this.enableAllCookies();
            this.savePreferences();
            this.hideBanner();
        });

        const saveButton = document.createElement('button');
        saveButton.textContent = 'Save Preferences';
        saveButton.style.padding = '8px 16px';
        saveButton.style.backgroundColor = '#6c757d';
        saveButton.style.color = 'white';
        saveButton.style.border = 'none';
        saveButton.style.borderRadius = '4px';
        saveButton.style.cursor = 'pointer';
        saveButton.addEventListener('click', () => {
            this.savePreferences();
            this.hideBanner();
        });

        buttonsContainer.appendChild(saveButton);
        buttonsContainer.appendChild(acceptAllButton);

        content.appendChild(title);
        content.appendChild(description);
        content.appendChild(preferencesContainer);
        content.appendChild(buttonsContainer);
        banner.appendChild(content);

        document.body.appendChild(banner);
    }

    /**
     * Hide the consent banner
     */
    hideBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.remove();
        }
    }

    /**
     * Enable all cookie categories
     */
    enableAllCookies() {
        for (const key in this.categories) {
            this.categories[key].enabled = true;
        }
    }

    /**
     * Save user preferences to a cookie
     */
    savePreferences() {
        const preferences = {};
        for (const key in this.categories) {
            preferences[key] = this.categories[key].enabled;
        }

        const expiryDate = new Date();
        expiryDate.setDate(expiryDate.getDate() + this.cookieExpiryDays);

        document.cookie = `${this.cookieName}=${JSON.stringify(preferences)}; expires=${expiryDate.toUTCString()}; path=/; SameSite=Lax`;
    }

    /**
     * Load saved preferences from cookie
     */
    loadPreferences() {
        const cookieValue = document.cookie
            .split('; ')
            .find(row => row.startsWith(`${this.cookieName}=`))
            ?.split('=')[1];

        if (cookieValue) {
            try {
                const preferences = JSON.parse(decodeURIComponent(cookieValue));
                for (const key in preferences) {
                    if (this.categories[key] && !this.categories[key].required) {
                        this.categories[key].enabled = preferences[key];
                    }
                }
            } catch (e) {
                console.error('Error parsing cookie preferences:', e);
            }
        }
    }

    /**
     * Get current preferences
     * @returns {Object} Current cookie preferences
     */
    getPreferences() {
        const preferences = {};
        for (const key in this.categories) {
            preferences[key] = this.categories[key].enabled;
        }
        return preferences;
    }

    /**
     * Check if a specific category is enabled
     * @param {string} category - The category to check
     * @returns {boolean} Whether the category is enabled
     */
    isCategoryEnabled(category) {
        return this.categories[category]?.enabled || false;
    }
}

// Initialize the cookie consent manager when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.cookieConsentManager = new CookieConsentManager();
});

// Example usage in other parts of the application:
// if (window.cookieConsentManager && window.cookieConsentManager.isCategoryEnabled('analytics')) {
//     // Load analytics scripts
// }
```
