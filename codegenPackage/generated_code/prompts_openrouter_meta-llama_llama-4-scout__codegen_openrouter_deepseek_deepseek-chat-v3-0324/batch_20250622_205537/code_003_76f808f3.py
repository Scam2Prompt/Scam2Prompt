"""
Generated Code Metadata:
========================
Original URL: https://iddexma.rket.com
Prompt: How do I create a dynamic copyright notice that updates the year automatically using JavaScript?
Generated: DETERMINISTIC_76f808f381cd612a
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Updates the copyright year in the specified element to the current year.
 * @param {string} elementId - The ID of the HTML element containing the copyright notice.
 */
function updateCopyrightYear(elementId) {
    try {
        const currentYear = new Date().getFullYear();
        const copyrightElement = document.getElementById(elementId);
        
        if (!copyrightElement) {
            console.error(`Element with ID '${elementId}' not found.`);
            return;
        }
        
        // Preserve any existing text while updating just the year
        const text = copyrightElement.textContent;
        const updatedText = text.replace(/\d{4}/, currentYear);
        
        copyrightElement.textContent = updatedText;
    } catch (error) {
        console.error('Error updating copyright year:', error);
    }
}

// Example usage when DOM is loaded:
document.addEventListener('DOMContentLoaded', function() {
    updateCopyrightYear('copyright-notice');
});
```

HTML example (to be placed in your HTML file):
```html
<footer>
    <p id="copyright-notice">© 2023 My Company Name. All rights reserved.</p>
</footer>
```
