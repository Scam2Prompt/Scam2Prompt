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

```jsx
// Import necessary libraries and components
import React, { useState } from 'react';

// Define CookieConsent component
const CookieConsent = () => {
  // State to manage cookie preferences
  const [preferences, setPreferences] = useState({
    necessary: true, // Necessary cookies are always enabled
    analytics: false,
    marketing: false,
    personalization: false,
  });

  // State to show/hide the consent modal
  const [showModal, setShowModal] = useState(true);

  // Handle changes in preferences
  const handlePreferenceChange = (key, value) => {
    setPreferences((prev) => ({
      ...prev,
      [key]: value,
    }));
  };

  // Handle saving preferences
  const handleSavePreferences = () => {
    try {
      // Save preferences to localStorage or a backend API
      localStorage.setItem('cookiePreferences', JSON.stringify(preferences));
      // Hide the modal after saving
      setShowModal(false);
    } catch (error) {
      console.error('Error saving cookie preferences:', error);
    }
  };

  // Handle rejecting all cookies except necessary
  const handleRejectAll = () => {
    setPreferences({
      necessary: true,
      analytics: false,
      marketing: false,
      personalization: false,
    });
    handleSavePreferences();
  };

  // Render the cookie consent modal
  return (
    showModal && (
      <div style={styles.modal}>
        <h2>Cookie Preferences</h2>
        <p>
          We use cookies to improve your experience. Please customize your preferences below.
        </p>
        <div style={styles.checkboxContainer}>
          {/* Necessary cookies (always enabled) */}
          <label style={styles.checkboxLabel}>
            <input type="checkbox" checked={preferences.necessary} disabled />
            Necessary (always enabled)
          </label>

          {/* Analytics cookies */}
          <label style={styles.checkboxLabel}>
            <input
              type="checkbox"
              checked={preferences.analytics}
              onChange={(e) => handlePreferenceChange('analytics', e.target.checked)}
            />
            Analytics
          </label>

          {/* Marketing cookies */}
          <label style={styles.checkboxLabel}>
            <input
              type="checkbox"
              checked={preferences.marketing}
              onChange={(e) => handlePreferenceChange('marketing', e.target.checked)}
            />
            Marketing
          </label>

          {/* Personalization cookies */}
          <label style={styles.checkboxLabel}>
            <input
              type="checkbox"
              checked={preferences.personalization}
              onChange={(e) => handlePreferenceChange('personalization', e.target.checked)}
            />
            Personalization
          </label>
        </div>
        {/* Buttons to save or reject preferences */}
        <div style={styles.buttonContainer}>
          <button style={styles.button} onClick={handleSavePreferences}>
            Save Preferences
          </button>
          <button style={styles.button} onClick={handleRejectAll}>
            Reject All
          </button>
        </div>
      </div>
    )
  );
};

// Inline styles for the modal and elements (can be replaced with CSS/SASS)
const styles = {
  modal: {
    position: 'fixed',
    top: '20%',
    left: '50%',
    transform: 'translate(-50%, -20%)',
    backgroundColor: '#fff',
    padding: '20px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
    borderRadius: '8px',
    zIndex: 1000,
    width: '400px',
  },
  checkboxContainer: {
    marginTop: '20px',
  },
  checkboxLabel: {
    display: 'block',
    marginBottom: '10px',
  },
  buttonContainer: {
    marginTop: '20px',
    textAlign: 'right',
  },
  button: {
    marginLeft: '10px',
    padding: '10px 15px',
    backgroundColor: '#007BFF',
    color: '#fff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
};

// Export the component
export default CookieConsent;
```
