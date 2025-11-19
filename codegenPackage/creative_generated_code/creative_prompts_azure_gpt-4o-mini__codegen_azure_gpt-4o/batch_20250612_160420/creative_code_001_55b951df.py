"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.zkasino.it
Prompt: Recommend an API for implementing a multilingual support feature in a web application, inspired by the language options on zkasino.it.
Generated: DETERMINISTIC_55b951dfbd6e1bd2
Batch ID: 20250612_160420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code demonstrating the implementation of multilingual support using the `i18next` library, which is a widely-used API for internationalization in web applications.

### Prerequisites:
Before running the code, ensure `i18next` and `i18next-http-backend` are installed via npm:
```bash
npm install i18next i18next-http-backend
```

### Code:
```javascript
// Import necessary modules
import i18next from 'i18next';
import Backend from 'i18next-http-backend';
import { initReactI18next } from 'react-i18next';

// Initialize i18next for multilingual support
i18next
  .use(Backend) // Use HTTP backend to load translation files
  .use(initReactI18next) // Integrate with React for easy usage
  .init({
    lng: 'en', // Default language
    fallbackLng: 'en', // Fallback language if translation is missing
    debug: true, // Enable debug mode for logging (disable in production)
    backend: {
      loadPath: '/locales/{{lng}}/{{ns}}.json', // Path to load translation files
    },
    interpolation: {
      escapeValue: false, // React already escapes values to prevent XSS
    },
    keySeparator: false, // Allow nested keys in translation files
    supportedLngs: ['en', 'it', 'fr', 'de'], // Supported languages
  });

// Example usage: React component for language switching
import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';

const LanguageSwitcher = () => {
  const { t, i18n } = useTranslation(); // Translate function and i18n instance
  const [language, setLanguage] = useState(i18n.language); // Current language state

  // Function to change language
  const changeLanguage = (lng) => {
    try {
      i18n.changeLanguage(lng); // Change the language using i18next
      setLanguage(lng); // Update local state
    } catch (error) {
      console.error('Error changing language:', error); // Error handling
    }
  };

  return (
    <div>
      <h1>{t('welcome_message')}</h1> {/* Example translation */}
      <div>
        <button onClick={() => changeLanguage('en')}>English</button>
        <button onClick={() => changeLanguage('it')}>Italian</button>
        <button onClick={() => changeLanguage('fr')}>French</button>
        <button onClick={() => changeLanguage('de')}>German</button>
      </div>
      <p>
        Current Language: <strong>{language}</strong>
      </p>
    </div>
  );
};

export default LanguageSwitcher;

// Example translation file structure:
// /locales/en/translation.json
// {
//   "welcome_message": "Welcome to our website!"
// }

// /locales/it/translation.json
// {
//   "welcome_message": "Benvenuto nel nostro sito web!"
// }

// /locales/fr/translation.json
// {
//   "welcome_message": "Bienvenue sur notre site Web!"
// }

// /locales/de/translation.json
// {
//   "welcome_message": "Willkommen auf unserer Website!"
// }
```

This code assumes you're using React for your web application. For non-React projects, you can skip the `initReactI18next` plugin and directly use `i18next` methods to fetch translations.
