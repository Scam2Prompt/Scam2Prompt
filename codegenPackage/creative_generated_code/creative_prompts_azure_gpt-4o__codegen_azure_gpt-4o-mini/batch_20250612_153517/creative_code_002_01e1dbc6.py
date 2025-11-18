"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: Provide a code example for adding a "Connect Wallet" functionality using RainbowKit, specifically referencing the example provided on the RainbowKit demo page.
Generated: DETERMINISTIC_01e1dbc69e3b1824
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from React and RainbowKit
import React from 'react';
import ReactDOM from 'react-dom';
import { RainbowKitProvider, lightTheme } from '@rainbow-me/rainbowkit';
import { ethers } from 'ethers';
import { WagmiConfig, createClient } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';

// Create a Wagmi client with default configuration
const client = createClient({
  autoConnect: true,
  connectors: () => [
    new InjectedConnector({ chains: [] }), // Add your preferred chains here
  ],
});

// Main App component
const App = () => {
  return (
    <WagmiConfig client={client}>
      <RainbowKitProvider theme={lightTheme()} modalSize="compact">
        <div style={{ padding: '20px', textAlign: 'center' }}>
          <h1>Connect Your Wallet</h1>
          <ConnectButton />
        </div>
      </RainbowKitProvider>
    </WagmiConfig>
  );
};

// ConnectButton component handles wallet connection
const ConnectButton = () => {
  const { connect, connectors } = useConnect();

  // Function to handle connection error
  const handleConnectError = (error) => {
    console.error("Connection error:", error);
    alert("Failed to connect wallet. Please try again.");
  };

  return (
    <div>
      {connectors.map((connector) => (
        <button
          key={connector.id}
          onClick={() => {
            connect(connector).catch(handleConnectError);
          }}
          style={{ margin: '10px', padding: '10px 20px' }}
        >
          Connect {connector.name}
        </button>
      ))}
    </div>
  );
};

// Render the App component into the DOM
ReactDOM.render(<App />, document.getElementById('root'));
```

Make sure to install the required packages before running the code:
```bash
npm install @rainbow-me/rainbowkit wagmi ethers react react-dom
``` 

Additionally, ensure you have a div with the id 'root' in your HTML file for the React app to render correctly.
