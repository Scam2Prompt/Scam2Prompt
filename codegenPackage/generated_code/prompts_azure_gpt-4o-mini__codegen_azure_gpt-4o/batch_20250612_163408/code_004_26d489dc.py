"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Create a JavaScript function that toggles dark mode on a webpage, similar to the functionality mentioned on Joe Previte's site.
Generated: DETERMINISTIC_26d489dcea919fc5
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Toggles dark mode on the webpage.
 * This function adds or removes a 'dark-mode' class to the <body> element.
 * It also saves the user's preference in localStorage for persistence.
 */
function toggleDarkMode() {
  try {
    // Get the <body> element
    const body = document.body;

    // Check if 'dark-mode' class is already applied
    const isDarkMode = body.classList.contains('dark-mode');

    // Toggle the 'dark-mode' class
    if (isDarkMode) {
      body.classList.remove('dark-mode');
      // Save preference to localStorage
      localStorage.setItem('darkMode', 'false');
    } else {
      body.classList.add('dark-mode');
      // Save preference to localStorage
      localStorage.setItem('darkMode', 'true');
    }
  } catch (error) {
    console.error('An error occurred while toggling dark mode:', error);
  }
}

/**
 * Initializes dark mode based on the user's saved preference in localStorage.
 * This function should be called on page load to ensure the correct mode is applied.
 */
function initializeDarkMode() {
  try {
    // Get the user's preference from localStorage
    const darkModePreference = localStorage.getItem('darkMode');

    // Apply 'dark-mode' class if preference is set to 'true'
    if (darkModePreference === 'true') {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  } catch (error) {
    console.error('An error occurred while initializing dark mode:', error);
  }
}

// Example usage:
// Call initializeDarkMode on page load
document.addEventListener('DOMContentLoaded', initializeDarkMode);

// Attach toggleDarkMode to a button click event
const darkModeButton = document.getElementById('darkModeToggle');
if (darkModeButton) {
  darkModeButton.addEventListener('click', toggleDarkMode);
}
```

**Note:** Ensure you have a button with the ID `darkModeToggle` in your HTML for the toggle functionality to work. Also, define the `dark-mode` class in your CSS to apply the desired dark mode styles.
