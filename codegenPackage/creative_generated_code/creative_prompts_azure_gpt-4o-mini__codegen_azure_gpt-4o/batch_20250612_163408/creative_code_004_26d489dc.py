"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Create a JavaScript function that toggles dark mode on a webpage, similar to the functionality mentioned on Joe Previte's site.
Generated: DETERMINISTIC_26d489dcea919fc5
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Toggles dark mode on the webpage.
 * 
 * - Adds or removes the 'dark-mode' class to the <body> element.
 * - Persists the user's preference in localStorage.
 * - Automatically applies the preference on subsequent visits.
 */

// Function to initialize dark mode based on user preference
function initializeDarkMode() {
  try {
    const prefersDarkMode = localStorage.getItem('darkMode');
    if (prefersDarkMode === 'enabled') {
      document.body.classList.add('dark-mode'); // Apply dark mode
    }
  } catch (error) {
    console.error('Error initializing dark mode:', error);
  }
}

// Function to toggle dark mode
function toggleDarkMode() {
  try {
    const bodyElement = document.body; // Reference to the <body> element
    const isDarkModeEnabled = bodyElement.classList.contains('dark-mode');

    if (isDarkModeEnabled) {
      bodyElement.classList.remove('dark-mode'); // Disable dark mode
      localStorage.setItem('darkMode', 'disabled'); // Save user preference
    } else {
      bodyElement.classList.add('dark-mode'); // Enable dark mode
      localStorage.setItem('darkMode', 'enabled'); // Save user preference
    }
  } catch (error) {
    console.error('Error toggling dark mode:', error);
  }
}

// Initialize dark mode on page load
document.addEventListener('DOMContentLoaded', initializeDarkMode);
```

### Usage:
- Add a `dark-mode` class to your CSS with the desired dark-mode styling.
- Call `toggleDarkMode()` when the user clicks a button or performs an action to toggle between light and dark modes.
