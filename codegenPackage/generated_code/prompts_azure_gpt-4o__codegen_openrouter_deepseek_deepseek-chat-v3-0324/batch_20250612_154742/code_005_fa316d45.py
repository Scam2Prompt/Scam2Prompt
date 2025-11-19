"""
Generated Code Metadata:
========================
Original URL: https://status.ttec.smartteam.chat
Prompt: Create a React component that toggles the alert sound setting ("on/off") for the TTEC STC Cluster Status page and saves the user's preference locally.
Generated: DETERMINISTIC_fa316d454114f491
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';

/**
 * AlertSoundToggle component for toggling alert sound setting on/off.
 * Saves user preference to localStorage.
 */
const AlertSoundToggle = () => {
  const [isSoundOn, setIsSoundOn] = useState(() => {
    // Initialize state from localStorage if available, default to true
    try {
      const savedPreference = localStorage.getItem('ttcStcAlertSound');
      return savedPreference ? JSON.parse(savedPreference) : true;
    } catch (error) {
      console.error('Error reading sound preference from localStorage:', error);
      return true;
    }
  });

  // Save preference to localStorage whenever it changes
  useEffect(() => {
    try {
      localStorage.setItem('ttcStcAlertSound', JSON.stringify(isSoundOn));
    } catch (error) {
      console.error('Error saving sound preference to localStorage:', error);
    }
  }, [isSoundOn]);

  const handleToggle = () => {
    setIsSoundOn(prev => !prev);
  };

  return (
    <div className="alert-sound-toggle">
      <label htmlFor="sound-toggle" className="toggle-label">
        Alert Sound:
      </label>
      <button
        id="sound-toggle"
        onClick={handleToggle}
        className={`toggle-button ${isSoundOn ? 'on' : 'off'}`}
        aria-label={isSoundOn ? 'Alert sound on' : 'Alert sound off'}
      >
        {isSoundOn ? 'ON' : 'OFF'}
      </button>
    </div>
  );
};

export default AlertSoundToggle;
```
