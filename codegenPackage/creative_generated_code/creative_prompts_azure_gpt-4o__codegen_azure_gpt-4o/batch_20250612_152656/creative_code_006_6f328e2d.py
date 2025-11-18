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
/**
 * Toggles dark mode for an admin dashboard UI.
 * Adds/removes the "dark-mode" class on the root element.
 * Saves the dark mode preference in localStorage.
 */

// Function to toggle dark mode
function toggleDarkMode() {
  try {
    const rootElement = document.documentElement; // Refers to the <html> element
    const darkModeClass = 'dark-mode';

    // Check if dark mode is currently active
    const isDarkModeActive = rootElement.classList.contains(darkModeClass);

    // Toggle the class
    if (isDarkModeActive) {
      rootElement.classList.remove(darkModeClass);
      localStorage.setItem('darkMode', 'off'); // Save preference to localStorage
    } else {
      rootElement.classList.add(darkModeClass);
      localStorage.setItem('darkMode', 'on'); // Save preference to localStorage
    }
  } catch (error) {
    console.error('An error occurred while toggling dark mode:', error);
  }
}

// Function to initialize dark mode based on saved preference
function initializeDarkMode() {
  try {
    const rootElement = document.documentElement; // Refers to the <html> element
    const darkModeClass = 'dark-mode';
    const savedPreference = localStorage.getItem('darkMode');

    // Apply dark mode if the saved preference is "on"
    if (savedPreference === 'on') {
      rootElement.classList.add(darkModeClass);
    } else {
      rootElement.classList.remove(darkModeClass);
    }
  } catch (error) {
    console.error('An error occurred while initializing dark mode:', error);
  }
}

// Event listener for toggling dark mode (e.g., when a button is clicked)
document.getElementById('darkModeToggleButton').addEventListener('click', toggleDarkMode);

// Initialize dark mode when the page loads
document.addEventListener('DOMContentLoaded', initializeDarkMode);
```
