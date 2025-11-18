"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Provide an example of using Web3 React to fetch and display the Chain ID and account balance of a connected wallet in a decentralized application.
Generated: DETERMINISTIC_a04a7e8734c3b3bf
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import React, { useState, useEffect } from "react";
import { useWeb3React } from "@web3-react/core";
import { InjectedConnector } from "@web3-react/injected-connector";

// Setup the injected connector for wallet connection
const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Mainnet, Ropsten, Rinkeby, Goerli, Kovan
});

const WalletInfo = () => {
  // Use Web3React hooks to manage wallet connection and blockchain data
  const { activate, active, account, library, chainId, deactivate } = useWeb3React();
  const [balance, setBalance] = useState(null);
  const [error, setError] = useState(null);

  // Function to connect the wallet
  const connectWallet = async () => {
    try {
      await activate(injected); // Activates the injected connector
      setError(null); // Clear any previous errors
    } catch (err) {
      setError("Failed to connect wallet. Please try again.");
    }
  };

  // Function to disconnect the wallet
  const disconnectWallet = () => {
    deactivate();
    setBalance(null);
    setError(null);
  };

  // Fetch account balance when account or library changes
  useEffect(() => {
    const fetchBalance = async () => {
      if (library && account) {
        try {
          const rawBalance = await library.getBalance(account); // Fetch raw balance
          const formattedBalance = parseFloat(library.utils.formatEther(rawBalance)); // Convert to Ether
          setBalance(formattedBalance); // Set the balance state
        } catch (err) {
          setError("Failed to fetch balance. Please try again.");
        }
      }
    };

    fetchBalance();
  }, [library, account]);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Decentralized Application</h1>
      {active ? (
        <div>
          <p><strong>Chain ID:</strong> {chainId}</p>
          <p><strong>Account:</strong> {account}</p>
          <p><strong>Balance:</strong> {balance !== null ? `${balance} ETH` : "Loading..."}</p>
          <button onClick={disconnectWallet} style={{ padding: "10px", marginTop: "10px", cursor: "pointer" }}>
            Disconnect Wallet
          </button>
        </div>
      ) : (
        <div>
          <button onClick={connectWallet} style={{ padding: "10px", cursor: "pointer" }}>
            Connect Wallet
          </button>
          {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
      )}
    </div>
  );
};

export default WalletInfo;
```
