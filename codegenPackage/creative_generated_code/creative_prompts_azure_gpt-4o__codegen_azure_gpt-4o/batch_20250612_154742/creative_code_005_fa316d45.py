"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status.ttec.smartteam.chat
Prompt: Create a React component that toggles the alert sound setting ("on/off") for the TTEC STC Cluster Status page and saves the user's preference locally.
Generated: DETERMINISTIC_fa316d454114f491
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from 'react';

const AlertSoundToggle = () => {
  // State to track the alert sound setting
  const [isSoundEnabled, setIsSoundEnabled] = useState(() => {
    // Initialize state from localStorage, default to true if not set
    const savedPreference = localStorage.getItem('alertSoundEnabled');
    return savedPreference === null ? true : savedPreference === 'true';
  });

  // Effect to save the user's preference to localStorage
  useEffect(() => {
    localStorage.setItem('alertSoundEnabled', isSoundEnabled);
  }, [isSoundEnabled]);

  // Handler to toggle the sound setting
  const handleToggle = () => {
    setIsSoundEnabled((prevState) => !prevState);
  };

  return (
    <div style={styles.container}>
      <label htmlFor="soundToggle" style={styles.label}>
        Alert Sound:
      </label>
      <button
        id="soundToggle"
        onClick={handleToggle}
        style={{
          ...styles.button,
          backgroundColor: isSoundEnabled ? 'green' : 'red',
        }}
      >
        {isSoundEnabled ? 'On' : 'Off'}
      </button>
    </div>
  );
};

// Inline styles for simplicity
const styles = {
  container: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: '10px',
    maxWidth: '300px',
    margin: '20px auto',
    border: '1px solid #ccc',
    borderRadius: '5px',
    backgroundColor: '#f9f9f9',
  },
  label: {
    marginRight: '10px',
    fontSize: '16px',
    fontWeight: 'bold',
  },
  button: {
    padding: '8px 16px',
    fontSize: '14px',
    fontWeight: 'bold',
    color: '#fff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
};

export default AlertSoundToggle;
```
