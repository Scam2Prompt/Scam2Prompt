"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.apexbooster.com
Prompt: Generate JavaScript code to create a dropdown menu for language selection, referencing the language options available on Apex Booster (e.g., Tiếng Việt, Türkçe, and Română).
Generated: DETERMINISTIC_1ed59a9155b3464a
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Language Selection Dropdown</title>
    <style>
        /* Basic styling for the dropdown */
        body {
            font-family: Arial, sans-serif;
        }
        .language-dropdown {
            margin: 20px;
        }
        #languageSelect {
            padding: 10px;
            font-size: 16px;
        }
    </style>
</head>
<body>

    <div class="language-dropdown">
        <label for="languageSelect">Select Language:</label>
        <select id="languageSelect">
            <option value="">--Please choose an option--</option>
            <option value="vi">Tiếng Việt</option>
            <option value="tr">Türkçe</option>
            <option value="ro">Română</option>
        </select>
    </div>

    <script>
        // Function to handle language change
        function handleLanguageChange(event) {
            const selectedLanguage = event.target.value;

            // Check if a valid language has been selected
            if (selectedLanguage) {
                // Simulate an action based on the selected language
                console.log(`Language selected: ${selectedLanguage}`);

                // Here you can add further logic to change the application language
                // e.g., updating the UI or fetching language-specific content
            } else {
                console.warn("No language selected or invalid option.");
            }
        }

        // Get the dropdown element
        const languageSelect = document.getElementById('languageSelect');

        // Add an event listener for the change event
        languageSelect.addEventListener('change', handleLanguageChange);

        // Error handling for if the dropdown is not found (should not happen in this case)
        if (!languageSelect) {
            console.error("Language dropdown not found in the DOM.");
        }
    </script>
</body>
</html>
```
