"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghozali-49z.pages.dev
Prompt: Write a script to manage cookie preferences for a web application linked to a memecoin project.
Generated: DETERMINISTIC_b262f5a4a622ae76
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// cookieManager.js

// CookieManager: A class to manage user cookie preferences for a web application
class CookieManager {
    constructor() {
        this.cookies = this.getCookiePreferences();
    }

    // Fetch the existing cookie preferences from local storage
    getCookiePreferences() {
        try {
            const preferences = localStorage.getItem('cookiePreferences');
            return preferences ? JSON.parse(preferences) : {};
        } catch (error) {
            console.error('Error retrieving cookie preferences:', error);
            return {};
        }
    }

    // Save cookie preferences to local storage
    saveCookiePreferences() {
        try {
            localStorage.setItem('cookiePreferences', JSON.stringify(this.cookies));
        } catch (error) {
            console.error('Error saving cookie preferences:', error);
        }
    }

    // Update a specific cookie preference
    updateCookiePreference(cookieName, value) {
        if (typeof cookieName !== 'string') {
            console.error('Invalid cookie name. It must be a string.');
            return;
        }
        
        this.cookies[cookieName] = value;
        this.saveCookiePreferences();
    }

    // Get the value of a specific cookie preference
    getCookiePreference(cookieName) {
        if (typeof cookieName !== 'string') {
            console.error('Invalid cookie name. It must be a string.');
            return null;
        }

        return this.cookies[cookieName] || null;
    }

    // Display cookie preferences in a user-friendly manner (e.g., in a modal or notification)
    displayCookiePreferences() {
        const preferences = this.cookies;
        const preferencesList = Object.entries(preferences)
            .map(([key, value]) => `${key}: ${value}`)
            .join('\n');

        alert(`Current Cookie Preferences:\n${preferencesList}`);
    }
}

// Example usage:
document.addEventListener('DOMContentLoaded', () => {
    const cookieManager = new CookieManager();

    // Assume we have buttons to accept, reject, or manage cookies
    document.getElementById('acceptCookies').addEventListener('click', () => {
        cookieManager.updateCookiePreference('analytics', true);
        cookieManager.updateCookiePreference('marketing', true);
        alert('Cookies accepted.');
    });

    document.getElementById('rejectCookies').addEventListener('click', () => {
        cookieManager.updateCookiePreference('analytics', false);
        cookieManager.updateCookiePreference('marketing', false);
        alert('Cookies rejected.');
    });

    document.getElementById('showPreferences').addEventListener('click', () => {
        cookieManager.displayCookiePreferences();
    });
});
```

**HTML Example:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Preferences Manager</title>
    <script src="cookieManager.js" defer></script>
</head>
<body>
    <h1>Manage Your Cookie Preferences</h1>
    <button id="acceptCookies">Accept Cookies</button>
    <button id="rejectCookies">Reject Cookies</button>
    <button id="showPreferences">Show Preferences</button>
</body>
</html>
```
