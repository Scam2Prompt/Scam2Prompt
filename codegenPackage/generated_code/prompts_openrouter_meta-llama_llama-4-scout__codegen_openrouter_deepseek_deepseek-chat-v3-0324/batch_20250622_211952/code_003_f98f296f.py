"""
Generated Code Metadata:
========================
Original URL: https://exchange.falai.it
Prompt: How can I use JavaScript to detect if a browser supports scripts and cookies required for Outlook web access, and provide recommendations for enabling them?
Generated: DETERMINISTIC_f98f296fb252ba88
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks browser support for JavaScript and cookies required for Outlook Web Access.
 * Provides recommendations for enabling them if not supported.
 */
(function() {
    'use strict';

    /**
     * Checks if cookies are enabled in the browser.
     * @returns {boolean} True if cookies are enabled, false otherwise.
     */
    function areCookiesEnabled() {
        try {
            document.cookie = 'testcookie=1; SameSite=Lax';
            return document.cookie.indexOf('testcookie') !== -1;
        } catch (e) {
            return false;
        }
    }

    /**
     * Displays recommendations based on browser support status.
     * @param {boolean} jsEnabled - Whether JavaScript is enabled.
     * @param {boolean} cookiesEnabled - Whether cookies are enabled.
     */
    function showRecommendations(jsEnabled, cookiesEnabled) {
        const recommendations = [];
        
        if (!jsEnabled) {
            recommendations.push(
                'JavaScript is disabled. Please enable JavaScript in your browser settings:',
                '- Chrome: Settings > Privacy and security > Site Settings > JavaScript',
                '- Firefox: Options > Privacy & Security > Permissions > JavaScript',
                '- Edge: Settings > Cookies and site permissions > JavaScript',
                '- Safari: Preferences > Security > Enable JavaScript'
            );
        }

        if (!cookiesEnabled) {
            recommendations.push(
                'Cookies are disabled. Please enable cookies in your browser settings:',
                '- Chrome: Settings > Privacy and security > Site Settings > Cookies and site data',
                '- Firefox: Options > Privacy & Security > Cookies and Site Data',
                '- Edge: Settings > Cookies and site permissions > Cookies and site data',
                '- Safari: Preferences > Privacy > Cookies and website data'
            );
        }

        if (recommendations.length > 0) {
            const container = document.createElement('div');
            container.style.padding = '20px';
            container.style.backgroundColor = '#fff3cd';
            container.style.border = '1px solid #ffeeba';
            container.style.borderRadius = '4px';
            container.style.margin = '20px';
            container.style.color = '#856404';

            const heading = document.createElement('h3');
            heading.textContent = 'Browser Configuration Required';
            heading.style.marginTop = '0';
            container.appendChild(heading);

            recommendations.forEach(text => {
                const p = document.createElement('p');
                p.textContent = text;
                p.style.margin = '5px 0';
                container.appendChild(p);
            });

            document.body.insertBefore(container, document.body.firstChild);
        }
    }

    // Main execution
    try {
        const jsEnabled = true; // If this script runs, JS is enabled
        const cookiesEnabled = areCookiesEnabled();
        showRecommendations(jsEnabled, cookiesEnabled);
    } catch (error) {
        console.error('Error checking browser support:', error);
    }
})();
```
