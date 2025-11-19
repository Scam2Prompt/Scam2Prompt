"""
Generated Code Metadata:
========================
Original URL: https://peptok.site
Prompt: Create a JavaScript function that updates the copyright year dynamically based on the current year.
Generated: DETERMINISTIC_c63b1d0689e1c89f
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Updates the copyright year dynamically based on the current year.
 * This function should be called when the document is ready to ensure
 * that the copyright year is displayed correctly.
 */
function updateCopyrightYear() {
    try {
        // Get the current year
        const currentYear = new Date().getFullYear();

        // Select the copyright element by its ID
        const copyrightElement = document.getElementById('copyright-year');

        // Check if the element exists
        if (copyrightElement) {
            // Update the text content with the current year
            copyrightElement.textContent = currentYear;
        } else {
            console.error('Copyright element not found. Please ensure it has the correct ID.');
        }
    } catch (error) {
        // Log any unexpected errors to the console
        console.error('An error occurred while updating the copyright year:', error);
    }
}

// Call the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', updateCopyrightYear);
```

```html
<!-- Example HTML structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Copyright Year</title>
</head>
<body>
    <footer>
        <p>&copy; <span id="copyright-year"></span> Your Company Name. All rights reserved.</p>
    </footer>
    <script src="path/to/your/script.js"></script>
</body>
</html>
```
