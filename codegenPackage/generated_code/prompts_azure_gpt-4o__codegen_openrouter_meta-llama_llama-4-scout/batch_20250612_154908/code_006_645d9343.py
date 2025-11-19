"""
Generated Code Metadata:
========================
Original URL: https://aptos-playback-policy.vercel.app
Prompt: Generate a Next.js app template that includes Aptos wallet connection and playback policy integration.
Generated: DETERMINISTIC_645d9343fb91f971
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**pages/_app.js**
```jsx
import { AptosWallet } from '@aptos/wallet-adapter';
import { WalletProvider } from '@aptos/wallet-adapter-react';
import { PlaybackPolicyProvider } from '../contexts/PlaybackPolicyContext';
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
  return (
    <WalletProvider
      wallets={[new AptosWallet()]}
      onError={(error) => console.error('Wallet error:', error)}
    >
      <PlaybackPolicyProvider>
        <Component {...pageProps} />
      </PlaybackPolicyProvider>
    </WalletProvider>
  );
}

export default MyApp;
```

**contexts/PlaybackPolicyContext.js**
```javascript
import { createContext, useState, useEffect } from 'react';

const PlaybackPolicyContext = createContext();

const PlaybackPolicyProvider = ({ children }) => {
  const [policy, setPolicy] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPlaybackPolicy = async () => {
      try {
        const response = await fetch('/api/playback-policy');
        const data = await response.json();
        setPolicy(data);
      } catch (error) {
        setError(error);
      }
    };
    fetchPlaybackPolicy();
  }, []);

  return (
    <PlaybackPolicyContext.Provider value={{ policy, error }}>
      {children}
    </PlaybackPolicyContext.Provider>
  );
};

export { PlaybackPolicyProvider, PlaybackPolicyContext };
```

**pages/api/playback-policy.js**
```javascript
import { NextApiRequest, NextApiResponse } from 'next';

const playbackPolicy = {
  // Add your playback policy data here
  id: 1,
  name: 'Example Policy',
  rules: [
    {
      id: 1,
      type: 'allow',
      conditions: [
        {
          id: 1,
          type: 'geo',
          value: 'US',
        },
      ],
    },
  ],
};

const getPlaybackPolicy = async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    return res.status(200).json(playbackPolicy);
  } catch (error) {
    return res.status(500).json({ error: 'Failed to fetch playback policy' });
  }
};

export default getPlaybackPolicy;
```

**components/WalletConnector.js**
```jsx
import { useWallet } from '@aptos/wallet-adapter-react';

const WalletConnector = () => {
  const { account, connect, disconnect } = useWallet();

  if (!account) {
    return (
      <button onClick={() => connect()}>
        Connect Wallet
      </button>
    );
  }

  return (
    <div>
      <p>Connected to {account.address}</p>
      <button onClick={() => disconnect()}>
        Disconnect Wallet
      </button>
    </div>
  );
};

export default WalletConnector;
```

**pages/index.js**
```jsx
import WalletConnector from '../components/WalletConnector';
import { usePlaybackPolicy } from '../contexts/PlaybackPolicyContext';

const Home = () => {
  const { policy, error } = usePlaybackPolicy();

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  if (!policy) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h1>Playback Policy</h1>
      <p>Policy ID: {policy.id}</p>
      <p>Policy Name: {policy.name}</p>
      <WalletConnector />
    </div>
  );
};

export default Home;
```

**next.config.js**
```javascript
module.exports = {
  reactStrictMode: true,
  webpack: (config) => {
    config.resolve.fallback = {
      fs: false,
      path: false,
    };
    return config;
  },
};
```

**package.json**
```json
{
  "name": "aptos-wallet-nextjs-template",
  "version": "0.1.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "@aptos/wallet-adapter": "^1.0.0",
    "@aptos/wallet-adapter-react": "^1.0.0",
    "next": "^12.1.6",
    "react": "^18.2.0"
  }
}
```
