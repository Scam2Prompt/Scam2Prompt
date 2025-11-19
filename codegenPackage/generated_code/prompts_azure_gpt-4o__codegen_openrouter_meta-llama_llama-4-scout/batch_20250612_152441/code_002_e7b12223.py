"""
Generated Code Metadata:
========================
Original URL: https://webmail.dexodoor.com
Prompt: Generate code to implement a multilingual locale selector for a webmail login page, supporting languages like Arabic, Japanese, and Russian, as described on the Dexodoor Webmail site.
Generated: DETERMINISTIC_e7b12223c0139fc6
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// locale-selector.js

/**
 * LocaleSelector class for handling multilingual locale selection.
 */
class LocaleSelector {
  /**
   * Supported locales.
   * @type {Object<string, string>}
   */
  static SUPPORTED_LOCALES = {
    'ar': 'Arabic',
    'ja': 'Japanese',
    'ru': 'Russian',
    'en': 'English', // default locale
  };

  /**
   * Constructor.
   * @param {Document} document - The document object.
   */
  constructor(document) {
    this.document = document;
    this.localeElement = null;
    this.locale = this.getInitialLocale();
  }

  /**
   * Initialize the locale selector.
   */
  init() {
    this.localeElement = this.document.getElementById('locale-selector');
    if (this.localeElement) {
      this.renderLocaleOptions();
      this.localeElement.addEventListener('change', this.handleLocaleChange.bind(this));
    }
  }

  /**
   * Get the initial locale from the browser's language settings or a stored value.
   * @returns {string} The initial locale.
   */
  getInitialLocale() {
    const storedLocale = localStorage.getItem('locale');
    if (storedLocale && LocaleSelector.SUPPORTED_LOCALES[storedLocale]) {
      return storedLocale;
    }
    const browserLang = navigator.language || navigator.userLanguage;
    const langCode = browserLang.substring(0, 2);
    return LocaleSelector.SUPPORTED_LOCALES[langCode] ? langCode : 'en';
  }

  /**
   * Render locale options in the selector element.
   */
  renderLocaleOptions() {
    Object.keys(LocaleSelector.SUPPORTED_LOCALES).forEach((locale) => {
      const option = this.document.createElement('option');
      option.value = locale;
      option.textContent = LocaleSelector.SUPPORTED_LOCALES[locale];
      option.selected = locale === this.locale;
      this.localeElement.appendChild(option);
    });
  }

  /**
   * Handle locale change event.
   * @param {Event} event - The change event.
   */
  handleLocaleChange(event) {
    const newLocale = event.target.value;
    this.locale = newLocale;
    localStorage.setItem('locale', newLocale);
    this.updatePageLocale();
  }

  /**
   * Update the page locale.
   */
  updatePageLocale() {
    // Update date and number formats according to the locale
    // For example, using the Intl API:
    const date = new Date();
    const formattedDate = new Intl.DateTimeFormat(this.locale).format(date);
    this.document.getElementById('current-date').textContent = formattedDate;

    // Update translations
    this.document.querySelectorAll('[data-translate]').forEach((element) => {
      const translationKey = element.getAttribute('data-translate');
      const translation = this.getTranslation(translationKey, this.locale);
      element.textContent = translation;
    });
  }

  /**
   * Get a translation for a given key and locale.
   * @param {string} key - The translation key.
   * @param {string} locale - The locale.
   * @returns {string} The translation.
   */
  getTranslation(key, locale) {
    // Implement your translation fetching logic here
    // For example, using a translation API or a JSON file:
    const translations = {
      'en': {
        'login': 'Login',
        'password': 'Password',
      },
      'ar': {
        'login': 'تسجيل الدخول',
        'password': 'كلمة المرور',
      },
      'ja': {
        'login': 'ログイン',
        'password': 'パスワード',
      },
      'ru': {
        'login': 'Войти',
        'password': 'Пароль',
      },
    };
    return translations[locale] && translations[locale][key] ? translations[locale][key] : '';
  }
}

// Initialize the locale selector
document.addEventListener('DOMContentLoaded', () => {
  const localeSelector = new LocaleSelector(document);
  localeSelector.init();
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Webmail Login</title>
  <style>
    /* Add some basic styling */
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <select id="locale-selector"></select>
  <form>
    <label for="login">Login:</label>
    <input type="text" id="login" data-translate="login"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" data-translate="password"><br><br>
    <input type="submit" value="Submit">
  </form>
  <p id="current-date"></p>

  <script src="locale-selector.js"></script>
</body>
</html>
```
