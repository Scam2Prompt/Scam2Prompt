"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Generate code for a frontend interface using React that allows users to input an ETH amount and displays the corresponding number of ALIEN tokens they will receive, based on the presale rate.
Generated: DETERMINISTIC_43232eb168744ee2
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/App.js

import React, { useState } from 'react';

// Constants for conversion rates
const PRESALE_RATE = 100; // Number of ALIEN tokens per ETH

// Main App component
const App = () => {
    // State to store ETH amount and ALIEN tokens
    const [ethAmount, setEthAmount] = useState('');
    const [alienTokens, setAlienTokens] = useState(null);

    // Handle input change for ETH amount
    const handleInputChange = (event) => {
        const value = event.target.value;

        // Update ETH amount in state
        setEthAmount(value);
        
        // Calculate ALIEN tokens if valid ETH amount is provided
        if (isNaN(value) || value < 0) {
            setAlienTokens(null);
        } else {
            const tokens = value * PRESALE_RATE;
            setAlienTokens(tokens);
        }
    };

    return (
        <div style={styles.container}>
            <h1>ETH to ALIEN Token Calculator</h1>
            <div style={styles.inputContainer}>
                <label htmlFor="ethInput" style={styles.label}>Enter ETH Amount:</label>
                <input
                    id="ethInput"
                    type="number"
                    value={ethAmount}
                    onChange={handleInputChange}
                    style={styles.input}
                    min="0"
                    step="0.01"
                    placeholder="0.00"
                />
            </div>
            {alienTokens !== null && (
                <div style={styles.result}>
                    <h2>{alienTokens.toFixed(2)} ALIEN Tokens</h2>
                </div>
            )}
        </div>
    );
};

// Styles for the component
const styles = {
    container: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
        backgroundColor: '#f4f4f4',
        fontFamily: 'Arial, sans-serif',
    },
    inputContainer: {
        margin: '20px 0',
    },
    label: {
        fontSize: '18px',
    },
    input: {
        padding: '10px',
        fontSize: '16px',
        marginLeft: '10px',
    },
    result: {
        marginTop: '20px',
        fontSize: '24px',
        fontWeight: 'bold',
    },
};

// Export the App component
export default App;
```

```bash
# src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Render the main App component
ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);
```

```json
// package.json (essential parts)

{
  "name": "eth-alien-token-calculator",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

To run the application, ensure you have Node.js installed, then run the following commands in your terminal:

```bash
# Install dependencies
npm install

# Start the development server
npm start
```
