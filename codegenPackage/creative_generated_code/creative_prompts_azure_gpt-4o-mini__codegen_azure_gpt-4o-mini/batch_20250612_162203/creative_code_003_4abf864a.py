"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Create a React component that allows users to customize their cookie consent preferences, reflecting the options available on the Masa website.
Generated: DETERMINISTIC_4abf864aa14f17a5
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// Define the available cookie preferences
const cookieOptions = [
  { id: 'essential', label: 'Essential Cookies', description: 'These cookies are necessary for the website to function.' },
  { id: 'analytics', label: 'Analytics Cookies', description: 'These cookies help us understand how users interact with our website.' },
  { id: 'advertising', label: 'Advertising Cookies', description: 'These cookies are used to deliver relevant ads to you.' },
];

// CookieConsentComponent allows users to customize their cookie consent preferences
const CookieConsentComponent = ({ onSave }) => {
  const [preferences, setPreferences] = useState({});

  // Load existing preferences from local storage
  useEffect(() => {
    const savedPreferences = JSON.parse(localStorage.getItem('cookieConsentPreferences')) || {};
    setPreferences(savedPreferences);
  }, []);

  // Handle checkbox change
  const handleChange = (id) => {
    setPreferences((prev) => ({
      ...prev,
      [id]: !prev[id],
    }));
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    try {
      localStorage.setItem('cookieConsentPreferences', JSON.stringify(preferences));
      onSave(preferences);
    } catch (error) {
      console.error('Error saving cookie preferences:', error);
    }
  };

  return (
    <div className="cookie-consent">
      <h2>Cookie Preferences</h2>
      <form onSubmit={handleSubmit}>
        {cookieOptions.map((option) => (
          <div key={option.id}>
            <label>
              <input
                type="checkbox"
                checked={preferences[option.id] || false}
                onChange={() => handleChange(option.id)}
              />
              <strong>{option.label}</strong>: {option.description}
            </label>
          </div>
        ))}
        <button type="submit">Save Preferences</button>
      </form>
    </div>
  );
};

// PropTypes for validation
CookieConsentComponent.propTypes = {
  onSave: PropTypes.func.isRequired,
};

export default CookieConsentComponent;
```
