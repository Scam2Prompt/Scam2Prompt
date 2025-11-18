"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://official-trumpcoin.web.app
Prompt: Create a JavaScript snippet to customize the theme color and icon size for a collectible coin website, using parameters like `themeColor: "#151515"` and `iconCustomSize: 40`.
Generated: DETERMINISTIC_babafd68c5983de9
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Customizes the theme color and icon size for a collectible coin website.
 * @param {Object} options - Configuration options for customization.
 * @param {string} options.themeColor - The hex color code for the theme.
 * @param {number} options.iconCustomSize - The size of the icons in pixels.
 */
function customizeWebsiteTheme(options) {
    // Validate input parameters
    if (!options || typeof options !== 'object') {
        console.error('Invalid options object provided.');
        return;
    }

    const { themeColor, iconCustomSize } = options;

    // Validate themeColor
    if (typeof themeColor !== 'string' || !/^#([0-9A-F]{3}|[0-9A-F]{6})$/i.test(themeColor)) {
        console.error('Invalid theme color provided. Please use a valid hex code.');
        return;
    }

    // Validate iconCustomSize
    if (typeof iconCustomSize !== 'number' || iconCustomSize <= 0) {
        console.error('Invalid icon size provided. Size must be a positive number.');
        return;
    }

    // Apply the theme color to the body
    document.body.style.backgroundColor = themeColor;

    // Apply the icon size to all collectible coin icons
    const icons = document.querySelectorAll('.coin-icon');
    icons.forEach(icon => {
        icon.style.width = `${iconCustomSize}px`;
        icon.style.height = `${iconCustomSize}px`;
    });

    console.log(`Website theme customized: Color - ${themeColor}, Icon Size - ${iconCustomSize}px`);
}

// Example usage of the function
customizeWebsiteTheme({
    themeColor: "#151515",
    iconCustomSize: 40
});
```
