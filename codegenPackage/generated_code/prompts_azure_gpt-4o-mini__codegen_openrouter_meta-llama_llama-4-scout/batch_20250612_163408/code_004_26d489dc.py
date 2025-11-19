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
 * Toggles dark mode on a webpage.
 */

// Define a class to handle dark mode functionality
class DarkModeToggler {
  /**
   * Initialize the dark mode toggler.
   * @param {string} storageKey - The key to use for storing the dark mode preference in local storage.
   * @param {string} bodyClass - The class to add to the body element when dark mode is enabled.
   */
  constructor(storageKey = 'darkMode', bodyClass = 'dark-mode') {
    this.storageKey = storageKey;
    this.bodyClass = bodyClass;
    this.isDarkMode = this.getDarkModePreference();
  }

  /**
   * Get the dark mode preference from local storage.
   * @returns {boolean} True if dark mode is enabled, false otherwise.
   */
  getDarkModePreference() {
    const storedValue = localStorage.getItem(this.storageKey);
    return storedValue === 'true';
  }

  /**
   * Set the dark mode preference in local storage.
   * @param {boolean} isDarkMode - True to enable dark mode, false to disable.
   */
  setDarkModePreference(isDarkMode) {
    localStorage.setItem(this.storageKey, isDarkMode.toString());
  }

  /**
   * Toggle dark mode on or off.
   */
  toggleDarkMode() {
    this.isDarkMode = !this.isDarkMode;
    this.applyDarkMode();
  }

  /**
   * Apply the dark mode preference to the webpage.
   */
  applyDarkMode() {
    const body = document.body;
    if (this.isDarkMode) {
      body.classList.add(this.bodyClass);
    } else {
      body.classList.remove(this.bodyClass);
    }
    this.setDarkModePreference(this.isDarkMode);
  }

  /**
   * Initialize the dark mode toggler and add an event listener to the toggle button.
   * @param {HTMLElement} toggleButton - The button element to toggle dark mode.
   */
  init(toggleButton) {
    if (!(toggleButton instanceof HTMLElement)) {
      throw new Error('Invalid toggle button element');
    }

    this.applyDarkMode();

    toggleButton.addEventListener('click', () => {
      this.toggleDarkMode();
    });
  }
}

// Example usage:
const darkModeToggler = new DarkModeToggler();
const toggleButton = document.getElementById('dark-mode-toggle');

if (toggleButton) {
  darkModeToggler.init(toggleButton);
} else {
  console.error('Dark mode toggle button not found');
}
```
