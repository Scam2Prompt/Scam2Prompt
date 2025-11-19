"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: Create a React component that allows users to customize their cookie consent preferences, reflecting the options available on the Masa website.
Generated: DETERMINISTIC_4abf864aa14f17a5
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// CookieConsent.js
import React, { useState } from 'react';

/**
 * Cookie Consent Component
 * 
 * Allows users to customize their cookie consent preferences.
 */
const CookieConsent = () => {
  // Define available cookie categories
  const [cookieCategories, setCookieCategories] = useState({
    essential: true, // Essential cookies are always enabled
    analytics: false,
    advertising: false,
    socialMedia: false,
  });

  // Handle changes to cookie category preferences
  const handleChange = (category) => {
    setCookieCategories((prevCategories) => ({
      ...prevCategories,
      [category]: !prevCategories[category],
    }));
  };

  // Save user's cookie preferences
  const savePreferences = () => {
    try {
      // Implement logic to save user's preferences (e.g., to local storage or API)
      localStorage.setItem('cookiePreferences', JSON.stringify(cookieCategories));
      console.log('Cookie preferences saved:', cookieCategories);
    } catch (error) {
      console.error('Error saving cookie preferences:', error);
    }
  };

  return (
    <div className="cookie-consent">
      <h2>Cookie Consent</h2>
      <p>Customize your cookie preferences:</p>
      <ul>
        <li>
          <label>
            <input
              type="checkbox"
              checked={cookieCategories.essential}
              disabled // Essential cookies are always enabled
            />
            Essential Cookies
            <span className="description">Necessary for the website to function properly.</span>
          </label>
        </li>
        <li>
          <label>
            <input
              type="checkbox"
              checked={cookieCategories.analytics}
              onChange={() => handleChange('analytics')}
            />
            Analytics Cookies
            <span className="description">Help us improve the website with anonymous usage data.</span>
          </label>
        </li>
        <li>
          <label>
            <input
              type="checkbox"
              checked={cookieCategories.advertising}
              onChange={() => handleChange('advertising')}
            />
            Advertising Cookies
            <span className="description">Allow targeted advertising based on your interests.</span>
          </label>
        </li>
        <li>
          <label>
            <input
              type="checkbox"
              checked={cookieCategories.socialMedia}
              onChange={() => handleChange('socialMedia')}
            />
            Social Media Cookies
            <span className="description">Enable sharing and social media tracking.</span>
          </label>
        </li>
      </ul>
      <button onClick={savePreferences}>Save Preferences</button>
    </div>
  );
};

export default CookieConsent;
```

```css
/* CookieConsent.css */
.cookie-consent {
  max-width: 400px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.cookie-consent ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.cookie-consent li {
  margin-bottom: 20px;
}

.cookie-consent label {
  display: block;
  cursor: pointer;
}

.cookie-consent input[type="checkbox"] {
  margin-right: 10px;
}

.cookie-consent .description {
  display: block;
  font-size: 14px;
  color: #666;
}

.cookie-consent button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.cookie-consent button:hover {
  background-color: #3e8e41;
}
```
