"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-crypto.yivesites.com
Prompt: Generate a JavaScript function to enable users to toggle between languages (Bahasa Indonesia and English) on the APELBET website.
Generated: DETERMINISTIC_6d1145d25c3f03f6
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Language toggle function for the APELBET website
// This function allows users to switch between Bahasa Indonesia and English

// An object to hold the translations for each language
const translations = {
    en: {
        welcome: "Welcome to APELBET",
        instructions: "Please select your preferred language."
    },
    id: {
        welcome: "Selamat datang di APELBET",
        instructions: "Silakan pilih bahasa yang Anda inginkan."
    }
};

// Function to set the language on the webpage
function setLanguage(lang) {
    // Check if the language is valid
    if (!translations[lang]) {
        console.error(`Language "${lang}" is not supported.`);
        return;
    }

    // Update the text content based on the selected language
    document.getElementById("welcome-message").textContent = translations[lang].welcome;
    document.getElementById("instructions-message").textContent = translations[lang].instructions;

    // Optionally, store the user's language preference in localStorage
    localStorage.setItem("preferredLanguage", lang);
}

// Function to toggle languages on user action
function toggleLanguage() {
    // Retrieve the current language from localStorage, defaulting to English
    const currentLang = localStorage.getItem("preferredLanguage") || 'en';
    
    // Determine the new language
    const newLang = currentLang === 'en' ? 'id' : 'en';
    
    // Set the new language
    setLanguage(newLang);
}

// Event listener for the language toggle button
document.getElementById("language-toggle-button").addEventListener("click", toggleLanguage);

// Initial setup: load the preferred language on page load
document.addEventListener("DOMContentLoaded", () => {
    const preferredLanguage = localStorage.getItem("preferredLanguage") || 'en';
    setLanguage(preferredLanguage);
});
```

```html
<!-- HTML Structure for the language toggle feature -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>APELBET Language Toggle</title>
</head>
<body>
    <div>
        <h1 id="welcome-message"></h1>
        <p id="instructions-message"></p>
        <button id="language-toggle-button">Toggle Language</button>
    </div>
    <script src="path/to/your/script.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
