"""
Generated Code Metadata:
========================
Original URL: https://masked-40w.pages.dev
Prompt: "How can I mask sensitive information on a web page using JavaScript?"
Generated: DETERMINISTIC_c0d7b19978df5a72
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Masks sensitive information on a web page by replacing text content with asterisks.
 * @param {string} selector - CSS selector for the elements containing sensitive info.
 * @param {number} [visibleChars=0] - Number of characters to leave unmasked at the end.
 * @param {string} [maskChar='*'] - Character to use for masking.
 * @throws {Error} If selector is invalid or no elements are found.
 */
function maskSensitiveInfo(selector, visibleChars = 0, maskChar = '*') {
    if (!selector || typeof selector !== 'string') {
        throw new Error('Invalid selector provided');
    }

    const elements = document.querySelectorAll(selector);
    if (!elements.length) {
        throw new Error('No elements found with the provided selector');
    }

    elements.forEach(element => {
        const originalText = element.textContent.trim();
        if (!originalText) return;

        const textLength = originalText.length;
        visibleChars = Math.min(visibleChars, textLength);

        const maskedPart = maskChar.repeat(Math.max(0, textLength - visibleChars));
        const visiblePart = originalText.slice(-visibleChars);
        element.textContent = maskedPart + visiblePart;
    });
}

// Example usage:
// Mask all elements with class 'sensitive-data', showing last 4 characters
// maskSensitiveInfo('.sensitive-data', 4);
```
