"""
Generated Code Metadata:
========================
Original URL: https://duoiudf-dsdds-1bs.pages.dev
Prompt: "Write a code example for implementing a simple website blocker using JavaScript."
Generated: DETERMINISTIC_04e9c7e038b1a9ca
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Website Blocker using JavaScript
 * 
 * This script blocks access to specified websites by redirecting the user
 * to a blocked page when they attempt to visit any of the blocked sites.
 */

// List of blocked websites (can be extended as needed)
const blockedSites = [
    "facebook.com",
    "twitter.com",
    "instagram.com",
    "youtube.com",
    "reddit.com"
];

// Check if current URL matches any blocked site
function isBlocked(url) {
    return blockedSites.some(site => {
        return url.includes(site);
    });
}

// Redirect to blocked page
function redirectToBlockedPage() {
    const blockedPageUrl = chrome.runtime.getURL('blocked.html');
    window.location.href = blockedPageUrl;
}

// Main function to check and block sites
function checkAndBlock() {
    const currentUrl = window.location.href.toLowerCase();
    
    if (isBlocked(currentUrl)) {
        redirectToBlockedPage();
    }
}

// Run the check when the page loads
window.addEventListener('load', checkAndBlock);

// Also check when the URL changes (for SPA sites)
window.addEventListener('hashchange', checkAndBlock);
window.addEventListener('popstate', checkAndBlock);

// Content Security Policy for Chrome extension
if (typeof chrome !== 'undefined' && chrome.runtime && chrome.runtime.id) {
    chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
        if (request.action === "checkBlocked") {
            sendResponse({ isBlocked: isBlocked(window.location.href) });
        }
    });
}

// Error handling for blocked page redirection
try {
    checkAndBlock();
} catch (error) {
    console.error('Website blocker error:', error);
}
```
