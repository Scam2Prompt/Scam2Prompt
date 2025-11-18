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
 * Toggles the content language of the webpage between English and Portuguese.
 * This function updates the text content of specified elements based on the selected language.
 * 
 * @param {string} lang - The target language to switch to ('en' for English, 'pt' for Portuguese).
 */
function toggleLanguage(lang) {
    // Validate the input language
    if (lang !== 'en' && lang !== 'pt') {
        console.error('Invalid language code. Use "en" for English or "pt" for Portuguese.');
        return;
    }

    // Define content for both languages
    const content = {
        en: {
            welcome: "Welcome to Magic Bear Canadian School!",
            description: "We provide bilingual education in a nurturing environment.",
            contact: "Contact us for more information."
        },
        pt: {
            welcome: "Bem-vindo à Magic Bear Canadian School!",
            description: "Oferecemos educação bilíngue em um ambiente acolhedor.",
            contact: "Entre em contato conosco para mais informações."
        }
    };

    // Update the content on the page
    try {
        document.getElementById('welcome').textContent = content[lang].welcome;
        document.getElementById('description').textContent = content[lang].description;
        document.getElementById('contact').textContent = content[lang].contact;
    } catch (error) {
        console.error('Error updating content:', error);
    }
}

// Example usage: Toggle to Portuguese
// toggleLanguage('pt');

// Example usage: Toggle to English
// toggleLanguage('en');
```

This code is ready to be integrated into a bilingual school website. Make sure to have elements with `id="welcome"`, `id="description"`, and `id="contact"` in your HTML for the text updates to reflect.
