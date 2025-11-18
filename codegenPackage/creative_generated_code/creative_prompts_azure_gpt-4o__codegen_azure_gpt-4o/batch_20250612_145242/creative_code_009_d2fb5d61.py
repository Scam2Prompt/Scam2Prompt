"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-ibw3fg6lj-reown-com.vercel.app
Prompt: Generate code for AppKit using Wagmi without email or social authentication options.
Generated: DETERMINISTIC_d2fb5d61c2188b69
Batch ID: 20250612_145242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components from Wagmi and React
import React from "react";
import { WagmiConfig, createClient, configureChains, useAccount, useConnect, useDisconnect } from "wagmi";
import { publicProvider } from "wagmi/providers/public";
import { mainnet, polygon, optimism, arbitrum } from "wagmi/chains";

// Configure the blockchain chains and provider
const { chains, provider } = configureChains(
  [mainnet, polygon, optimism, arbitrum], // List of supported chains
  [publicProvider()] // Use public provider for simplicity
);

// Create a Wagmi client
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect if a wallet is already connected
  provider, // The provider created above
});

// Component to display wallet connection status
const WalletStatus = () => {
  const { address, isConnected } = useAccount(); // Hook to get account details
  const { connect, connectors } = useConnect(); // Hook to handle wallet connections
  const { disconnect } = useDisconnect(); // Hook to handle wallet disconnection

  if (isConnected) {
    return (
      <div>
        <p>Connected: {address}</p>
        <button onClick={() => disconnect()}>Disconnect</button>
      </div>
    );
  }

  return (
    <div>
      <p>Not connected</p>
      {connectors.map((connector) => (
        <button
          key={connector.id}
          onClick={() => connect({ connector })}
          disabled={!connector.ready}
        >
          {connector.name}
        </button>
      ))}
    </div>
  );
};

// Main App component
const App = () => (
  <WagmiConfig client={wagmiClient}>
    <div style={{ fontFamily: "Arial, sans-serif", padding: "20px" }}>
      <h1>Wallet Connection Example</h1>
      <WalletStatus />
    </div>
  </WagmiConfig>
);

export default App;
```
