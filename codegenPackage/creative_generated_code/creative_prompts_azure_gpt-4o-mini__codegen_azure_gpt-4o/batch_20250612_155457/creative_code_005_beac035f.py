"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-n76z148gg-reown-com.vercel.app
Prompt: Create a demo using sample wallets with all features enabled in AppKit, utilizing ethers or wagmi.
Generated: DETERMINISTIC_beac035fc4f3606a
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import { useState, useEffect } from 'react';
import { ethers } from 'ethers'; // Ethers.js library
import { configureChains, createClient, WagmiConfig, useAccount, useConnect, useDisconnect } from 'wagmi';
import { mainnet, goerli } from 'wagmi/chains'; // Chains to configure
import { publicProvider } from 'wagmi/providers/public'; // Public provider for blockchain data

// Configure chains and providers
const { chains, provider } = configureChains(
  [mainnet, goerli], // Specify chains for the app (Mainnet and Goerli here as an example)
  [publicProvider()] // Use the public provider
);

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect wallets if possible
  provider, // Specify provider configuration
});

// Main App Component
function App() {
  const { connect, connectors } = useConnect(); // Handle wallet connection
  const { disconnect } = useDisconnect(); // Handle wallet disconnection
  const { address, isConnected } = useAccount(); // Get account details

  const [balance, setBalance] = useState(null); // Track wallet balance

  // Fetch wallet balance when address changes
  useEffect(() => {
    if (address && isConnected) {
      const fetchBalance = async () => {
        try {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          const balanceInWei = await provider.getBalance(address); // Get balance in Wei
          const balanceInEth = ethers.utils.formatEther(balanceInWei); // Convert to ETH
          setBalance(balanceInEth);
        } catch (error) {
          console.error("Error fetching wallet balance:", error); // Log any errors
        }
      };
      fetchBalance();
    } else {
      setBalance(null); // Reset balance when disconnected
    }
  }, [address, isConnected]);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>AppKit Wallet Demo</h1>
      {isConnected ? (
        <>
          <p>Connected Address: {address}</p>
          <p>Wallet Balance: {balance ? `${balance} ETH` : 'Fetching...'}</p>
          <button onClick={disconnect} style={{ padding: '10px', cursor: 'pointer' }}>
            Disconnect Wallet
          </button>
        </>
      ) : (
        <>
          <p>No wallet connected.</p>
          {connectors.map((connector) => (
            <button
              key={connector.id}
              onClick={() => connect({ connector })}
              style={{ padding: '10px', margin: '5px', cursor: 'pointer' }}
              disabled={!connector.ready}
            >
              {connector.name}
              {!connector.ready && ' (not supported)'}
            </button>
          ))}
        </>
      )}
    </div>
  );
}

// Render the App Component within WagmiConfig
function Root() {
  return (
    <WagmiConfig client={wagmiClient}>
      <App />
    </WagmiConfig>
  );
}

export default Root; // Export the root component for rendering
```
