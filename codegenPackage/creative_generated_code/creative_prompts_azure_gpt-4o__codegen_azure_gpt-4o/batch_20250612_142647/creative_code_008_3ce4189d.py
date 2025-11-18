"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-zerolend.web.app
Prompt: Write code to integrate a wallet connection feature for ZeroLend's dApp, ensuring compatibility with the dashboard and markets.
Generated: DETERMINISTIC_3ce4189d197cb838
Batch ID: 20250612_142647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages
import { useEffect, useState } from "react";
import { ethers } from "ethers";

// Constants
const ZERO_LEND_CONTRACT_ADDRESS = "0xYourZeroLendContractAddressHere"; // Replace with actual contract address
const ZERO_LEND_ABI = [
  // Replace with ZeroLend's ABI (Application Binary Interface)
];

// Wallet Connection Component
function WalletConnector() {
  // State variables
  const [walletAddress, setWalletAddress] = useState(null);
  const [provider, setProvider] = useState(null);
  const [zeroLendContract, setZeroLendContract] = useState(null);

  // Initialize wallet connection
  const connectWallet = async () => {
    try {
      // Check if MetaMask or any provider is available
      if (!window.ethereum) throw new Error("No Ethereum provider found");

      // Request account access
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

      // Set the wallet address
      setWalletAddress(accounts[0]);

      // Create an ethers provider
      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      setProvider(web3Provider);

      // Attach the ZeroLend contract instance
      const contract = new ethers.Contract(ZERO_LEND_CONTRACT_ADDRESS, ZERO_LEND_ABI, web3Provider.getSigner());
      setZeroLendContract(contract);
    } catch (error) {
      console.error("Error connecting wallet:", error.message);
      alert("Failed to connect wallet. Please try again.");
    }
  };

  // Disconnect wallet
  const disconnectWallet = () => {
    setWalletAddress(null);
    setProvider(null);
    setZeroLendContract(null);
    alert("Wallet disconnected successfully!");
  };

  // Display wallet address or connection button
  const renderConnectionStatus = () => {
    if (walletAddress) {
      return (
        <div>
          <p>Connected Wallet: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      );
    } else {
      return <button onClick={connectWallet}>Connect Wallet</button>;
    }
  };

  // Detect account changes (e.g., user switches accounts)
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on("accountsChanged", (accounts) => {
        if (accounts.length > 0) {
          setWalletAddress(accounts[0]);
        } else {
          disconnectWallet();
        }
      });
    }
    // Cleanup listener on component unmount
    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener("accountsChanged", () => {});
      }
    };
  }, []);

  // Render
  return (
    <div>
      <h1>ZeroLend Wallet Connection</h1>
      <div>{renderConnectionStatus()}</div>
    </div>
  );
}

export default WalletConnector;
```
