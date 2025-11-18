"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: Write code to integrate StarkNet wallet authentication into a decentralized application built with Next.js.
Generated: DETERMINISTIC_1ac68fd4388f94dc
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
import { StarknetProvider } from '@starknet/react';

function MyApp({ Component, pageProps }) {
  return (
    <StarknetProvider>
      <Component {...pageProps} />
    </StarknetProvider>
  );
}

export default MyApp;

// pages/index.js
import { useStarknet, useAccount } from '@starknet/react';
import { useState } from 'react';

const Home = () => {
  const { account, connect, disconnect } = useStarknet();
  const [error, setError] = useState(null);

  // Function to handle wallet connection
  const handleConnect = async () => {
    try {
      setError(null);
      await connect();
    } catch (err) {
      setError('Failed to connect wallet. Please try again.');
      console.error(err);
    }
  };

  // Function to handle wallet disconnection
  const handleDisconnect = async () => {
    try {
      await disconnect();
    } catch (err) {
      setError('Failed to disconnect wallet. Please try again.');
      console.error(err);
    }
  };

  return (
    <div>
      <h1>StarkNet Wallet Authentication</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={handleDisconnect}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={handleConnect}>Connect Wallet</button>
      )}
    </div>
  );
};

export default Home;

// Additional setup instructions would typically be included in README.md
```
