"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetapp.vercel.app
Prompt: Write code to integrate a "Connect Wallet" button for a StarkNet-based dApp using Next.js.
Generated: DETERMINISTIC_8229f9e2fcb6ffff
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js

import { useEffect } from 'react';
import { StarknetProvider } from '@starknet-react/core';
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
  return (
    <StarknetProvider>
      <Component {...pageProps} />
    </StarknetProvider>
  );
}

export default MyApp;
```

```javascript
// components/ConnectWalletButton.js

import React from 'react';
import { useStarknet, useAccount } from '@starknet-react/core';

const ConnectWalletButton = () => {
  const { account, connect, disconnect } = useStarknet();
  
  // Function to handle wallet connection
  const handleConnect = async () => {
    try {
      await connect();
    } catch (error) {
      console.error('Failed to connect wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Function to handle wallet disconnection
  const handleDisconnect = () => {
    try {
      disconnect();
    } catch (error) {
      console.error('Failed to disconnect wallet:', error);
    }
  };

  return (
    <div>
      {account ? (
        <button onClick={handleDisconnect}>
          Disconnect Wallet ({account.slice(0, 6)}...{account.slice(-4)})
        </button>
      ) : (
        <button onClick={handleConnect}>
          Connect Wallet
        </button>
      )}
    </div>
  );
};

export default ConnectWalletButton;
```

```javascript
// pages/index.js

import React from 'react';
import ConnectWalletButton from '../components/ConnectWalletButton';

const IndexPage = () => {
  return (
    <div>
      <h1>Welcome to My StarkNet dApp</h1>
      <ConnectWalletButton />
    </div>
  );
};

export default IndexPage;
```

```json
// package.json

{
  "name": "starknet-dapp",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest",
    "@starknet-react/core": "latest"
  },
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

```bash
# Command to install dependencies
npm install
```

```bash
# Command to run the development server
npm run dev
```

```css
/* styles/globals.css */
/* Add any global styles here */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
  color: #333;
}

h1 {
  text-align: center;
  margin-top: 50px;
}
```

This code integrates a "Connect Wallet" button into a StarkNet-based dApp using Next.js, following best practices, with proper error handling and documentation.
