"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.consesys.io
Prompt: How can I implement a locale selection feature in a web application similar to the one used in Webmail?
Generated: DETERMINISTIC_2d6c447689d06d4c
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// localeSelector.js

// Import necessary libraries (assuming we're using React for this example)
import React, { useState, useEffect } from 'react';

// Supported locales
const SUPPORTED_LOCALES = {
    en: 'English',
    es: 'Español',
    fr: 'Français',
    de: 'Deutsch',
};

// Function to get the saved locale from localStorage or return the default locale
const getSavedLocale = () => {
    const savedLocale = localStorage.getItem('appLocale');
    return savedLocale ? savedLocale : 'en'; // Default to English
};

// LocaleSelector component
const LocaleSelector = () => {
    // State to store the current locale
    const [locale, setLocale] = useState(getSavedLocale());

    // Effect to update localStorage whenever locale changes
    useEffect(() => {
        localStorage.setItem('appLocale', locale);
        // Optionally, you can also re-render based on locale changes to show translated content
    }, [locale]);

    // Handler for locale change
    const handleLocaleChange = (event) => {
        const newLocale = event.target.value;
        if (SUPPORTED_LOCALES[newLocale]) {
            setLocale(newLocale);
        } else {
            console.error(`Unsupported locale selected: ${newLocale}`);
        }
    };

    return (
        <div>
            <label htmlFor="locale-select">Select Language:</label>
            <select id="locale-select" value={locale} onChange={handleLocaleChange}>
                {Object.keys(SUPPORTED_LOCALES).map((key) => (
                    <option key={key} value={key}>
                        {SUPPORTED_LOCALES[key]}
                    </option>
                ))}
            </select>
        </div>
    );
};

export default LocaleSelector;

// Usage in your main application file
// import LocaleSelector from './localeSelector';
// <LocaleSelector />
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Locale Selector Example</title>
</head>
<body>
    <div id="root"></div>
    <script src="path/to/your/bundled/javascript.js"></script>
</body>
</html>
```

```css
/* styles.css */
/* Add basic styles for the locale selector */
label {
    margin-right: 10px;
}

select {
    padding: 5px;
    font-size: 16px;
}
```

```json
// package.json
{
    "name": "locale-selector-example",
    "version": "1.0.0",
    "main": "index.js",
    "dependencies": {
        "react": "^17.0.2",
        "react-dom": "^17.0.2"
    },
    "scripts": {
        "start": "react-scripts start",
        "build": "react-scripts build"
    },
    "license": "MIT"
}
```

```bash
# To run this project, ensure you have Node.js and npm installed, then run:
npm install
npm start
```
