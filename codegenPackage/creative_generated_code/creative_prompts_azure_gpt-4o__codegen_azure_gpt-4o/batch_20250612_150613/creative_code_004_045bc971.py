"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.com
Prompt: Write a function in JavaScript to toggle between English and Russian language options on a web page, similar to the language selection feature on HELPGM.
Generated: DETERMINISTIC_045bc9712587760a
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to toggle between English and Russian languages on a web page
function toggleLanguage() {
    // Get the current language setting from localStorage (persistent across sessions)
    let currentLanguage = localStorage.getItem('language') || 'en'; // Default to English ('en') if not set

    // Determine the new language to switch to
    let newLanguage = currentLanguage === 'en' ? 'ru' : 'en';

    // Update the language in localStorage
    localStorage.setItem('language', newLanguage);

    // Update the text content on the page based on the selected language
    updatePageLanguage(newLanguage);
}

// Function to update the page content based on the selected language
function updatePageLanguage(language) {
    // Define translations for English ('en') and Russian ('ru')
    const translations = {
        en: {
            greeting: 'Hello',
            description: 'Welcome to our website!',
            buttonText: 'Switch to Russian'
        },
        ru: {
            greeting: 'Привет',
            description: 'Добро пожаловать на наш сайт!',
            buttonText: 'Переключиться на английский'
        }
    };

    // Get the translation object for the selected language
    const selectedTranslations = translations[language];

    // Safely update text elements on the page (using IDs as an example)
    try {
        // Update the greeting text
        document.getElementById('greeting').textContent = selectedTranslations.greeting;

        // Update the description text
        document.getElementById('description').textContent = selectedTranslations.description;

        // Update the button text
        document.getElementById('toggleButton').textContent = selectedTranslations.buttonText;
    } catch (error) {
        console.error('Error updating page language:', error);
    }
}

// Event listener to toggle language when the button is clicked
document.getElementById('toggleButton').addEventListener('click', toggleLanguage);

// Initialize the page with the preferred language on load
document.addEventListener('DOMContentLoaded', () => {
    const savedLanguage = localStorage.getItem('language') || 'en'; // Load saved language or default to English
    updatePageLanguage(savedLanguage);
});
```

This code assumes the existence of specific HTML elements with IDs `greeting`, `description`, and `toggleButton`. Below is a minimal example of the HTML structure this code would work with:

```html
<div>
    <h1 id="greeting"></h1>
    <p id="description"></p>
    <button id="toggleButton"></button>
</div>
```
