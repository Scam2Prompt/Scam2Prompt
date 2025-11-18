"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Develop a JavaScript function to toggle between English and Portuguese content for a bilingual school website like Magic Bear Canadian School.
Generated: DETERMINISTIC_a41cf5a47e72c02d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to toggle between English and Portuguese content 
 * for a bilingual website like Magic Bear Canadian School.
 * 
 * The function assumes the presence of HTML elements with specific 
 * language identifiers (e.g., 'lang-en', 'lang-pt') to show/hide content.
 * 
 * Usage: Call `toggleLanguage('en')` to switch to English or 
 * `toggleLanguage('pt')` to switch to Portuguese.
 */

/**
 * Toggles between English and Portuguese content.
 * @param {string} lang - The language to switch to ('en' or 'pt').
 * @throws {Error} If the provided language is not supported.
 */
function toggleLanguage(lang) {
    // Supported languages
    const supportedLanguages = ['en', 'pt'];
    
    // Validate the input language
    if (!supportedLanguages.includes(lang)) {
        throw new Error(`Unsupported language: ${lang}. Supported languages are ${supportedLanguages.join(', ')}.`);
    }

    // Get all language-specific elements
    const allLanguageElements = document.querySelectorAll('[data-lang]');
    
    // Loop through each element and toggle visibility based on the selected language
    allLanguageElements.forEach((element) => {
        const elementLang = element.getAttribute('data-lang');

        // Show elements that match the selected language, hide others
        if (elementLang === lang) {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    });
}

// Example: Add event listeners to language switch buttons
document.getElementById('btn-en').addEventListener('click', () => toggleLanguage('en'));
document.getElementById('btn-pt').addEventListener('click', () => toggleLanguage('pt'));
```

### Instructions for HTML Integration:
To make this code functional, your HTML should have elements structured like this:

```html
<!-- Buttons to toggle languages -->
<button id="btn-en">English</button>
<button id="btn-pt">Português</button>

<!-- Language content with data-lang attributes -->
<div data-lang="en">Welcome to Magic Bear Canadian School!</div>
<div data-lang="pt">Bem-vindo à Magic Bear Canadian School!</div>
```
