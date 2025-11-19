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
/**
 * ThemeSwitcher - A customizable theme switcher with light/dark modes, RTL support, and localization.
 * 
 * Features:
 * - Light/Dark mode switching
 * - RTL/LTR direction support
 * - Localization support
 * - Persistent settings via localStorage
 * - Event-based architecture
 * - Accessibility compliant
 */

class ThemeSwitcher {
  /**
   * @param {Object} options - Configuration options
   * @param {string} options.defaultTheme - Default theme ('light' or 'dark')
   * @param {string} options.defaultDirection - Default direction ('ltr' or 'rtl')
   * @param {string} options.defaultLanguage - Default language code (e.g., 'en')
   * @param {Object} options.localization - Localization strings
   */
  constructor(options = {}) {
    this.config = {
      defaultTheme: options.defaultTheme || 'light',
      defaultDirection: options.defaultDirection || 'ltr',
      defaultLanguage: options.defaultLanguage || 'en',
      localization: options.localization || {
        en: {
          light: 'Light',
          dark: 'Dark',
          rtl: 'RTL',
          ltr: 'LTR'
        }
      }
    };

    this.state = {
      theme: this.getSavedTheme(),
      direction: this.getSavedDirection(),
      language: this.getSavedLanguage()
    };

    this.init();
  }

  /**
   * Initialize the theme switcher
   */
  init() {
    this.applyTheme();
    this.applyDirection();
    this.applyLanguage();
    this.setupEventListeners();
  }

  /**
   * Get saved theme from localStorage or use default
   * @returns {string}
   */
  getSavedTheme() {
    try {
      return localStorage.getItem('theme') || this.config.defaultTheme;
    } catch (e) {
      console.error('Error accessing localStorage:', e);
      return this.config.defaultTheme;
    }
  }

  /**
   * Get saved direction from localStorage or use default
   * @returns {string}
   */
  getSavedDirection() {
    try {
      return localStorage.getItem('direction') || this.config.defaultDirection;
    } catch (e) {
      console.error('Error accessing localStorage:', e);
      return this.config.defaultDirection;
    }
  }

  /**
   * Get saved language from localStorage or use default
   * @returns {string}
   */
  getSavedLanguage() {
    try {
      return localStorage.getItem('language') || this.config.defaultLanguage;
    } catch (e) {
      console.error('Error accessing localStorage:', e);
      return this.config.defaultLanguage;
    }
  }

  /**
   * Apply current theme to the document
   */
  applyTheme() {
    document.documentElement.setAttribute('data-theme', this.state.theme);
    try {
      localStorage.setItem('theme', this.state.theme);
    } catch (e) {
      console.error('Error saving theme to localStorage:', e);
    }
  }

  /**
   * Apply current direction to the document
   */
  applyDirection() {
    document.documentElement.setAttribute('dir', this.state.direction);
    try {
      localStorage.setItem('direction', this.state.direction);
    } catch (e) {
      console.error('Error saving direction to localStorage:', e);
    }
  }

  /**
   * Apply current language to the document
   */
  applyLanguage() {
    document.documentElement.lang = this.state.language;
    try {
      localStorage.setItem('language', this.state.language);
    } catch (e) {
      console.error('Error saving language to localStorage:', e);
    }
  }

  /**
   * Setup event listeners for theme switcher UI
   */
  setupEventListeners() {
    document.addEventListener('DOMContentLoaded', () => {
      // Theme toggle button
      const themeToggle = document.getElementById('theme-toggle');
      if (themeToggle) {
        themeToggle.addEventListener('click', () => {
          this.toggleTheme();
        });
      }

      // Direction toggle button
      const directionToggle = document.getElementById('direction-toggle');
      if (directionToggle) {
        directionToggle.addEventListener('click', () => {
          this.toggleDirection();
        });
      }

      // Language selector
      const languageSelect = document.getElementById('language-select');
      if (languageSelect) {
        languageSelect.addEventListener('change', (e) => {
          this.setLanguage(e.target.value);
        });
      }
    });
  }

  /**
   * Toggle between light and dark themes
   */
  toggleTheme() {
    this.state.theme = this.state.theme === 'light' ? 'dark' : 'light';
    this.applyTheme();
    this.dispatchEvent('themeChange', { theme: this.state.theme });
  }

  /**
   * Toggle between RTL and LTR directions
   */
  toggleDirection() {
    this.state.direction = this.state.direction === 'ltr' ? 'rtl' : 'ltr';
    this.applyDirection();
    this.dispatchEvent('directionChange', { direction: this.state.direction });
  }

  /**
   * Set language
   * @param {string} lang - Language code
   */
  setLanguage(lang) {
    if (this.config.localization[lang]) {
      this.state.language = lang;
      this.applyLanguage();
      this.dispatchEvent('languageChange', { language: this.state.language });
    }
  }

  /**
   * Dispatch custom event
   * @param {string} eventName - Name of the event
   * @param {Object} detail - Event details
   */
  dispatchEvent(eventName, detail) {
    const event = new CustomEvent(eventName, { detail });
    document.dispatchEvent(event);
  }

  /**
   * Get localized string
   * @param {string} key - Localization key
   * @returns {string}
   */
  getLocalizedString(key) {
    const strings = this.config.localization[this.state.language] || this.config.localization[this.config.defaultLanguage];
    return strings[key] || key;
  }
}

// Example usage:
/*
document.addEventListener('DOMContentLoaded', () => {
  const themeSwitcher = new ThemeSwitcher({
    defaultTheme: 'light',
    defaultDirection: 'ltr',
    defaultLanguage: 'en',
    localization: {
      en: {
        light: 'Light',
        dark: 'Dark',
        rtl: 'Right-to-Left',
        ltr: 'Left-to-Right'
      },
      ar: {
        light: 'فاتح',
        dark: 'غامق',
        rtl: 'يمين-إلى-يسار',
        ltr: 'يسار-إلى-يمين'
      }
    }
  });

  // Listen for theme changes
  document.addEventListener('themeChange', (e) => {
    console.log('Theme changed to:', e.detail.theme);
  });

  // Listen for direction changes
  document.addEventListener('directionChange', (e) => {
    console.log('Direction changed to:', e.detail.direction);
  });

  // Listen for language changes
  document.addEventListener('languageChange', (e) => {
    console.log('Language changed to:', e.detail.language);
  });
});
*/
```
