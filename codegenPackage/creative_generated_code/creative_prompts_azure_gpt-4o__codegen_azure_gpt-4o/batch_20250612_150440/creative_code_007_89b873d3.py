"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Write a JavaScript function using Web3-React to check if a wallet is connected and retrieve the currently selected blockchain network (e.g., Optimism Mainnet or Celo Alfajores).
Generated: DETERMINISTIC_89b873d30f0fda8a
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies from React and Web3-React
import { useWeb3React } from "@web3-react/core";

/**
 * Function to check if a wallet is connected and retrieve the currently selected blockchain network.
 * @returns {Object} An object containing the connection status and network information.
 */
const getWalletStatusAndNetwork = () => {
  // Use the Web3React hook to access the active wallet and network context
  const { active, chainId, error, account } = useWeb3React();

  // Error handling: Return error information if there's an issue
  if (error) {
    return {
      connected: false,
      errorMessage: error.message,
      account: null,
      network: null,
    };
  }

  // If the wallet is not connected, return appropriate response
  if (!active) {
    return {
      connected: false,
      account: null,
      network: null,
    };
  }

  // Map chain IDs to human-readable blockchain network names
  const chainIdToNetworkMap = {
    10: "Optimism Mainnet",
    44787: "Celo Alfajores",
    // Add other chain IDs and networks as needed
  };

  // Get the network name based on the chainId
  const networkName = chainIdToNetworkMap[chainId] || "Unknown Network";

  // Return connection status and network details
  return {
    connected: true,
    account: account, // Wallet address
    network: networkName, // Human-readable network name
  };
};

export default getWalletStatusAndNetwork;
```
