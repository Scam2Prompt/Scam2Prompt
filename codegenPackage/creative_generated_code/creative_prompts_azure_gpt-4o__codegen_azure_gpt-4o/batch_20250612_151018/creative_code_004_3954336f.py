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
/**
 * Function to toggle between light and dark modes.
 * This uses localStorage to save the user's preference and updates the document's class accordingly.
 */
function toggleDarkMode() {
  try {
    // Get the current theme from localStorage
    const currentTheme = localStorage.getItem('theme');

    // Check if the current theme is dark
    if (currentTheme === 'dark') {
      // Switch to light mode
      document.documentElement.classList.remove('dark-mode');
      localStorage.setItem('theme', 'light');
    } else {
      // Switch to dark mode
      document.documentElement.classList.add('dark-mode');
      localStorage.setItem('theme', 'dark');
    }
  } catch (error) {
    // Log any errors encountered
    console.error('An error occurred while toggling dark mode:', error);
  }
}

/**
 * Function to initialize the theme based on the saved preference in localStorage.
 * Call this function on page load to ensure the correct theme is applied.
 */
function initializeTheme() {
  try {
    // Get the saved theme from localStorage
    const savedTheme = localStorage.getItem('theme');

    // Apply the saved theme to the document
    if (savedTheme === 'dark') {
      document.documentElement.classList.add('dark-mode');
    } else {
      document.documentElement.classList.remove('dark-mode');
    }
  } catch (error) {
    // Log any errors encountered
    console.error('An error occurred while initializing the theme:', error);
  }
}

// Example usage:
// Call `initializeTheme()` on page load to set the correct theme.
// Attach `toggleDarkMode()` to a button's click event to toggle themes.

// Initialize the theme when the page loads
window.addEventListener('DOMContentLoaded', initializeTheme);

// Example: Add event listener to a button (ensure the button exists in your HTML)
// const toggleButton = document.getElementById('theme-toggle-button');
// toggleButton.addEventListener('click', toggleDarkMode);
```
