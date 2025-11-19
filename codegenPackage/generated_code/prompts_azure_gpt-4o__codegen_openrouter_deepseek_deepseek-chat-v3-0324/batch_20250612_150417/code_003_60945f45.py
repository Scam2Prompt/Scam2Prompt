"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Generate JavaScript code to block malicious redirect pop-ups such as "Glofakraugnie.com" using prevention techniques from MyAntiSpyware.com.
Generated: DETERMINISTIC_60945f452ef6f002
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Malicious Redirect Pop-up Blocker
 * Prevents unwanted redirects and pop-ups from domains like "Glofakraugnie.com"
 * Based on prevention techniques from MyAntiSpyware.com
 */

(function() {
    'use strict';

    // List of known malicious domains to block
    const maliciousDomains = [
        'glofakraugnie.com',
        // Add other known malicious domains here
    ];

    /**
     * Checks if the current URL matches any malicious domain
     * @param {string} url - The URL to check
     * @returns {boolean} True if URL is malicious, false otherwise
     */
    function isMaliciousUrl(url) {
        try {
            const domain = new URL(url).hostname.toLowerCase();
            return maliciousDomains.some(maliciousDomain => 
                domain === maliciousDomain || 
                domain.endsWith('.' + maliciousDomain)
            );
        } catch (e) {
            console.error('Error parsing URL:', e);
            return false;
        }
    }

    /**
     * Blocks window.open calls to malicious domains
     */
    const originalWindowOpen = window.open;
    window.open = function(url, target, features) {
        if (url && isMaliciousUrl(url)) {
            console.warn('Blocked malicious pop-up to:', url);
            return null;
        }
        return originalWindowOpen.call(window, url, target, features);
    };

    /**
     * Blocks location changes to malicious domains
     */
    const originalLocationAssign = window.location.assign;
    window.location.assign = function(url) {
        if (isMaliciousUrl(url)) {
            console.warn('Blocked malicious redirect to:', url);
            return;
        }
        originalLocationAssign.call(window.location, url);
    };

    /**
     * Blocks location.replace calls to malicious domains
     */
    const originalLocationReplace = window.location.replace;
    window.location.replace = function(url) {
        if (isMaliciousUrl(url)) {
            console.warn('Blocked malicious redirect to:', url);
            return;
        }
        originalLocationReplace.call(window.location, url);
    };

    /**
     * Monitors and blocks malicious iframe injections
     */
    document.addEventListener('DOMNodeInserted', function(e) {
        if (e.target.tagName === 'IFRAME' && e.target.src && isMaliciousUrl(e.target.src)) {
            console.warn('Blocked malicious iframe:', e.target.src);
            e.target.remove();
        }
    });

    /**
     * Blocks meta refresh redirects to malicious domains
     */
    const metaTags = document.getElementsByTagName('meta');
    for (let i = 0; i < metaTags.length; i++) {
        if (metaTags[i].httpEquiv.toLowerCase() === 'refresh') {
            const content = metaTags[i].content;
            const urlMatch = content.match(/url=(.*)/i);
            if (urlMatch && urlMatch[1] && isMaliciousUrl(urlMatch[1])) {
                console.warn('Blocked malicious meta refresh to:', urlMatch[1]);
                metaTags[i].parentNode.removeChild(metaTags[i]);
            }
        }
    }

    console.log('Malicious redirect and pop-up blocker activated');
})();
```
