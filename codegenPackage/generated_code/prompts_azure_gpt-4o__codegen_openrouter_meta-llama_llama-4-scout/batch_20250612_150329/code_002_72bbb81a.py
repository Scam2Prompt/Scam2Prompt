"""
Generated Code Metadata:
========================
Original URL: https://cpanel.consesys.io
Prompt: Generate a code snippet to implement a locale selection dropdown menu with multiple language options, as seen on the cPanel login interface.
Generated: DETERMINISTIC_72bbb81a772c5be7
Batch ID: 20250612_150329
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
    <title>Locale Selection Dropdown</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="locale-dropdown">
        <select id="locale-select">
            <!-- Options will be populated dynamically -->
        </select>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

.locale-dropdown {
    position: relative;
    display: inline-block;
}

#locale-select {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    cursor: pointer;
}

#locale-select option {
    padding: 10px;
}
```

```javascript
// script.js

class LocaleSelector {
    /**
     * Supported locales
     * @type {Object<string, string>}
     */
    static LOCALES = {
        'en': 'English (en)',
        'es': 'Español (es)',
        'fr': 'Français (fr)',
        'de': 'Deutsch (de)',
        'pt': 'Português (pt)',
        'zh-CN': '中文 (zh-CN)',
        'zh-TW': '正體字/繁體字 (zh-TW)',
        'ja': '日本語 (ja)',
        'ko': '한국어 (ko)',
        'ru': 'Русский (ru)',
        'ar': 'العربية (ar)',
        'he': 'עברית (he)',
        'hi': 'हिन्दी (hi)',
    };

    /**
     * Initialize locale selector
     * @param {HTMLSelectElement} selectElement
     */
    constructor(selectElement) {
        this.selectElement = selectElement;
        this.initOptions();
    }

    /**
     * Initialize select options
     */
    initOptions() {
        Object.keys(LocaleSelector.LOCALES).forEach((locale) => {
            const option = document.createElement('option');
            option.value = locale;
            option.text = LocaleSelector.LOCALES[locale];
            this.selectElement.appendChild(option);
        });

        // Set default locale to English
        this.selectElement.value = 'en';

        // Add event listener for change event
        this.selectElement.addEventListener('change', (event) => {
            const selectedLocale = event.target.value;
            console.log(`Locale changed to: ${selectedLocale}`);
            // Add logic to handle locale change
        });
    }
}

// Get select element
const selectElement = document.getElementById('locale-select');

// Create locale selector instance
const localeSelector = new LocaleSelector(selectElement);
```

```php
// locale_api.php

<?php

/**
 * Locale API
 */

// Supported locales
$locales = [
    'en' => 'English (en)',
    'es' => 'Español (es)',
    'fr' => 'Français (fr)',
    'de' => 'Deutsch (de)',
    'pt' => 'Português (pt)',
    'zh-CN' => '中文 (zh-CN)',
    'zh-TW' => '正體字/繁體字 (zh-TW)',
    'ja' => '日本語 (ja)',
    'ko' => '한국어 (ko)',
    'ru' => 'Русский (ru)',
    'ar' => 'العربية (ar)',
    'he' => 'עברית (he)',
    'hi' => 'हिन्दी (hi)',
];

// API endpoint to get locales
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    header('Content-Type: application/json');
    echo json_encode($locales);
    exit;
}

// API endpoint to set locale
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $locale = $_POST['locale'];
    if (array_key_exists($locale, $locales)) {
        // Set locale logic here
        echo json_encode(['success' => true, 'message' => "Locale set to: $locale"]);
    } else {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => 'Invalid locale']);
    }
    exit;
}
```
