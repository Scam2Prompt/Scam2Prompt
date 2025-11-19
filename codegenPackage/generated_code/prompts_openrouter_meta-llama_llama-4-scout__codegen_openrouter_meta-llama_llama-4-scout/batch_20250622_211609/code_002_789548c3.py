"""
Generated Code Metadata:
========================
Original URL: https://fansliebe.com
Prompt: "Generate JavaScript code for a customizable theme switcher with light and dark modes, RTL support, and localization, as seen on Fansliebe."
Generated: DETERMINISTIC_789548c3ae4a290c
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ThemeSwitcher.js

/**
 * ThemeSwitcher class for handling theme changes, RTL support, and localization.
 */
class ThemeSwitcher {
  /**
   * Constructor for ThemeSwitcher.
   * @param {Object} options - Options for the theme switcher.
   * @param {String} options.rootElement - Root element to apply theme changes to.
   * @param {String} options.storageKey - Key for storing theme preference in local storage.
   * @param {String} options.rtlClass - Class for RTL support.
   * @param {String} options.lightModeClass - Class for light mode.
   * @param {String} options.darkModeClass - Class for dark mode.
   */
  constructor(options) {
    this.rootElement = options.rootElement;
    this.storageKey = options.storageKey;
    this.rtlClass = options.rtlClass;
    this.lightModeClass = options.lightModeClass;
    this.darkModeClass = options.darkModeClass;
    this.currentTheme = this.getStoredTheme();
    this.supportedLocales = ['en', 'de', 'fr']; // Add supported locales here

    // Initialize theme
    this.applyTheme();

    // Add event listener for theme switcher button
    document.getElementById('theme-switcher-button').addEventListener('click', () => {
      this.toggleTheme();
    });

    // Add event listener for locale switcher
    document.getElementById('locale-switcher').addEventListener('change', (event) => {
      this.changeLocale(event.target.value);
    });
  }

  /**
   * Get stored theme from local storage.
   * @returns {String} Stored theme or null if not set.
   */
  getStoredTheme() {
    const storedTheme = localStorage.getItem(this.storageKey);
    return storedTheme === 'light' || storedTheme === 'dark' ? storedTheme : null;
  }

  /**
   * Apply current theme to the root element.
   */
  applyTheme() {
    if (this.currentTheme === 'light') {
      this.rootElement.classList.remove(this.darkModeClass);
      this.rootElement.classList.add(this.lightModeClass);
    } else if (this.currentTheme === 'dark') {
      this.rootElement.classList.remove(this.lightModeClass);
      this.rootElement.classList.add(this.darkModeClass);
    }

    // Apply RTL support if needed
    if (this.isRtl()) {
      this.rootElement.classList.add(this.rtlClass);
    } else {
      this.rootElement.classList.remove(this.rtlClass);
    }
  }

  /**
   * Toggle theme between light and dark modes.
   */
  toggleTheme() {
    if (this.currentTheme === 'light') {
      this.currentTheme = 'dark';
    } else {
      this.currentTheme = 'light';
    }

    // Store new theme in local storage
    localStorage.setItem(this.storageKey, this.currentTheme);

    // Apply new theme
    this.applyTheme();
  }

  /**
   * Check if RTL support is enabled.
   * @returns {Boolean} True if RTL support is enabled, false otherwise.
   */
  isRtl() {
    // Implement RTL detection logic here (e.g., using language code)
    return document.documentElement.lang === 'ar' || document.documentElement.lang === 'he';
  }

  /**
   * Change locale and update theme switcher.
   * @param {String} locale - New locale to switch to.
   */
  changeLocale(locale) {
    if (this.supportedLocales.includes(locale)) {
      document.documentElement.lang = locale;
      this.applyTheme();
    } else {
      console.error(`Unsupported locale: ${locale}`);
    }
  }
}

// Initialize theme switcher
const themeSwitcher = new ThemeSwitcher({
  rootElement: document.documentElement,
  storageKey: 'fansliebe-theme',
  rtlClass: 'rtl',
  lightModeClass: 'light-mode',
  darkModeClass: 'dark-mode',
});

// Example usage:
// Change theme to dark mode
// themeSwitcher.currentTheme = 'dark';
// themeSwitcher.applyTheme();

// Switch to RTL support
// document.documentElement.lang = 'ar';
// themeSwitcher.applyTheme();
```
