"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapptoolkit.com
Prompt: Write code using the Web3Modal SDK to connect a user's wallet to a decentralized application, ensuring compatibility with multiple chains like Ethereum, Binance, and Polygon.
Generated: DETERMINISTIC_e9d65c80777e9437
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import { Web3Modal } from "@web3modal/react";
import { EthereumClient, w3mProvider, w3mConnectors } from "@web3modal/ethereum";
import { configureChains, createClient } from "wagmi";
import { mainnet, polygon, bsc } from "wagmi/chains";
import { useState } from "react";

// Configuration for supported chains: Ethereum, Binance Smart Chain, Polygon
const chains = [mainnet, polygon, bsc];

// Configure chains and providers
const { provider } = configureChains(chains, [w3mProvider({ projectId: "<YOUR_PROJECT_ID>" })]);

// Create Wagmi Client
const wagmiClient = createClient({
  autoConnect: true,
  connectors: w3mConnectors({ chains, projectId: "<YOUR_PROJECT_ID>" }),
  provider,
});

// Initialize Ethereum Client for Web3Modal
const ethereumClient = new EthereumClient(wagmiClient, chains);

const WalletConnector = () => {
  // State to store connection status
  const [connectedAccount, setConnectedAccount] = useState(null);

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      // Request the wallet connection
      const signer = await wagmiClient.getSigner();

      // Fetch wallet address
      const address = await signer.getAddress();

      // Update state with connected account
      setConnectedAccount(address);
    } catch (error) {
      console.error("Failed to connect wallet:", error);
    }
  };

  return (
    <div>
      {/* Button to trigger wallet connection */}
      <button onClick={connectWallet}>
        {connectedAccount ? "Wallet Connected" : "Connect Wallet"}
      </button>

      {/* Display connected wallet address */}
      {connectedAccount && <p>Connected Address: {connectedAccount}</p>}

      {/* Web3Modal UI */}
      <Web3Modal projectId="<YOUR_PROJECT_ID>" ethereumClient={ethereumClient} />
    </div>
  );
};

export default WalletConnector;
```
