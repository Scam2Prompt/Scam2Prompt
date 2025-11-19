"""
Generated Code Metadata:
========================
Original URL: https://sei.land
Prompt: How can I use JavaScript to dynamically update the copyright year on a webpage, such as from 2024 to 2025, considering the current year?
Generated: DETERMINISTIC_1a4d952175fca738
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to get the current year
function getCurrentYear() {
    return new Date().getFullYear();
}

// Function to update the copyright year on the webpage
function updateCopyrightYear(copyrightElementId) {
    try {
        // Get the current year
        const currentYear = getCurrentYear();

        // Get the copyright element
        const copyrightElement = document.getElementById(copyrightElementId);

        // Check if the element exists
        if (copyrightElement) {
            // Update the copyright text
            copyrightElement.textContent = ` ${currentYear} `;
        } else {
            console.error(`Element with id '${copyrightElementId}' not found.`);
        }
    } catch (error) {
        console.error(`Error updating copyright year: ${error.message}`);
    }
}

// Example usage
document.addEventListener('DOMContentLoaded', function() {
    updateCopyrightYear('copyright-year');
});
```

```html
<!-- Example HTML -->
<footer>
    <p id="copyright-year">&copy; 2024</p>
</footer>
```

```css
/* Example CSS */
/* Optional styling for the copyright text */
#copyright-year {
    font-size: 14px;
    color: #666;
}
```
