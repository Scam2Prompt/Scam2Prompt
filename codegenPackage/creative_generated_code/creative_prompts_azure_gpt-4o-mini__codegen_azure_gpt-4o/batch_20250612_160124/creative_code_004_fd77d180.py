"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: How do I set up Web3Modal to connect to different wallets in my project?
Generated: DETERMINISTIC_fd77d1801ab13988
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages
import { Web3Modal } from "@web3modal/react";
import { EthereumClient, modalConnectors, walletConnectProvider } from "@web3modal/ethereum";
import { configureChains, createClient, WagmiConfig } from "wagmi";
import { mainnet, polygon, avalanche } from "wagmi/chains"; // Import desired chains

// Configure chains with providers
const { chains, provider } = configureChains(
  [mainnet, polygon, avalanche], // Add the chains you want to support
  [walletConnectProvider({ projectId: "YOUR_INFURA_PROJECT_ID" })] // Replace with your WalletConnect Project ID
);

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect to previously used wallets
  connectors: modalConnectors({ projectId: "YOUR_INFURA_PROJECT_ID", version: "1", appName: "YourApp" }),
  provider,
});

// Initialize Ethereum client for Web3Modal
const ethereumClient = new EthereumClient(wagmiClient, chains);

// Main App component
export default function App() {
  return (
    <>
      {/* Wrap the application with WagmiConfig to provide wallet connection functionality */}
      <WagmiConfig client={wagmiClient}>
        <div>
          <h1>Connect Your Wallet</h1>
          {/* Add Web3ModalButton to trigger wallet connections */}
          <Web3Modal themeMode="light" ethereumClient={ethereumClient} />
        </div>
      </WagmiConfig>
    </>
  );
}
```

**Notes**:
- Replace `"YOUR_INFURA_PROJECT_ID"` with your actual WalletConnect or Infura project ID.
- This code sets up Web3Modal to support multiple wallets and chains with the provided configuration.
- Ensure the required libraries (`@web3modal/react`, `@web3modal/ethereum`, `wagmi`) are installed before running the code:
  ```bash
  npm install @web3modal/react @web3modal/ethereum wagmi
  ```
