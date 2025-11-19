"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Create a JavaScript function that dynamically adjusts the font size and line height on a tourism webpage to improve accessibility for users with visual impairments, inspired by the accessibility tools mentioned on Marchigüe's site.
Generated: DETERMINISTIC_fdba2d6e9fdc79e2
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically adjusts the font size and line height on a webpage
 * to improve accessibility for users with visual impairments.
 * 
 * Usage:
 * Call `adjustAccessibilitySettings(fontSizeFactor, lineHeightFactor)` with
 * appropriate factors to modify font size and line height proportionally.
 */

/**
 * Adjusts font size and line height for all elements on the page.
 *
 * @param {number} fontSizeFactor - The factor by which to multiply the default font size. (e.g., 1.2 for 20% increase)
 * @param {number} lineHeightFactor - The factor by which to multiply the default line height. (e.g., 1.5 for 50% increase)
 */
function adjustAccessibilitySettings(fontSizeFactor, lineHeightFactor) {
    try {
        // Validate input parameters
        if (typeof fontSizeFactor !== 'number' || typeof lineHeightFactor !== 'number' || 
            fontSizeFactor <= 0 || lineHeightFactor <= 0) {
            throw new Error('Invalid input: fontSizeFactor and lineHeightFactor must be positive numbers.');
        }

        // Select all elements on the page
        const allElements = document.querySelectorAll('*');

        // Iterate over all elements and adjust their styles
        allElements.forEach(element => {
            const computedStyle = window.getComputedStyle(element);
            
            // Parse and adjust font size
            const currentFontSize = parseFloat(computedStyle.fontSize);
            if (!isNaN(currentFontSize)) {
                element.style.fontSize = (currentFontSize * fontSizeFactor) + 'px';
            }

            // Parse and adjust line height
            const currentLineHeight = parseFloat(computedStyle.lineHeight);
            if (!isNaN(currentLineHeight) && currentLineHeight !== 'normal') {
                element.style.lineHeight = (currentLineHeight * lineHeightFactor) + 'px';
            }
        });
    } catch (error) {
        // Log error to the console for debugging purposes
        console.error('Error adjusting accessibility settings:', error.message);
    }
}

// Example usage:
// Increase font size by 20% and line height by 50%
// adjustAccessibilitySettings(1.2, 1.5);
```
