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

**web3modal-nextjs-integration**
=====================================

### Step 1: Install Web3Modal and required dependencies

```bash
npm install web3modal ethers
```

### Step 2: Create a Web3Modal instance

**web3modal.js**
```javascript
// Import required dependencies
import Web3Modal from 'web3modal';
import { ethers } from 'ethers';

// Create a Web3Modal instance
const web3Modal = new Web3Modal({
  // Network to connect to
  network: 'mainnet',
  // Cache provider
  cacheProvider: true,
  // Enable or disable the provider options
  providerOptions: {
    // MetaMask provider options
    metamask: {
      // Enable or disable MetaMask
      enabled: true,
    },
  },
});

export default web3Modal;
```

### Step 3: Create a Next.js API route for Web3Modal

**pages/api/web3modal.js**
```javascript
// Import required dependencies
import web3Modal from '../../lib/web3modal';

// API route for Web3Modal
export default async function handler(req, res) {
  try {
    // Handle GET request
    if (req.method === 'GET') {
      // Get the Web3Modal provider
      const provider = await web3Modal.connect();

      // Return the provider
      return res.status(200).json(provider);
    }

    // Handle POST request
    if (req.method === 'POST') {
      // Disconnect the Web3Modal provider
      await web3Modal.clearCachedProvider();

      // Return success response
      return res.status(200).json({ message: 'Provider disconnected' });
    }

    // Handle invalid request method
    return res.status(405).json({ message: 'Method not allowed' });
  } catch (error) {
    // Handle error
    console.error(error);
    return res.status(500).json({ message: 'Internal server error' });
  }
}
```

### Step 4: Create a Next.js page for Web3Modal integration

**pages/index.js**
```javascript
// Import required dependencies
import Head from 'next/head';
import web3Modal from '../lib/web3modal';
import { ethers } from 'ethers';

// Home page component
export default function Home() {
  // State to store the user's address
  const [address, setAddress] = useState(null);

  // Connect to Web3Modal
  const connectWeb3Modal = async () => {
    try {
      // Get the Web3Modal provider
      const provider = await web3Modal.connect();

      // Get the user's address
      const signer = provider.getSigner();
      const userAddress = await signer.getAddress();

      // Update the address state
      setAddress(userAddress);
    } catch (error) {
      // Handle error
      console.error(error);
    }
  };

  // Disconnect from Web3Modal
  const disconnectWeb3Modal = async () => {
    try {
      // Disconnect the Web3Modal provider
      await web3Modal.clearCachedProvider();

      // Update the address state
      setAddress(null);
    } catch (error) {
      // Handle error
      console.error(error);
    }
  };

  return (
    <div>
      <Head>
        <title>Web3Modal Next.js Integration</title>
      </Head>

      <main>
        <h1>Web3Modal Next.js Integration</h1>

        {address ? (
          <div>
            <p>Connected to {address}</p>
            <button onClick={disconnectWeb3Modal}>Disconnect</button>
          </div>
        ) : (
          <button onClick={connectWeb3Modal}>Connect</button>
        )}
      </main>
    </div>
  );
}
```

### Step 5: Configure Vercel environment variables

**vercel.json**
```json
{
  "env": {
    "NEXT_PUBLIC_WEB3MODAL_PROJECT_ID": "YOUR_WEB3MODAL_PROJECT_ID"
  }
}
```

**next.config.js**
```javascript
module.exports = {
  //...
  env: {
    NEXT_PUBLIC_WEB3MODAL_PROJECT_ID: process.env.NEXT_PUBLIC_WEB3MODAL_PROJECT_ID,
  },
};
```
