"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.ire-coinbase.com
Prompt: How do I change the locale settings in a webmail interface to support multiple languages?
Generated: DETERMINISTIC_63bfaa283e54da44
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// LocaleManager.js

class LocaleManager {
    constructor() {
        // Supported languages
        this.supportedLocales = ['en', 'es', 'fr', 'de', 'zh'];
        // Default locale
        this.currentLocale = 'en';
        // Language resources
        this.languageResources = {
            en: { greeting: "Hello", farewell: "Goodbye" },
            es: { greeting: "Hola", farewell: "Adiós" },
            fr: { greeting: "Bonjour", farewell: "Au revoir" },
            de: { greeting: "Hallo", farewell: "Auf Wiedersehen" },
            zh: { greeting: "你好", farewell: "再见" }
        };
    }

    /**
     * Set the current locale if the requested locale is supported.
     * @param {string} locale - The locale code (e.g., 'en', 'es').
     * @throws Will throw an error if the locale is not supported.
     */
    setLocale(locale) {
        if (!this.supportedLocales.includes(locale)) {
            throw new Error(`Locale '${locale}' is not supported.`);
        }
        this.currentLocale = locale;
    }

    /**
     * Get the current locale.
     * @returns {string} The current locale.
     */
    getLocale() {
        return this.currentLocale;
    }

    /**
     * Get translation for a given key in the current locale.
     * @param {string} key - The key for the translation.
     * @returns {string} The translated string.
     * @throws Will throw an error if the key does not exist for the current locale.
     */
    translate(key) {
        const translations = this.languageResources[this.currentLocale];
        if (!translations || !translations[key]) {
            throw new Error(`Translation for key '${key}' not found in locale '${this.currentLocale}'.`);
        }
        return translations[key];
    }
}

// Usage example
try {
    const localeManager = new LocaleManager();
    
    // Change locale to Spanish
    localeManager.setLocale('es');
    console.log(localeManager.translate('greeting')); // Outputs: Hola

    // Change locale to French
    localeManager.setLocale('fr');
    console.log(localeManager.translate('farewell')); // Outputs: Au revoir

} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
