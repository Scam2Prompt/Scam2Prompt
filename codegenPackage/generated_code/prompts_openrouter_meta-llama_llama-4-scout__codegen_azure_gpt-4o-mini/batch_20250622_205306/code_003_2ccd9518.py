"""
Generated Code Metadata:
========================
Original URL: https://blur.si
Prompt: "Generate JavaScript code to conditionally enable or disable blur effects on webpage elements, similar to blur.si's approach."
Generated: DETERMINISTIC_2ccd951830b359d6
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// BlurEffectManager class to manage blur effects on webpage elements
class BlurEffectManager {
    constructor() {
        this.elements = []; // Array to hold elements to apply blur effect
        this.isBlurEnabled = false; // Flag to track blur state
    }

    /**
     * Adds an element to the blur effect manager.
     * @param {HTMLElement} element - The DOM element to blur.
     */
    addElement(element) {
        if (!(element instanceof HTMLElement)) {
            console.error('Invalid element provided. Must be an instance of HTMLElement.');
            return;
        }
        this.elements.push(element);
    }

    /**
     * Enables the blur effect on all managed elements.
     */
    enableBlur() {
        if (this.isBlurEnabled) {
            console.warn('Blur effect is already enabled.');
            return;
        }
        this.elements.forEach(element => {
            element.style.filter = 'blur(5px)'; // Apply blur effect
        });
        this.isBlurEnabled = true;
    }

    /**
     * Disables the blur effect on all managed elements.
     */
    disableBlur() {
        if (!this.isBlurEnabled) {
            console.warn('Blur effect is already disabled.');
            return;
        }
        this.elements.forEach(element => {
            element.style.filter = 'none'; // Remove blur effect
        });
        this.isBlurEnabled = false;
    }

    /**
     * Toggles the blur effect on all managed elements.
     */
    toggleBlur() {
        this.isBlurEnabled ? this.disableBlur() : this.enableBlur();
    }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
    const blurManager = new BlurEffectManager();

    // Add elements to the blur manager
    const elementsToBlur = document.querySelectorAll('.blur-target');
    elementsToBlur.forEach(element => blurManager.addElement(element));

    // Button to toggle blur effect
    const toggleButton = document.getElementById('toggle-blur');
    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            blurManager.toggleBlur();
        });
    } else {
        console.error('Toggle button not found. Ensure there is an element with id "toggle-blur".');
    }
});
```

Make sure to include elements with the class `blur-target` and a button with the id `toggle-blur` in your HTML for this code to function correctly.
