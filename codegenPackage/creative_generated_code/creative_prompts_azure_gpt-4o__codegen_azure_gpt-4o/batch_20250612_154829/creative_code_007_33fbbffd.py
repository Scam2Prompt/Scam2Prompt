"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: Provide an example of integrating MetaMask SDK with Wagmi to handle wallet connection and transaction management in a Next.js project.
Generated: DETERMINISTIC_33fbbffd96bd7e9f
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: pages/_app.js
import '../styles/globals.css';
import { WagmiConfig, createClient, configureChains } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';
import { MetaMaskConnector } from 'wagmi/connectors/metaMask';
import { mainnet, goerli } from 'wagmi/chains';

// Configure chains and providers
const { chains, provider } = configureChains([mainnet, goerli], [publicProvider()]);

// Initialize Wagmi client
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect to the wallet if possible
  connectors: [
    new MetaMaskConnector({ chains }), // MetaMask Connector
  ],
  provider,
});

// Main application wrapper
export default function App({ Component, pageProps }) {
  return (
    <WagmiConfig client={wagmiClient}>
      <Component {...pageProps} />
    </WagmiConfig>
  );
}
```

```javascript
// File: components/WalletManager.js
import { useState } from 'react';
import { useAccount, useConnect, useDisconnect, useBalance, useSendTransaction } from 'wagmi';
import { parseEther } from 'ethers/lib/utils';

const WalletManager = () => {
  const { connect, connectors, error } = useConnect(); // Handles wallet connections
  const { disconnect } = useDisconnect(); // Handles wallet disconnections
  const { address, isConnected } = useAccount(); // Fetches the current account
  const { data: balance, refetch } = useBalance({ address }); // Fetches the wallet balance
  const { sendTransaction } = useSendTransaction(); // Handles transactions

  const [transactionValue, setTransactionValue] = useState('');

  const handleTransaction = async () => {
    try {
      await sendTransaction({
        to: '0xRecipientAddressHere', // Replace with the recipient address
        value: parseEther(transactionValue), // Convert the value to Ether
      });
      alert('Transaction sent successfully!');
      refetch(); // Refresh balance after transaction
    } catch (err) {
      console.error('Transaction failed:', err.message);
      alert('Transaction failed!');
    }
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h1>Wallet Manager</h1>

      {/* Wallet Connection Section */}
      {!isConnected ? (
        <div>
          <h2>Connect Wallet</h2>
          {connectors.map((connector) => (
            <button
              key={connector.id}
              onClick={() => connect({ connector })}
              disabled={!connector.ready}
            >
              {connector.name}
              {!connector.ready && ' (unsupported)'}
            </button>
          ))}
          {error && <p style={{ color: 'red' }}>{error.message}</p>}
        </div>
      ) : (
        <div>
          {/* Wallet Info Section */}
          <h2>Wallet Connected</h2>
          <p>Address: {address}</p>
          <p>Balance: {balance?.formatted} {balance?.symbol}</p>
          <button onClick={disconnect}>Disconnect</button>

          {/* Transaction Section */}
          <h2>Send Transaction</h2>
          <input
            type="number"
            placeholder="Enter amount in ETH"
            value={transactionValue}
            onChange={(e) => setTransactionValue(e.target.value)}
          />
          <button onClick={handleTransaction}>Send</button>
        </div>
      )}
    </div>
  );
};

export default WalletManager;
```

```javascript
// File: pages/index.js
import WalletManager from '../components/WalletManager';

const Home = () => {
  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px' }}>
      <h1>Next.js + MetaMask + Wagmi</h1>
      <WalletManager />
    </div>
  );
};

export default Home;
```

```javascript
// File: styles/globals.css
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
  color: #333;
}

button {
  margin: 5px;
  padding: 10px 20px;
  font-size: 14px;
  cursor: pointer;
}

input {
  padding: 10px;
  font-size: 14px;
  margin: 5px;
  width: 100%;
}
```

**Note:** Replace `0xRecipientAddressHere` in the transaction handling logic with the actual recipient Ethereum address. Ensure you have MetaMask installed and connected to the correct network to test this functionality.
