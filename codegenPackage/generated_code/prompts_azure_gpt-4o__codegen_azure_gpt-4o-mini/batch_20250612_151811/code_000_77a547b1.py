"""
Generated Code Metadata:
========================
Original URL: https://wonderino.com
Prompt: Write JavaScript code to implement a keyboard navigation feature similar to Wonderino's accessibility profile, allowing users to navigate menus and buttons using Tab, Shift+Tab, and Enter keys.
Generated: DETERMINISTIC_77a547b19076c706
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Keyboard Navigation Feature for Menus and Buttons

// Function to handle keyboard navigation
function handleKeyboardNavigation(event) {
    const focusableElements = getFocusableElements();
    const currentIndex = focusableElements.indexOf(document.activeElement);

    switch (event.key) {
        case 'Tab':
            // Prevent default behavior if Shift is held down
            if (event.shiftKey) {
                // Shift + Tab: Move focus to the previous element
                if (currentIndex > 0) {
                    focusableElements[currentIndex - 1].focus();
                } else {
                    // Loop back to the last element
                    focusableElements[focusableElements.length - 1].focus();
                }
                event.preventDefault();
            } else {
                // Tab: Move focus to the next element
                if (currentIndex < focusableElements.length - 1) {
                    focusableElements[currentIndex + 1].focus();
                } else {
                    // Loop back to the first element
                    focusableElements[0].focus();
                }
                event.preventDefault();
            }
            break;

        case 'Enter':
            // Trigger click event on the focused element
            if (document.activeElement instanceof HTMLButtonElement || document.activeElement instanceof HTMLAnchorElement) {
                document.activeElement.click();
                event.preventDefault();
            }
            break;

        default:
            break;
    }
}

// Function to get all focusable elements within the document
function getFocusableElements() {
    return Array.from(document.querySelectorAll('a[href], area[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), button:not([disabled]), [tabindex]:not([tabindex="-1"])'));
}

// Initialize keyboard navigation
function initKeyboardNavigation() {
    // Add event listener for keydown events
    document.addEventListener('keydown', handleKeyboardNavigation);
}

// Call the initialization function on DOMContentLoaded
document.addEventListener('DOMContentLoaded', initKeyboardNavigation);
```
