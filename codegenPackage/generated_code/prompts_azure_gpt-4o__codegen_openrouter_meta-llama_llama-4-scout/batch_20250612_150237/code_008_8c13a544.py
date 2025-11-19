"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write a code snippet to detect the connected blockchain chain ID and display it in a Next.js application, using the tools mentioned in the Dapp Starter.
Generated: DETERMINISTIC_8c13a544a27ae4c9
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// components/ChainId.js
import { useEffect, useState } from 'react';
import Web3 from 'web3';

/**
 * Component to display the connected blockchain chain ID.
 */
const ChainId = () => {
  const [chainId, setChainId] = useState(null);
  const [error, setError] = useState(null);

  // Initialize web3 provider
  const web3 = new Web3(window.ethereum);

  useEffect(() => {
    const getChainId = async () => {
      try {
        // Check if Ethereum provider is available
        if (window.ethereum) {
          // Get chain ID
          const chainId = await web3.eth.getChainId();
          setChainId(chainId);
        } else {
          setError('Ethereum provider not available');
        }
      } catch (error) {
        setError(error.message);
      }
    };
    getChainId();
  }, []);

  return (
    <div>
      {chainId ? (
        <p>Connected to chain ID: {chainId}</p>
      ) : (
        <p>{error || 'Loading...'}</p>
      )}
    </div>
  );
};

export default ChainId;
```

```javascript
// pages/_app.js
import ChainId from '../components/ChainId';

function MyApp({ Component, pageProps }) {
  return (
    <div>
      <ChainId />
      <Component {...pageProps} />
    </div>
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import Head from 'next/head';

export default function Home() {
  return (
    <div>
      <Head>
        <title>Blockchain Chain ID Detector</title>
      </Head>
      <h1>Blockchain Chain ID Detector</h1>
    </div>
  );
}
```

```javascript
// utils/web3.js
import Web3 from 'web3';

/**
 * Initialize web3 provider.
 */
const initializeWeb3 = () => {
  if (window.ethereum) {
    return new Web3(window.ethereum);
  } else {
    throw new Error('Ethereum provider not available');
  }
};

export default initializeWeb3;
```

```javascript
// next.config.js
module.exports = {
  //...
  webpack: (config) => {
    config.resolve.fallback = {
      //...
      web3: false,
    };
    return config;
  },
};
```
