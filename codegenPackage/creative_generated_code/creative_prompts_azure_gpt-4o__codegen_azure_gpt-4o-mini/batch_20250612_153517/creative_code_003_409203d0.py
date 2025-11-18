"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: Generate a React component that uses RainbowKit to connect a MetaMask wallet, with custom button designs similar to the RainbowKit example.
Generated: DETERMINISTIC_409203d06d29d442
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React from 'react';
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { RainbowKitProvider, ConnectButton } from '@rainbow-me/rainbowkit';
import '@rainbow-me/rainbowkit/styles.css';
import './App.css'; // Custom styles can be defined in this file

const WalletConnectButton = () => {
  const { isConnected } = useAccount();
  const { connect, disconnect } = useConnect();
  
  // Custom button styles
  const buttonStyle = {
    padding: '10px 20px',
    borderRadius: '8px',
    border: 'none',
    cursor: 'pointer',
    backgroundColor: isConnected ? '#FF3D00' : '#4CAF50',
    color: 'white',
    fontWeight: 'bold',
    fontSize: '16px',
  };

  // Handle connect and disconnect actions
  const handleConnect = async () => {
    try {
      await connect(new InjectedConnector());
    } catch (error) {
      console.error("Connection error:", error);
    }
  };

  const handleDisconnect = async () => {
    try {
      await disconnect();
    } catch (error) {
      console.error("Disconnection error:", error);
    }
  };

  return (
    <button
      style={buttonStyle}
      onClick={isConnected ? handleDisconnect : handleConnect}
    >
      {isConnected ? 'Disconnect Wallet' : 'Connect MetaMask'}
    </button>
  );
};

const App = () => {
  return (
    <RainbowKitProvider>
      <div style={{ textAlign: 'center', marginTop: '50px' }}>
        <h1>Connect Your Wallet</h1>
        <WalletConnectButton />
      </div>
    </RainbowKitProvider>
  );
};

export default App;
```

```css
/* App.css */
body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
  color: #333;
}

h1 {
  color: #444;
}
```
