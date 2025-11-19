"""
Generated Code Metadata:
========================
Original URL: https://web3-dapp.vercel.app
Prompt: Generate a step-by-step guide to integrate Web3Modal into a Next.js Web3 project hosted on Vercel.
Generated: DETERMINISTIC_20364bead0d62803
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# Step 1: Create a new Next.js project
npx create-next-app@latest my-web3-app
cd my-web3-app

# Step 2: Install necessary dependencies
npm install web3modal ethers
```

```javascript
// Step 3: Create a new file for Web3Modal configuration
// File: lib/web3Modal.js

import Web3Modal from 'web3modal';
import { ethers } from 'ethers';

/**
 * Initializes Web3Modal instance
 * @returns {Web3Modal} Instance of Web3Modal
 */
export const initWeb3Modal = () => {
  const providerOptions = {
    // Add any provider options here (e.g., WalletConnect, Fortmatic, etc.)
  };

  return new Web3Modal({
    cacheProvider: true, // optional
    providerOptions, // required
  });
};

/**
 * Connects to the wallet using Web3Modal
 * @returns {Promise<ethers.providers.Web3Provider>} Connected provider
 */
export const connectWallet = async () => {
  const web3Modal = initWeb3Modal();
  const provider = await web3Modal.connect();
  return new ethers.providers.Web3Provider(provider);
};
```

```javascript
// Step 4: Create a simple UI to connect to the wallet
// File: pages/index.js

import { useEffect, useState } from 'react';
import { connectWallet } from '../lib/web3Modal';

/**
 * Home component for the Next.js application
 * @returns {JSX.Element} Rendered component
 */
export default function Home() {
  const [account, setAccount] = useState(null);

  /**
   * Connects to the wallet and updates the account state
   */
  const handleConnectWallet = async () => {
    try {
      const provider = await connectWallet();
      const signer = provider.getSigner();
      const address = await signer.getAddress();
      setAccount(address);
    } catch (error) {
      console.error('Failed to connect wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Welcome to My Web3 App</h1>
      {account ? (
        <p>Connected Account: {account}</p>
      ) : (
        <button onClick={handleConnectWallet}>Connect Wallet</button>
      )}
    </div>
  );
}
```

```bash
# Step 5: Deploy the application to Vercel
# Make sure to install Vercel CLI if you haven't already
npm i -g vercel

# Deploy the application
vercel
```

```json
// Step 6: Add a .env.local file for environment variables (if needed)
// File: .env.local

# Add any environment variables here
# For example, if you are using Infura or Alchemy, you can add their URLs
NEXT_PUBLIC_INFURA_URL=your_infura_url
NEXT_PUBLIC_ALCHEMY_URL=your_alchemy_url
```

```javascript
// Step 7: Update the provider options in lib/web3Modal.js if needed
// Example for adding WalletConnect provider

const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider, // required
    options: {
      infuraId: process.env.NEXT_PUBLIC_INFURA_URL, // required
    },
  },
  // Add other providers as needed
};
```

```bash
# Step 8: Run the application locally to test
npm run dev
```

```bash
# Step 9: After testing, redeploy to Vercel
vercel --prod
```
