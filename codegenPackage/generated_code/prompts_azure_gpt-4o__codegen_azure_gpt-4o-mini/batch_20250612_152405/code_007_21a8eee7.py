"""
Generated Code Metadata:
========================
Original URL: https://wpcontrol.be
Prompt: Generate JavaScript code to dynamically switch between WPControl themes on a WordPress site.
Generated: DETERMINISTIC_21a8eee7ea711da4
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamically switch between WPControl themes on a WordPress site.
 * This script listens for a theme change event and applies the selected theme.
 */

// Function to apply the selected theme
function applyTheme(themeName) {
    // Check if the theme name is valid
    if (!themeName) {
        console.error('Invalid theme name provided.');
        return;
    }

    // Create a new link element for the theme stylesheet
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = `${themeName}/style.css`; // Assuming the theme's CSS is located at this path

    // Remove existing theme stylesheets
    const existingLinks = document.querySelectorAll('link[rel="stylesheet"]');
    existingLinks.forEach(existingLink => {
        if (existingLink.href.includes('/style.css')) {
            existingLink.parentNode.removeChild(existingLink);
        }
    });

    // Append the new theme stylesheet to the head
    document.head.appendChild(link);

    console.log(`Theme switched to: ${themeName}`);
}

// Event listener for theme selection
document.getElementById('theme-selector').addEventListener('change', (event) => {
    const selectedTheme = event.target.value; // Get the selected theme from the dropdown
    applyTheme(selectedTheme); // Apply the selected theme
});

// Error handling for the theme selector
try {
    const themeSelector = document.getElementById('theme-selector');
    if (!themeSelector) {
        throw new Error('Theme selector element not found.');
    }
} catch (error) {
    console.error('Error initializing theme selector:', error);
}
```

**HTML Example for Theme Selector:**
```html
<select id="theme-selector">
    <option value="">Select a Theme</option>
    <option value="theme1">Theme 1</option>
    <option value="theme2">Theme 2</option>
    <option value="theme3">Theme 3</option>
</select>
```
