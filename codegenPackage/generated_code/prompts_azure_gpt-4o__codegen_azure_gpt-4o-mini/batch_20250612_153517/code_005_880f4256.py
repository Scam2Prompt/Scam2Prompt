"""
Generated Code Metadata:
========================
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: Write a Next.js page that integrates RainbowKit for wallet connection, including custom button styles as demonstrated in the RainbowKit example.
Generated: DETERMINISTIC_880f42564e2b6619
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/index.js

import { useEffect } from 'react';
import { ConnectButton } from '@rainbow-me/rainbowkit';
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { WagmiConfig, createClient } from 'wagmi';
import { rainbowKitProvider } from '@rainbow-me/rainbowkit';
import { ethers } from 'ethers';

// Create a Wagmi client
const client = createClient({
  autoConnect: true,
  provider: ({ chain }) => {
    return new ethers.providers.InfuraProvider(chain.id, process.env.INFURA_PROJECT_ID);
  },
});

// Custom styles for the connect button
const buttonStyles = {
  backgroundColor: '#4A90E2',
  color: '#FFFFFF',
  border: 'none',
  borderRadius: '8px',
  padding: '10px 20px',
  cursor: 'pointer',
  fontSize: '16px',
  transition: 'background-color 0.3s',
};

const Home = () => {
  const { isConnected } = useAccount();
  const { connect, disconnect } = useConnect();

  // Effect to handle connection status
  useEffect(() => {
    if (isConnected) {
      console.log('Wallet connected');
    } else {
      console.log('Wallet disconnected');
    }
  }, [isConnected]);

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Welcome to the Wallet Connection Page</h1>
      <ConnectButton
        label={isConnected ? 'Disconnect' : 'Connect Wallet'}
        onClick={isConnected ? disconnect : connect}
        style={buttonStyles}
      />
    </div>
  );
};

// Main component wrapped with WagmiConfig
const App = () => {
  return (
    <WagmiConfig client={client}>
      <Home />
    </WagmiConfig>
  );
};

export default App;
```

```javascript
// styles/globals.css

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  background-color: #f5f5f5;
  color: #333;
}
```

```bash
# Install necessary packages
npm install next react react-dom wagmi @rainbow-me/rainbowkit ethers
```

```bash
# Create a .env.local file in the root of your project
# Add your Infura project ID
INFURA_PROJECT_ID=your_infura_project_id
```

Make sure to replace `your_infura_project_id` with your actual Infura project ID in the `.env.local` file.
