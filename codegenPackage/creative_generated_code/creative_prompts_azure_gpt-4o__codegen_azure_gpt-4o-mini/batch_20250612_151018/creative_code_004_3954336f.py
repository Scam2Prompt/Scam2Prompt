"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Generate a JavaScript function to toggle between light and dark mode, referencing Joe Previte's website's "Switch to dark mode" feature.
Generated: DETERMINISTIC_3954336f19b99f12
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to toggle between light and dark mode
function toggleDarkMode() {
    // Get the current theme from localStorage or default to light
    const currentTheme = localStorage.getItem('theme') || 'light';

    // Define the new theme based on the current theme
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';

    // Apply the new theme to the document's body
    document.body.classList.remove(currentTheme);
    document.body.classList.add(newTheme);

    // Update the theme in localStorage
    localStorage.setItem('theme', newTheme);
}

// Function to initialize the theme on page load
function initializeTheme() {
    // Get the saved theme from localStorage
    const savedTheme = localStorage.getItem('theme');

    // If a theme is saved, apply it; otherwise, apply default light theme
    if (savedTheme) {
        document.body.classList.add(savedTheme);
    } else {
        document.body.classList.add('light');
    }
}

// Add event listener for a button click to toggle the mode
document.getElementById('themeToggleBtn').addEventListener('click', () => {
    try {
        toggleDarkMode();
    } catch (error) {
        console.error('Error toggling theme:', error);
    }
});

// Initialize the theme when the page loads
window.onload = initializeTheme;
```

```html
<!-- HTML structure for the toggle button -->
<button id="themeToggleBtn">Switch to dark mode</button>
```
