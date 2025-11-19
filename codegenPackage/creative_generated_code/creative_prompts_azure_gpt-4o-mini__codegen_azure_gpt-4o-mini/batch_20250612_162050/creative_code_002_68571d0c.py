"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdbondindia.com
Prompt: Create a JavaScript function that allows users to customize the colors and sizes of signboards, inspired by the offerings at SD BOND India.
Generated: DETERMINISTIC_68571d0cb216c990
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Class representing a customizable signboard.
 */
class Signboard {
    /**
     * Create a signboard.
     * @param {string} text - The text to be displayed on the signboard.
     * @param {string} color - The color of the signboard text.
     * @param {string} backgroundColor - The background color of the signboard.
     * @param {string} size - The size of the signboard text (e.g., 'small', 'medium', 'large').
     */
    constructor(text, color, backgroundColor, size) {
        this.text = text;
        this.color = color;
        this.backgroundColor = backgroundColor;
        this.size = size;
        this.validateInputs();
    }

    /**
     * Validates the signboard inputs.
     * @throws {Error} Throws an error if any input is invalid.
     */
    validateInputs() {
        const validSizes = ['small', 'medium', 'large'];
        if (typeof this.text !== 'string' || this.text.trim() === '') {
            throw new Error('Invalid text: must be a non-empty string.');
        }
        if (typeof this.color !== 'string' || !this.isValidColor(this.color)) {
            throw new Error('Invalid color: must be a valid CSS color string.');
        }
        if (typeof this.backgroundColor !== 'string' || !this.isValidColor(this.backgroundColor)) {
            throw new Error('Invalid background color: must be a valid CSS color string.');
        }
        if (!validSizes.includes(this.size)) {
            throw new Error(`Invalid size: must be one of ${validSizes.join(', ')}.`);
        }
    }

    /**
     * Checks if a string is a valid CSS color.
     * @param {string} color - The color string to validate.
     * @returns {boolean} True if valid, false otherwise.
     */
    isValidColor(color) {
        const s = new Option().style;
        s.color = color;
        return s.color !== '';
    }

    /**
     * Renders the signboard to the DOM.
     * @param {HTMLElement} container - The container element to append the signboard to.
     */
    render(container) {
        const signboard = document.createElement('div');
        signboard.textContent = this.text;
        signboard.style.color = this.color;
        signboard.style.backgroundColor = this.backgroundColor;
        signboard.style.padding = '10px';
        signboard.style.border = '1px solid #000';
        
        switch (this.size) {
            case 'small':
                signboard.style.fontSize = '12px';
                break;
            case 'medium':
                signboard.style.fontSize = '16px';
                break;
            case 'large':
                signboard.style.fontSize = '20px';
                break;
        }

        container.appendChild(signboard);
    }
}

/**
 * Function to create and display a signboard with user-defined properties.
 * @param {string} text - The text for the signboard.
 * @param {string} textColor - The text color.
 * @param {string} bgColor - The background color.
 * @param {string} size - The size of the text.
 */
function createSignboard(text, textColor, bgColor, size) {
    try {
        const signboard = new Signboard(text, textColor, bgColor, size);
        const container = document.getElementById('signboard-container');
        if (!container) {
            throw new Error('Container element not found.');
        }
        signboard.render(container);
    } catch (error) {
        console.error('Error creating signboard:', error.message);
        alert(error.message); // Notify the user of the error
    }
}

// Example usage
// Assuming there is a div with id="signboard-container" in your HTML
// createSignboard('Welcome to SD BOND India', 'white', 'blue', 'medium');
```
