"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.arbitrium.adv.br
Prompt: Generate a script in JavaScript to dynamically change the language of a cPanel login page based on user selection.
Generated: DETERMINISTIC_036a6c7ba6123e6a
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// cPanel Language Selector Script
// This script dynamically changes the language of the cPanel login page based on user selection

// Wrap the code in an IIFE to avoid polluting the global namespace
(function () {
    // List of available languages and their corresponding cPanel language codes
    const languages = {
        English: "en",
        Spanish: "es",
        French: "fr",
        German: "de",
        Chinese: "zh",
        Japanese: "ja"
    };

    // Create a dropdown for language selection
    const languageSelector = document.createElement("select");
    languageSelector.id = "languageSelector";

    // Populate the dropdown with language options
    for (const [language, code] of Object.entries(languages)) {
        const option = document.createElement("option");
        option.value = code;
        option.textContent = language;
        languageSelector.appendChild(option);
    }

    // Style the dropdown for better appearance (optional)
    languageSelector.style.position = "absolute";
    languageSelector.style.top = "20px";
    languageSelector.style.right = "20px";
    languageSelector.style.padding = "5px";

    // Append the dropdown to the body of the page
    document.body.appendChild(languageSelector);

    // Function to change the page language based on selection
    const changeLanguage = (languageCode) => {
        try {
            // Update the 'locale' query parameter to the selected language
            const url = new URL(window.location.href); // Get the current URL
            url.searchParams.set("locale", languageCode); // Set the 'locale' parameter
            window.location.href = url.toString(); // Redirect to the updated URL
        } catch (error) {
            // Log any errors to the console
            console.error("Error changing language:", error);
        }
    };

    // Event listener for language selection change
    languageSelector.addEventListener("change", (event) => {
        const selectedLanguageCode = event.target.value; // Get the selected language code
        changeLanguage(selectedLanguageCode); // Call the function to update the language
    });

    // Set the dropdown to match the current language on page load
    window.addEventListener("load", () => {
        try {
            const url = new URL(window.location.href);
            const currentLanguage = url.searchParams.get("locale") || "en"; // Default to English
            languageSelector.value = currentLanguage; // Set the dropdown to the current language
        } catch (error) {
            console.error("Error initializing language selector:", error);
        }
    });
})();
```
