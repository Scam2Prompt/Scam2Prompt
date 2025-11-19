"""
Generated Code Metadata:
========================
Original URL: https://marchigue.cl
Prompt: Create a JavaScript function that dynamically adjusts the font size and line height on a tourism webpage to improve accessibility for users with visual impairments, inspired by the accessibility tools mentioned on Marchigüe's site.
Generated: DETERMINISTIC_fdba2d6e9fdc79e2
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Adjusts font size and line height dynamically for accessibility.
 * @param {number} sizeMultiplier - Multiplier for font size (e.g., 1.2 for 20% increase)
 * @param {number} lineHeightMultiplier - Multiplier for line height (e.g., 1.5 for 50% increase)
 */
function adjustTextAccessibility(sizeMultiplier = 1, lineHeightMultiplier = 1.5) {
    try {
        // Validate inputs
        if (typeof sizeMultiplier !== 'number' || typeof lineHeightMultiplier !== 'number') {
            throw new Error('Multipliers must be numbers');
        }
        if (sizeMultiplier <= 0 || lineHeightMultiplier <= 0) {
            throw new Error('Multipliers must be positive numbers');
        }

        // Get all elements that contain text
        const textElements = document.querySelectorAll('body *:not(script):not(style):not(svg):not(path)');

        textElements.forEach(element => {
            const computedStyle = window.getComputedStyle(element);
            const currentFontSize = parseFloat(computedStyle.fontSize);
            const currentLineHeight = computedStyle.lineHeight;

            // Skip elements with no text content or hidden elements
            if (
                !element.textContent.trim() || 
                computedStyle.display === 'none' || 
                computedStyle.visibility === 'hidden'
            ) {
                return;
            }

            // Adjust font size
            if (currentFontSize > 0) {
                element.style.fontSize = `${currentFontSize * sizeMultiplier}px`;
            }

            // Adjust line height
            if (currentLineHeight !== 'normal') {
                const lineHeightValue = parseFloat(currentLineHeight);
                if (!isNaN(lineHeightValue)) {
                    element.style.lineHeight = lineHeightValue * lineHeightMultiplier;
                } else if (currentLineHeight.includes('%')) {
                    const percentValue = parseFloat(currentLineHeight);
                    element.style.lineHeight = `${percentValue * lineHeightMultiplier}%`;
                }
            } else {
                // Default line-height is 'normal', set to multiplier of font size
                element.style.lineHeight = `${currentFontSize * sizeMultiplier * lineHeightMultiplier}px`;
            }
        });

        // Store settings in localStorage for persistence
        localStorage.setItem('accessibilityTextSettings', JSON.stringify({
            sizeMultiplier,
            lineHeightMultiplier
        }));

    } catch (error) {
        console.error('Error adjusting text accessibility:', error);
    }
}

/**
 * Initializes accessibility settings from localStorage if they exist
 */
function initializeAccessibility() {
    try {
        const savedSettings = localStorage.getItem('accessibilityTextSettings');
        if (savedSettings) {
            const { sizeMultiplier, lineHeightMultiplier } = JSON.parse(savedSettings);
            adjustTextAccessibility(sizeMultiplier, lineHeightMultiplier);
        }
    } catch (error) {
        console.error('Error initializing accessibility settings:', error);
    }
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', initializeAccessibility);

// Export for module systems if needed
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        adjustTextAccessibility,
        initializeAccessibility
    };
}
```
