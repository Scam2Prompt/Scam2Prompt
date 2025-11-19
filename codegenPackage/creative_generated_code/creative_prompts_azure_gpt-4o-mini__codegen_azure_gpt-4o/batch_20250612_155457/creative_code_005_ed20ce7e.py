"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-ibhc82bf8-reown-com.vercel.app
Prompt: Create a demo code that showcases all features enabled, using sample wallets with either Ethers or Wagmi as per the AppKit Lab documentation.
Generated: DETERMINISTIC_ed20ce7e5de9edd6
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Wagmi and Ethers
import { WagmiConfig, createClient, useAccount, useConnect, useDisconnect, useBalance } from 'wagmi';
import { getDefaultWallets } from '@rainbow-me/rainbowkit';
import { configureChains, chain, publicProvider } from 'wagmi';
import { ethers } from 'ethers';

// Configure chains and providers for Wagmi
const { chains, provider } = configureChains(
  [chain.mainnet, chain.goerli], // Include mainnet and Goerli testnet
  [publicProvider()] // Use the default public provider
);

// Configure default wallets via RainbowKit
const { connectors } = getDefaultWallets({
  appName: 'Demo App', // Name for the wallet connection modal
  chains,
});

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true, // Auto-connect wallet if available
  connectors,
  provider,
});

// App Component
function App() {
  // Hooks to access Wagmi functionalities
  const { connect, connectors, error: connectError } = useConnect();
  const { disconnect } = useDisconnect();
  const { isConnected, address } = useAccount();
  const { data: balance, error: balanceError } = useBalance({
    addressOrName: address,
  });

  return (
    <WagmiConfig client={wagmiClient}>
      <div style={{ padding: '20px' }}>
        <h1>Demo App</h1>

        {/* Wallet Connection Section */}
        {isConnected ? (
          <div>
            <p>Wallet Address: {address}</p>
            {/* Display user balance */}
            {balance && <p>Balance: {ethers.utils.formatEther(balance.value)} ETH</p>}
            {balanceError && <p>Error fetching balance: {balanceError.message}</p>}
            <button onClick={() => disconnect()}>Disconnect Wallet</button>
          </div>
        ) : (
          <div>
            <h2>Connect Your Wallet</h2>
            {connectors.map((connector) => (
              <button
                key={connector.id}
                onClick={() => connect(connector)}
                disabled={!connector.ready}
              >
                {connector.name}
                {/* Show if connector is unsupported */}
                {!connector.ready && ' (unsupported)'}
              </button>
            ))}
            {connectError && <p>Error connecting: {connectError.message}</p>}
          </div>
        )}
      </div>
    </WagmiConfig>
  );
}

export default App;
```
