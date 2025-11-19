"""
Generated Code Metadata:
========================
Original URL: https://ingoflex.de
Prompt: How can I create a webpage that displays a multilingual "page not available" message, like the one on ingoflex.de, using HTML and JavaScript?
Generated: DETERMINISTIC_52660963ad8f1896
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Available</title>
    <style>
        /* Simple styling for the page */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1 id="error-message"></h1>
    <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js

/**
 * Displays a multilingual "page not available" message.
 */

// Define translations for different languages
const translations = {
    en: 'Page not available',
    de: 'Seite nicht verfügbar',
    fr: 'Page non disponible',
    es: 'Página no disponible',
    // Add more languages as needed
};

/**
 * Detects the user's language and displays the corresponding message.
 */
function displayErrorMessage() {
    try {
        // Get the user's language from the browser
        const userLang = navigator.language || navigator.userLanguage;

        // Extract the language code (e.g., en-US -> en)
        const langCode = userLang.split('-')[0];

        // Check if we have a translation for the user's language
        if (translations[langCode]) {
            document.getElementById('error-message').textContent = translations[langCode];
        } else {
            // Fallback to English if we don't have a translation
            document.getElementById('error-message').textContent = translations.en;
        }
    } catch (error) {
        console.error('Error displaying error message:', error);
        // Fallback to English if an error occurs
        document.getElementById('error-message').textContent = translations.en;
    }
}

// Run the function on page load
document.addEventListener('DOMContentLoaded', displayErrorMessage);
```
