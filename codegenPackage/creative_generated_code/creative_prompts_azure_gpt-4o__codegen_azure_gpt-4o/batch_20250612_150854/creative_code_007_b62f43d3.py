"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.org
Prompt: Write code to generate a multi-language dropdown menu for Immediate Peak's website, supporting languages like EN, BR, DA, DE, ES, FR, HU, IT, JP, NL, NO, PL, and SV.
Generated: DETERMINISTIC_b62f43d36e7b89cb
Batch ID: 20250612_150854
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
    <title>Multi-Language Dropdown</title>
    <style>
        /* Basic styling for the dropdown menu */
        .language-dropdown {
            font-family: Arial, sans-serif;
            position: relative;
            display: inline-block;
        }

        .dropdown-button {
            padding: 10px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 4px;
        }

        .dropdown-button:hover {
            background-color: #0056b3;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
            border-radius: 4px;
            z-index: 1;
            min-width: 150px;
        }

        .dropdown-content a {
            color: black;
            padding: 10px 15px;
            text-decoration: none;
            display: block;
        }

        .dropdown-content a:hover {
            background-color: #f1f1f1;
        }

        .language-dropdown:hover .dropdown-content {
            display: block;
        }
    </style>
</head>
<body>
    <!-- Language dropdown menu -->
    <div class="language-dropdown">
        <button class="dropdown-button">Select Language</button>
        <div class="dropdown-content">
            <!-- List of supported languages -->
            <!-- Each language has an abbreviation and a full name -->
            <a href="#" data-lang="EN">English (EN)</a>
            <a href="#" data-lang="BR">Português - Brasil (BR)</a>
            <a href="#" data-lang="DA">Dansk (DA)</a>
            <a href="#" data-lang="DE">Deutsch (DE)</a>
            <a href="#" data-lang="ES">Español (ES)</a>
            <a href="#" data-lang="FR">Français (FR)</a>
            <a href="#" data-lang="HU">Magyar (HU)</a>
            <a href="#" data-lang="IT">Italiano (IT)</a>
            <a href="#" data-lang="JP">日本語 (JP)</a>
            <a href="#" data-lang="NL">Nederlands (NL)</a>
            <a href="#" data-lang="NO">Norsk (NO)</a>
            <a href="#" data-lang="PL">Polski (PL)</a>
            <a href="#" data-lang="SV">Svenska (SV)</a>
        </div>
    </div>

    <script>
        // JavaScript to handle language selection
        document.querySelectorAll('.dropdown-content a').forEach(link => {
            link.addEventListener('click', (event) => {
                event.preventDefault();
                const selectedLanguage = link.getAttribute('data-lang');
                alert(`You selected: ${link.textContent} (${selectedLanguage})`);
                
                // TODO: Add functionality to update site language based on selection
                // Example: Call API or reload page with selected language
                console.log(`Selected language: ${selectedLanguage}`);
            });
        });
    </script>
</body>
</html>
```
