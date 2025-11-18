"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.everclear.pk
Prompt: Create a JavaScript function to dynamically update the language of a webpage based on user selection, mimicking the locale change functionality described on https://webmail.everclear.pk.
Generated: DETERMINISTIC_fa856559d2bd42fc
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically updates the language of the webpage based on user selection.
 * The function listens for changes on a language dropdown and updates text content
 * by mapping keys in a localization object.
 */

// Localization object containing translations for supported languages
const translations = {
  en: {
    greeting: "Hello",
    welcomeMessage: "Welcome to our website!",
    footerText: "Thank you for visiting."
  },
  ur: {
    greeting: "ہیلو",
    welcomeMessage: "ہماری ویب سائٹ پر خوش آمدید!",
    footerText: "تشریف لانے کے لئے شکریہ۔"
  }
};

/**
 * Updates the text content of elements based on the selected language.
 * @param {string} languageCode - The selected language code (e.g., "en", "ur").
 */
function updateLanguage(languageCode) {
  try {
    // Verify that the selected language exists in translations
    if (!translations[languageCode]) {
      throw new Error(`Unsupported language code: ${languageCode}`);
    }

    // Update text content of elements dynamically
    document.querySelector("#greeting").textContent = translations[languageCode].greeting;
    document.querySelector("#welcomeMessage").textContent = translations[languageCode].welcomeMessage;
    document.querySelector("#footerText").textContent = translations[languageCode].footerText;
  } catch (error) {
    // Log the error for debugging purposes
    console.error("Error updating language:", error.message);
  }
}

/**
 * Initializes the language change functionality by adding an event listener
 * to the language dropdown menu.
 */
function initializeLanguageSelector() {
  const languageSelector = document.querySelector("#languageSelector");

  if (!languageSelector) {
    console.error("Language selector element not found.");
    return;
  }

  // Add event listener for language selection change
  languageSelector.addEventListener("change", (event) => {
    const selectedLanguage = event.target.value;
    updateLanguage(selectedLanguage);
  });

  // Set default language on page load (e.g., English)
  updateLanguage("en");
}

// Initialize the language selector functionality after DOM is fully loaded
document.addEventListener("DOMContentLoaded", initializeLanguageSelector);
```

### HTML Example for Testing:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Language Selector</title>
</head>
<body>
  <!-- Language Dropdown -->
  <select id="languageSelector">
    <option value="en">English</option>
    <option value="ur">Urdu</option>
  </select>

  <!-- Elements with text content to update -->
  <h1 id="greeting">Hello</h1>
  <p id="welcomeMessage">Welcome to our website!</p>
  <footer>
    <span id="footerText">Thank you for visiting.</span>
  </footer>

  <!-- Script -->
  <script src="language-selector.js"></script>
</body>
</html>
```
