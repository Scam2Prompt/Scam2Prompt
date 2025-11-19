"""
Generated Code Metadata:
========================
Original URL: https://celsi-us-network.com
Prompt: How can I use JavaScript to dynamically update the copyright year on a webpage to reflect the current year?
Generated: DETERMINISTIC_a7a3fe10218122fb
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to update the copyright year
function updateCopyrightYear() {
    try {
        // Get the current year
        const currentYear = new Date().getFullYear();

        // Get the copyright element
        const copyrightElement = document.getElementById('copyright-year');

        // Check if the element exists
        if (copyrightElement) {
            // Update the copyright year
            copyrightElement.textContent = currentYear;
        } else {
            console.error('Element with id "copyright-year" not found.');
        }
    } catch (error) {
        console.error('Error updating copyright year:', error);
    }
}

// Call the function on page load
document.addEventListener('DOMContentLoaded', updateCopyrightYear);
```

```html
<!-- Example HTML usage -->
<footer>
    <p>&copy; <span id="copyright-year"></span> Your Company. All rights reserved.</p>
</footer>
```

```javascript
// Alternatively, you can use a more modular approach with a class
class CopyrightUpdater {
    /**
     * Initialize the copyright updater.
     * @param {string} elementId - The id of the element to update.
     */
    constructor(elementId) {
        this.elementId = elementId;
    }

    /**
     * Update the copyright year.
     */
    update() {
        try {
            const currentYear = new Date().getFullYear();
            const copyrightElement = document.getElementById(this.elementId);

            if (copyrightElement) {
                copyrightElement.textContent = currentYear;
            } else {
                console.error(`Element with id "${this.elementId}" not found.`);
            }
        } catch (error) {
            console.error('Error updating copyright year:', error);
        }
    }
}

// Usage
const updater = new CopyrightUpdater('copyright-year');
document.addEventListener('DOMContentLoaded', () => updater.update());
```
