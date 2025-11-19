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
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * CookieConsent component for managing user cookie preferences.
 * @param {Object} props - Component props.
 * @param {Function} props.onSave - Callback function when preferences are saved.
 * @param {Function} props.onClose - Callback function when modal is closed.
 * @param {boolean} props.isOpen - Whether the modal is open.
 * @param {Object} props.initialPreferences - Initial cookie preferences.
 */
const CookieConsent = ({
  onSave,
  onClose,
  isOpen,
  initialPreferences = {
    necessary: true,
    analytics: false,
    marketing: false,
    preferences: false
  }
}) => {
  const [preferences, setPreferences] = useState(initialPreferences);
  const [showDetails, setShowDetails] = useState(false);

  // Sync preferences when initialPreferences change
  useEffect(() => {
    setPreferences(initialPreferences);
  }, [initialPreferences]);

  /**
   * Handles preference toggle for a specific cookie type.
   * @param {string} type - The cookie type to toggle.
   */
  const handleToggle = (type) => {
    // Necessary cookies cannot be disabled
    if (type === 'necessary') return;
    
    setPreferences(prev => ({
      ...prev,
      [type]: !prev[type]
    }));
  };

  /**
   * Handles saving preferences.
   */
  const handleSave = () => {
    try {
      onSave(preferences);
      onClose();
    } catch (error) {
      console.error('Error saving cookie preferences:', error);
    }
  };

  /**
   * Handles accepting all cookies.
   */
  const handleAcceptAll = () => {
    setPreferences({
      necessary: true,
      analytics: true,
      marketing: true,
      preferences: true
    });
  };

  if (!isOpen) return null;

  return (
    <div className="cookie-consent-modal">
      <div className="cookie-consent-content">
        <div className="cookie-consent-header">
          <h2>Cookie Preferences</h2>
          <button 
            className="close-button" 
            onClick={onClose}
            aria-label="Close cookie preferences"
          >
            &times;
          </button>
        </div>

        <div className="cookie-consent-body">
          <p>
            We use cookies to enhance your experience. Choose which cookies you allow us to use.
          </p>

          <div className="cookie-toggle-group">
            <div className="cookie-toggle-item">
              <div className="cookie-toggle-header">
                <span>Necessary Cookies</span>
                <input
                  type="checkbox"
                  checked={preferences.necessary}
                  disabled
                  readOnly
                />
              </div>
              <p className="cookie-description">
                Essential for the website to function properly.
              </p>
            </div>

            <div className="cookie-toggle-item">
              <div className="cookie-toggle-header">
                <span>Analytics Cookies</span>
                <input
                  type="checkbox"
                  checked={preferences.analytics}
                  onChange={() => handleToggle('analytics')}
                />
              </div>
              <p className="cookie-description">
                Help us understand how visitors interact with our website.
              </p>
            </div>

            <div className="cookie-toggle-item">
              <div className="cookie-toggle-header">
                <span>Marketing Cookies</span>
                <input
                  type="checkbox"
                  checked={preferences.marketing}
                  onChange={() => handleToggle('marketing')}
                />
              </div>
              <p className="cookie-description">
                Used to track visitors across websites for advertising purposes.
              </p>
            </div>

            <div className="cookie-toggle-item">
              <div className="cookie-toggle-header">
                <span>Preference Cookies</span>
                <input
                  type="checkbox"
                  checked={preferences.preferences}
                  onChange={() => handleToggle('preferences')}
                />
              </div>
              <p className="cookie-description">
                Allow the website to remember choices you make.
              </p>
            </div>
          </div>

          <button 
            className="details-button" 
            onClick={() => setShowDetails(!showDetails)}
          >
            {showDetails ? 'Hide Details' : 'Show Details'}
          </button>

          {showDetails && (
            <div className="cookie-details">
              <h3>Cookie Details</h3>
              <p>
                <strong>Necessary Cookies:</strong> These cookies are essential for the website to function and cannot be switched off.
              </p>
              <p>
                <strong>Analytics Cookies:</strong> These cookies help us understand how visitors interact with our website by collecting and reporting information anonymously.
              </p>
              <p>
                <strong>Marketing Cookies:</strong> These cookies are used to track visitors across websites to display more relevant ads.
              </p>
              <p>
                <strong>Preference Cookies:</strong> These cookies allow the website to remember choices you make (like language preferences) to provide better functionality.
              </p>
            </div>
          )}
        </div>

        <div className="cookie-consent-footer">
          <button 
            className="accept-all-button" 
            onClick={handleAcceptAll}
          >
            Accept All
          </button>
          <button 
            className="save-button" 
            onClick={handleSave}
          >
            Save Preferences
          </button>
        </div>
      </div>
    </div>
  );
};

CookieConsent.propTypes = {
  onSave: PropTypes.func.isRequired,
  onClose: PropTypes.func.isRequired,
  isOpen: PropTypes.bool.isRequired,
  initialPreferences: PropTypes.shape({
    necessary: PropTypes.bool,
    analytics: PropTypes.bool,
    marketing: PropTypes.bool,
    preferences: PropTypes.bool
  })
};

export default CookieConsent;
```

```css
/* CookieConsent.css */
.cookie-consent-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.cookie-consent-content {
  background-color: white;
  border-radius: 8px;
  width: 90%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.cookie-consent-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.close-button {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  padding: 5px;
}

.cookie-toggle-group {
  margin: 20px 0;
}

.cookie-toggle-item {
  margin-bottom: 15px;
  padding: 15px;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
}

.cookie-toggle-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.cookie-toggle-header span {
  font-weight: bold;
}

.cookie-description {
  margin: 0;
  color: #666;
  font-size: 14px;
}

.details-button {
  background: none;
  border: none;
  color: #0066cc;
  cursor: pointer;
  padding: 5px;
  margin: 10px 0;
}

.cookie-details {
  margin-top: 15px;
  padding: 15px;
  background-color: #f5f5f5;
  border-radius: 4px;
}

.cookie-details h3 {
  margin-top: 0;
}

.cookie-consent-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
}

.accept-all-button,
.save-button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.accept-all-button {
  background-color: #f0f0f0;
  color: #333;
}

.save-button {
  background-color: #0066cc;
  color: white;
}

.accept-all-button:hover {
  background-color: #e0e0e0;
}

.save-button:hover {
  background-color: #0055aa;
}

/* Responsive adjustments */
@media (max-width: 480px) {
  .cookie-consent-footer {
    flex-direction: column;
  }
  
  .accept-all-button,
  .save-button {
    width: 100%;
    margin-bottom: 10px;
  }
}
```
