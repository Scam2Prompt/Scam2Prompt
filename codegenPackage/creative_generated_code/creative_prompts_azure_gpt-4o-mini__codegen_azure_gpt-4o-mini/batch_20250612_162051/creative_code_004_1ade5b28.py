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
// Importing the necessary library for language switching
import i18next from 'i18next';
import i18nextBrowserLanguageDetector from 'i18next-browser-languagedetector';
import i18nextXHRBackend from 'i18next-xhr-backend';

// Initialize i18next library
i18next
  .use(i18nextBrowserLanguageDetector) // Detect user's language
  .use(i18nextXHRBackend) // Use XHR backend for loading translations
  .init({
    fallbackLng: 'en', // Default language if detected language is not available
    debug: true, // Enable debug mode for development

    // Define the backend options for loading translation files
    backend: {
      loadPath: '/locales/{{lng}}/{{ns}}.json', // Path to translation files
    },

    // Define supported languages
    supportedLngs: ['en', 'es'], // English and Spanish
    interpolation: {
      escapeValue: false, // React already does escaping
    },
  })
  .then(() => {
    // Initialization successful, update UI with the default language
    updateContent();
  })
  .catch((error) => {
    console.error('Error initializing i18next:', error); // Error handling
  });

// Function to update UI content based on the current language
function updateContent() {
  document.getElementById('content').innerHTML = i18next.t('welcome_message'); // Update content
}

// Function to switch languages
function switchLanguage(language) {
  i18next.changeLanguage(language) // Change the language
    .then(() => {
      updateContent(); // Update content after language change
    })
    .catch((error) => {
      console.error('Error changing language:', error); // Error handling
    });
}

// Event listeners for language buttons
document.getElementById('btn-en').addEventListener('click', () => switchLanguage('en'));
document.getElementById('btn-es').addEventListener('click', () => switchLanguage('es'));

// Initial content load
updateContent();
```

**Note:** Ensure you have the translation files structured correctly in the `/locales` directory, following the naming convention used in the `loadPath` option.
