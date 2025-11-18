"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokoswap-admin-build.pages.dev
Prompt: Generate a JavaScript snippet to toggle dark mode in a minimal UI kit for an admin dashboard.
Generated: DETERMINISTIC_6f328e2d06bcb050
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to toggle dark mode
function toggleDarkMode() {
    // Get the current theme from local storage or default to 'light'
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Toggle the theme
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    // Set the new theme to the body class
    document.body.className = newTheme;

    // Save the new theme to local storage
    localStorage.setItem('theme', newTheme);
}

// Function to initialize the theme on page load
function initializeTheme() {
    // Check for the saved theme in local storage
    const savedTheme = localStorage.getItem('theme') || 'light';
    
    // Set the body class to the saved theme
    document.body.className = savedTheme;
}

// Event listener for the dark mode toggle button
document.addEventListener('DOMContentLoaded', () => {
    // Initialize the theme on page load
    initializeTheme();

    // Get the toggle button element
    const toggleButton = document.getElementById('dark-mode-toggle');
    
    // Ensure the toggle button exists in the DOM
    if (toggleButton) {
        // Add event listener for click event
        toggleButton.addEventListener('click', () => {
            try {
                toggleDarkMode();
            } catch (error) {
                console.error('Error toggling dark mode:', error);
            }
        });
    } else {
        console.warn('Toggle button not found in the DOM');
    }
});
```

```html
<!-- Include this HTML snippet in your admin dashboard -->
<button id="dark-mode-toggle">Toggle Dark Mode</button>
```

```css
/* Basic styles for light and dark themes */
body.light {
    background-color: #ffffff;
    color: #000000;
}

body.dark {
    background-color: #000000;
    color: #ffffff;
}
```
