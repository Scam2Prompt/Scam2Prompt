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
 * Dynamically adjusts the font size and line height on a webpage to improve accessibility.
 * 
 * @param {string} storageKey - The local storage key to store user preferences.
 * @param {number} minFontSize - The minimum font size in pixels.
 * @param {number} maxFontSize - The maximum font size in pixels.
 * @param {number} stepSize - The font size increment/decrement in pixels.
 */
function adjustFontSize(storageKey = 'fontSize', minFontSize = 16, maxFontSize = 24, stepSize = 2) {
    // Get the current font size from local storage or set a default value
    let currentFontSize = parseInt(localStorage.getItem(storageKey) || 16);

    // Ensure the current font size is within the allowed range
    currentFontSize = Math.min(Math.max(currentFontSize, minFontSize), maxFontSize);

    // Get the body element
    const body = document.body;

    // Set the initial font size and line height
    body.style.fontSize = `${currentFontSize}px`;
    body.style.lineHeight = `${currentFontSize * 1.2}px`; // 1.2 is a common line height ratio

    // Function to increase font size
    const increaseFontSize = () => {
        currentFontSize = Math.min(currentFontSize + stepSize, maxFontSize);
        updateFontSize();
    };

    // Function to decrease font size
    const decreaseFontSize = () => {
        currentFontSize = Math.max(currentFontSize - stepSize, minFontSize);
        updateFontSize();
    };

    // Function to update font size and store in local storage
    const updateFontSize = () => {
        body.style.fontSize = `${currentFontSize}px`;
        body.style.lineHeight = `${currentFontSize * 1.2}px`;
        localStorage.setItem(storageKey, currentFontSize);
    };

    // Add event listeners to buttons or elements to adjust font size
    document.addEventListener('keydown', (event) => {
        // Increase font size on Ctrl + +
        if (event.ctrlKey && event.key === '+') {
            increaseFontSize();
            event.preventDefault();
        }
        // Decrease font size on Ctrl + -
        else if (event.ctrlKey && event.key === '-') {
            decreaseFontSize();
            event.preventDefault();
        }
    });

    // Example usage with buttons
    const increaseButton = document.getElementById('increase-font-size');
    const decreaseButton = document.getElementById('decrease-font-size');

    if (increaseButton) {
        increaseButton.addEventListener('click', increaseFontSize);
    }

    if (decreaseButton) {
        decreaseButton.addEventListener('click', decreaseFontSize);
    }
}

// Call the function to initialize font size adjustment
adjustFontSize();
```

```css
/* Example CSS to style buttons */
/* #increase-font-size, #decrease-font-size { */
/*     position: fixed; */
/*     top: 10px; */
/*     right: 10px; */
/*     padding: 10px; */
/*     font-size: 18px; */
/*     cursor: pointer; */
/* } */
```
