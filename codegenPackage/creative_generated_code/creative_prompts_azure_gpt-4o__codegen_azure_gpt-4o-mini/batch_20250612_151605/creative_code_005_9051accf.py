"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-homepage.vercel.app
Prompt: Provide a code example to integrate Starknet wallet functionality into a React application using `Starknet-React`.
Generated: DETERMINISTIC_9051accf93043d08
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies from React and Starknet libraries
import React, { useEffect, useState } from 'react';
import { StarknetProvider, useStarknet } from '@starknet-react/core';

// Main App component
const App = () => {
  // State to handle connected wallet address
  const [walletAddress, setWalletAddress] = useState(null);
  // Use Starknet hook to access wallet functionality
  const { account, connect, disconnect } = useStarknet();

  // Effect to update wallet address when account changes
  useEffect(() => {
    if (account) {
      setWalletAddress(account);
    } else {
      setWalletAddress(null);
    }
  }, [account]);

  // Function to handle wallet connection
  const handleConnect = async () => {
    try {
      await connect();
    } catch (error) {
      console.error("Error connecting to wallet:", error);
    }
  };

  // Function to handle wallet disconnection
  const handleDisconnect = async () => {
    try {
      await disconnect();
      setWalletAddress(null);
    } catch (error) {
      console.error("Error disconnecting from wallet:", error);
    }
  };

  return (
    <StarknetProvider>
      <div>
        <h1>Starknet Wallet Integration</h1>
        {walletAddress ? (
          <div>
            <p>Connected Wallet: {walletAddress}</p>
            <button onClick={handleDisconnect}>Disconnect Wallet</button>
          </div>
        ) : (
          <button onClick={handleConnect}>Connect Wallet</button>
        )}
      </div>
    </StarknetProvider>
  );
};

export default App;
```

```javascript
// index.js - Entry point for the React application
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Render the main App component into the root element
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```json
// package.json - Necessary dependencies for the project
{
  "name": "starknet-wallet-integration",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "@starknet-react/core": "^0.1.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
``` 

Make sure to run `npm install` to install the dependencies before starting the application.
