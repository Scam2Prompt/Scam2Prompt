"""
Generated Code Metadata:
========================
Original URL: https://draco.finance
Prompt: Generate code for a loading screen that appears while connecting a wallet to a DeFi app, similar to the "Loading..." message described on draco.finance.
Generated: DETERMINISTIC_fce95c98ff399e6f
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './LoadingScreen.css'; // Importing CSS for styling

/**
 * LoadingScreen component displays a loading message while connecting a wallet.
 * 
 * @param {boolean} isLoading - Indicates whether the loading screen should be displayed.
 * @param {string} message - Custom message to display during loading.
 */
const LoadingScreen = ({ isLoading, message }) => {
    // State to manage the visibility of the loading screen
    const [visible, setVisible] = useState(isLoading);

    useEffect(() => {
        // Update visibility based on isLoading prop
        setVisible(isLoading);
    }, [isLoading]);

    // If not loading, return null to render nothing
    if (!visible) return null;

    return (
        <div className="loading-screen">
            <div className="loading-content">
                <div className="spinner"></div>
                <p>{message || 'Loading...'}</p>
            </div>
        </div>
    );
};

// PropTypes for type checking
LoadingScreen.propTypes = {
    isLoading: PropTypes.bool.isRequired,
    message: PropTypes.string,
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
    z-index: 9999; /* Ensure it appears above other content */
}

/* Styles for the loading content */
.loading-content {
    text-align: center;
    color: white;
}

/* Spinner animation */
.spinner {
    border: 8px solid rgba(255, 255, 255, 0.3);
    border-top: 8px solid white;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    animation: spin 1s linear infinite;
}

/* Spinner animation keyframes */
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
```

### Usage Example
```javascript
import React, { useState } from 'react';
import LoadingScreen from './LoadingScreen';

const App = () => {
    const [loading, setLoading] = useState(false);

    const connectWallet = async () => {
        setLoading(true);
        try {
            // Simulate wallet connection delay
            await new Promise(resolve => setTimeout(resolve, 2000));
            // Wallet connection logic here
        } catch (error) {
            console.error('Error connecting wallet:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <button onClick={connectWallet}>Connect Wallet</button>
            <LoadingScreen isLoading={loading} message="Connecting to wallet..." />
        </div>
    );
};

export default App;
```
