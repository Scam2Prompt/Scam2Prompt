"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inbetweener-blue.pages.dev
Prompt: Create a JavaScript function to handle multilingual support for a Shopify store, with a focus on brands like "$BLUE" by inBetweeners.
Generated: DETERMINISTIC_cf2191caa5fed677
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Multilingual support for a Shopify store.
 * This function handles the retrieval and display of language-specific strings.
 * 
 * @param {string} lang - The language code (e.g., 'en', 'fr', 'es').
 * @param {string} key - The key for the string to retrieve.
 * @returns {string} - The localized string or a fallback message if not found.
 */
function getLocalizedString(lang, key) {
    // Define a localization object with supported languages
    const localizationData = {
        en: {
            welcome: "Welcome to $BLUE by inBetweeners!",
            products: "Our Products",
            contact: "Contact Us"
        },
        fr: {
            welcome: "Bienvenue chez $BLUE par inBetweeners!",
            products: "Nos Produits",
            contact: "Contactez-nous"
        },
        es: {
            welcome: "¡Bienvenido a $BLUE de inBetweeners!",
            products: "Nuestros Productos",
            contact: "Contáctenos"
        }
    };

    // Check if the requested language is supported
    if (!localizationData[lang]) {
        console.error(`Language '${lang}' is not supported.`);
        lang = 'en'; // Fall back to English if the language is not supported
    }

    // Retrieve the localized string
    const localizedString = localizationData[lang][key];

    // Check if the requested key exists in the selected language
    if (!localizedString) {
        console.warn(`Key '${key}' not found for language '${lang}'. Falling back to default.`);
        return localizationData['en'][key] || "String not available."; // Fallback to English or a default message
    }

    return localizedString; // Return the localized string
}

// Usage example
document.addEventListener('DOMContentLoaded', () => {
    const userLang = navigator.language.slice(0, 2); // Get user's language (first two characters)
    const welcomeMessage = getLocalizedString(userLang, 'welcome');
    document.getElementById('welcome-message').innerText = welcomeMessage; // Set welcome message on the page
});
```
