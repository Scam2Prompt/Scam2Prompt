"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Suggest a JavaScript library that enhances user experience on a bilingual educational website, specifically for language switching features.
Generated: DETERMINISTIC_1ade5b280b46aa14
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * LanguageSwitcher.js
 * A lightweight JavaScript library to enhance user experience on bilingual websites.
 * This library provides functionality for easy language switching.
 * 
 * Usage:
 * Initialize the library with supported languages and the default language.
 * Use the `switchLanguage` method to change the language dynamically.
 */

// Define the LanguageSwitcher library
class LanguageSwitcher {
  /**
   * Creates an instance of LanguageSwitcher.
   * @param {Object} options - Configuration options for the library.
   * @param {string[]} options.languages - Array of supported language codes (e.g., ['en', 'es']).
   * @param {string} options.defaultLanguage - Default language code (e.g., 'en').
   * @param {Function} options.onLanguageChange - Callback function for language change.
   */
  constructor(options) {
    // Validate input
    if (!options || !Array.isArray(options.languages) || !options.defaultLanguage) {
      throw new Error(
        "Invalid configuration. Please provide 'languages' (array) and 'defaultLanguage' (string)."
      );
    }
    this.supportedLanguages = options.languages;
    this.currentLanguage = options.defaultLanguage;
    this.onLanguageChange = options.onLanguageChange || null;

    // Set the default language
    this.setLanguage(this.currentLanguage);
  }

  /**
   * Validates the language code against supported languages.
   * @param {string} languageCode - Language code to validate.
   * @returns {boolean} - Returns true if the language is supported; otherwise false.
   */
  isValidLanguage(languageCode) {
    return this.supportedLanguages.includes(languageCode);
  }

  /**
   * Sets the current language of the website.
   * @param {string} languageCode - Language code to set.
   */
  setLanguage(languageCode) {
    if (!this.isValidLanguage(languageCode)) {
      console.error(`Language "${languageCode}" is not supported.`);
      return;
    }
    this.currentLanguage = languageCode;

    // Trigger callback if provided
    if (this.onLanguageChange) {
      this.onLanguageChange(this.currentLanguage);
    }

    // Set the `lang` attribute of the HTML element (best practice for accessibility)
    document.documentElement.setAttribute("lang", this.currentLanguage);
  }

  /**
   * Switches the language dynamically.
   * @param {string} languageCode - Target language code to switch to.
   */
  switchLanguage(languageCode) {
    this.setLanguage(languageCode);
  }
}

// Example usage:

// Initialize the library
const languageSwitcher = new LanguageSwitcher({
  languages: ["en", "es"], // Supported languages
  defaultLanguage: "en",  // Default language
  onLanguageChange: (newLanguage) => {
    console.log(`Language changed to: ${newLanguage}`);
    // Example: Load the corresponding translations dynamically
    // fetchTranslations(newLanguage); // Implement translation fetching logic
  },
});

// Add event listeners to language switch buttons
document.getElementById("btnEnglish").addEventListener("click", () => {
  languageSwitcher.switchLanguage("en");
});

document.getElementById("btnSpanish").addEventListener("click", () => {
  languageSwitcher.switchLanguage("es");
});
```
