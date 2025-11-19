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
 * Dynamically adjusts font size and line height on a webpage to improve accessibility.
 * This function allows users to increase or decrease font size and line height
 * for better readability, inspired by accessibility tools.
 */

// Function to adjust font size and line height
function adjustAccessibility(fontSizeChange, lineHeightChange) {
  try {
    // Get all elements on the page
    const elements = document.querySelectorAll('*');

    // Loop through each element and adjust styles
    elements.forEach((element) => {
      // Get current font size and line height
      const currentFontSize = window.getComputedStyle(element).fontSize;
      const currentLineHeight = window.getComputedStyle(element).lineHeight;

      // Parse current values to numbers
      const fontSizeValue = parseFloat(currentFontSize);
      const lineHeightValue = parseFloat(currentLineHeight);

      // Calculate new values
      const newFontSize = fontSizeValue + fontSizeChange;
      const newLineHeight = lineHeightValue + lineHeightChange;

      // Apply new styles
      element.style.fontSize = `${newFontSize}px`;
      element.style.lineHeight = `${newLineHeight}px`;
    });
  } catch (error) {
    console.error('Error adjusting accessibility settings:', error);
  }
}

/**
 * Example usage:
 * Increase font size by 2px and line height by 2px:
 * adjustAccessibility(2, 2);
 * 
 * Decrease font size by 2px and line height by 2px:
 * adjustAccessibility(-2, -2);
 */

// Add event listeners for buttons to control accessibility
document.getElementById('increase-accessibility').addEventListener('click', () => {
  adjustAccessibility(2, 2); // Increase font size and line height
});

document.getElementById('decrease-accessibility').addEventListener('click', () => {
  adjustAccessibility(-2, -2); // Decrease font size and line height
});
```

**Note:** Ensure that the HTML contains buttons with IDs `increase-accessibility` and `decrease-accessibility` for the event listeners to work.
