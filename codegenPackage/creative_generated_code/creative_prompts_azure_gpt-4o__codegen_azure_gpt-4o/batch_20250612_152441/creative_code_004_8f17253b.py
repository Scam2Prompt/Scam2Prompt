"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-ten.pages.dev
Prompt: Write a function in JavaScript to toggle between light and dark themes on the Ten Gateway interface.
Generated: DETERMINISTIC_8f17253b87d363fd
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Toggles between light and dark themes on the Ten Gateway interface.
 * This function updates the CSS class on the `body` element and stores the
 * user's preferred theme in localStorage for persistence across sessions.
 */

// Function to toggle light and dark themes
function toggleTheme() {
  // Get the body element
  const body = document.body;

  // Check the current theme by inspecting the body's class list
  const currentTheme = body.classList.contains('dark-theme') ? 'dark' : 'light';

  // Toggle the theme
  if (currentTheme === 'dark') {
    // Switch to light theme
    body.classList.remove('dark-theme');
    body.classList.add('light-theme');
    // Store the user's preference in localStorage
    localStorage.setItem('theme', 'light');
  } else {
    // Switch to dark theme
    body.classList.remove('light-theme');
    body.classList.add('dark-theme');
    // Store the user's preference in localStorage
    localStorage.setItem('theme', 'dark');
  }
}

/**
 * Initializes the theme based on user preference stored in localStorage.
 * If no preference is stored, defaults to light theme.
 */
function initializeTheme() {
  // Get the user's preferred theme from localStorage
  const savedTheme = localStorage.getItem('theme');

  // Set the theme based on the saved preference or default to light
  if (savedTheme === 'dark') {
    document.body.classList.add('dark-theme');
  } else {
    document.body.classList.add('light-theme');
  }
}

// Event listener to bind the toggleTheme function to a button
document.addEventListener('DOMContentLoaded', () => {
  // Initialize the theme on page load
  initializeTheme();

  // Assume there's a button with an ID of 'theme-toggle' for toggling themes
  const themeToggleButton = document.getElementById('theme-toggle');

  if (themeToggleButton) {
    themeToggleButton.addEventListener('click', toggleTheme);
  } else {
    console.error("Theme toggle button with ID 'theme-toggle' not found.");
  }
});
```
