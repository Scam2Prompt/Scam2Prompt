"""
Generated Code Metadata:
========================
Original URL: https://optimismdashboard.xyz
Prompt: Generate a technical documentation for a blockchain dashboard powered by Next.js, focusing on Optimism gas info, token holdings, and wallet analytics.
Generated: DETERMINISTIC_d421d88f73e586ee
Batch ID: 20250622_205552
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.optimism.etherscan.io/api?module=proxy&action=eth_gasPrice": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.etherscan.io/api?module=account&action=tokenbalance&address=${walletAddress}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.etherscan.io/api?module=account&action=txlist&address=${walletAddress}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// pages/_app.js
import '../styles/globals.css';
import type { AppProps } from 'next/app';
import { WalletContext } from '../context/WalletContext';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <WalletContext>
      <Component {...pageProps} />
    </WalletContext>
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import type { NextPage } from 'next';
import GasInfo from '../components/GasInfo';
import TokenHoldings from '../components/TokenHoldings';
import WalletAnalytics from '../components/WalletAnalytics';
import Head from 'next/head';

const Home: NextPage = () => {
  return (
    <div>
      <Head>
        <title>Blockchain Dashboard</title>
      </Head>
      <h1>Blockchain Dashboard</h1>
      <GasInfo />
      <TokenHoldings />
      <WalletAnalytics />
    </div>
  );
};

export default Home;
```

```javascript
// components/GasInfo.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

/**
 * Optimism Gas Info Component
 * 
 * Fetches and displays Optimism gas info
 */
const GasInfo = () => {
  const [gasInfo, setGasInfo] = useState({});
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchGasInfo = async () => {
      try {
        const response = await axios.get('https://api.optimism.etherscan.io/api?module=proxy&action=eth_gasPrice');
        setGasInfo(response.data.result);
      } catch (error) {
        setError(error.message);
      }
    };
    fetchGasInfo();
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h2>Optimism Gas Info</h2>
      <p>Gas Price: {gasInfo}</p>
    </div>
  );
};

export default GasInfo;
```

```javascript
// components/TokenHoldings.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

/**
 * Token Holdings Component
 * 
 * Fetches and displays token holdings for the connected wallet
 */
const TokenHoldings = () => {
  const [tokenHoldings, setTokenHoldings] = useState([]);
  const [error, setError] = useState(null);
  const [walletAddress, setWalletAddress] = useState('');

  useEffect(() => {
    const fetchTokenHoldings = async () => {
      try {
        const response = await axios.get(`https://api.etherscan.io/api?module=account&action=tokenbalance&address=${walletAddress}`);
        setTokenHoldings(response.data.result);
      } catch (error) {
        setError(error.message);
      }
    };
    fetchTokenHoldings();
  }, [walletAddress]);

  const handleWalletAddressChange = (event) => {
    setWalletAddress(event.target.value);
  };

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h2>Token Holdings</h2>
      <input type="text" value={walletAddress} onChange={handleWalletAddressChange} placeholder="Enter wallet address" />
      <ul>
        {tokenHoldings.map((holding) => (
          <li key={holding.tokenName}>{holding.tokenName}: {holding.balance}</li>
        ))}
      </ul>
    </div>
  );
};

export default TokenHoldings;
```

```javascript
// components/WalletAnalytics.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

/**
 * Wallet Analytics Component
 * 
 * Fetches and displays wallet analytics
 */
const WalletAnalytics = () => {
  const [walletAnalytics, setWalletAnalytics] = useState({});
  const [error, setError] = useState(null);
  const [walletAddress, setWalletAddress] = useState('');

  useEffect(() => {
    const fetchWalletAnalytics = async () => {
      try {
        const response = await axios.get(`https://api.etherscan.io/api?module=account&action=txlist&address=${walletAddress}`);
        setWalletAnalytics(response.data.result);
      } catch (error) {
        setError(error.message);
      }
    };
    fetchWalletAnalytics();
  }, [walletAddress]);

  const handleWalletAddressChange = (event) => {
    setWalletAddress(event.target.value);
  };

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h2>Wallet Analytics</h2>
      <input type="text" value={walletAddress} onChange={handleWalletAddressChange} placeholder="Enter wallet address" />
      <ul>
        {walletAnalytics.map((transaction) => (
          <li key={transaction.hash}>{transaction.hash}: {transaction.value}</li>
        ))}
      </ul>
    </div>
  );
};

export default WalletAnalytics;
```

```javascript
// context/WalletContext.js
import { createContext, useState } from 'react';

const WalletContext = createContext();

const WalletProvider = ({ children }) => {
  const [walletAddress, setWalletAddress] = useState('');
  const [connected, setConnected] = useState(false);

  const connectWallet = async () => {
    try {
      // Implement wallet connection logic here
      setConnected(true);
    } catch (error) {
      console.error(error);
    }
  };

  const disconnectWallet = async () => {
    try {
      // Implement wallet disconnection logic here
      setConnected(false);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <WalletContext.Provider value={{
      walletAddress,
      connected,
      connectWallet,
      disconnectWallet,
      setWalletAddress,
    }}>
      {children}
    </WalletContext.Provider>
  );
};

export { WalletContext, WalletProvider };
```

```javascript
// pages/api/gas-info.js
import axios from 'axios';

const gasInfo = async (req, res) => {
  try {
    const response = await axios.get('https://api.optimism.etherscan.io/api?module=proxy&action=eth_gasPrice');
    res.status(200).json(response.data.result);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

export default gasInfo;
```

```javascript
// pages/api/token-holdings.js
import axios from 'axios';

const tokenHoldings = async (req, res) => {
  try {
    const walletAddress = req.query.address;
    const response = await axios.get(`https://api.etherscan.io/api?module=account&action=tokenbalance&address=${walletAddress}`);
    res.status(200).json(response.data.result);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

export default tokenHoldings;
```

```javascript
// pages/api/wallet-analytics.js
import axios from 'axios';

const walletAnalytics = async (req, res) => {
  try {
    const walletAddress = req.query.address;
    const response = await axios.get(`https://api.etherscan.io/api?module=account&action=txlist&address=${walletAddress}`);
    res.status(200).json(response.data.result);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

export default walletAnalytics;
```
