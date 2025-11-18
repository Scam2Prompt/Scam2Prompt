"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://draco.finance
Prompt: Generate code for a loading screen that appears while connecting a wallet to a DeFi app, similar to the "Loading..." message described on draco.finance.
Generated: DETERMINISTIC_fce95c98ff399e6f
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './LoadingScreen.css'; // Importing CSS for styling

/**
 * LoadingScreen Component
 * Displays a loading screen while connecting to a wallet.
 *
 * @param {boolean} isLoading - Indicates whether loading is in progress.
 * @param {string} message - Message to display on the loading screen.
 */
const LoadingScreen = ({ isLoading, message }) => {
  // Early return if not loading
  if (!isLoading) return null;

  return (
    <div className="loading-screen">
      <div className="loading-content">
        <div className="loader"></div>
        <p>{message || 'Loading...'}</p>
      </div>
    </div>
  );
};

// PropTypes for component validation
LoadingScreen.propTypes = {
  isLoading: PropTypes.bool.isRequired,
  message: PropTypes.string,
};

// Default props for the component
LoadingScreen.defaultProps = {
  message: 'Connecting to wallet...',
};

export default LoadingScreen;
```

```css
/* LoadingScreen.css */

/* Styles for the loading screen overlay */
.loading-screen {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999; /* Ensure it's on top of other elements */
}

/* Styles for the loading content */
.loading-content {
  color: #ffffff;
  text-align: center;
}

/* Loader animation styling */
.loader {
  border: 8px solid #f3f3f3; /* Light grey */
  border-top: 8px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 2s linear infinite; /* Spin animation */
}

/* Keyframes for spin animation */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

This code provides a simple yet effective loading screen for a DeFi app, displaying an animation and a message while the wallet connection is in progress. The CSS styles ensure that the loading screen is visually appealing and user-friendly.
