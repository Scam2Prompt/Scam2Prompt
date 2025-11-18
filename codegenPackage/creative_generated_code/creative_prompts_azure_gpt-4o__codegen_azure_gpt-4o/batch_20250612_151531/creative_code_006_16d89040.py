"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sealanapresales.pages.dev
Prompt: Create a React component for a widget that connects a self-custody wallet to purchase $SEAL tokens, using the features highlighted on the Sealana Presale webpage.
Generated: DETERMINISTIC_16d89040f011e9d0
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Importing necessary modules and libraries
import React, { useState } from "react";
import Web3 from "web3"; // Library for Ethereum blockchain connection
import { toast } from "react-toastify"; // Notification library for user feedback
import "react-toastify/dist/ReactToastify.css"; // Relevant styles for toast notifications

// React component for connecting wallet and purchasing $SEAL tokens
const SealanaTokenWidget = () => {
  // State variables for managing wallet connection and token purchase
  const [walletAddress, setWalletAddress] = useState(null);
  const [isWalletConnected, setIsWalletConnected] = useState(false);
  const [loading, setLoading] = useState(false);

  // Function to connect a self-custody wallet
  const connectWallet = async () => {
    try {
      // Check if the browser supports Ethereum wallets
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum); // Create Web3 instance
        await window.ethereum.request({ method: "eth_requestAccounts" }); // Request wallet connection
        const accounts = await web3.eth.getAccounts(); // Get user's wallet account
        setWalletAddress(accounts[0]); // Set wallet address in state
        setIsWalletConnected(true); // Update wallet connection status
        toast.success("Wallet connected successfully!"); // Show success notification
      } else {
        toast.error("Ethereum wallet not detected. Please install MetaMask or similar."); // Error message for missing wallet
      }
    } catch (error) {
      console.error("Error connecting wallet:", error); // Log error details
      toast.error("Failed to connect wallet. Please try again."); // Error notification
    }
  };

  // Function to purchase $SEAL tokens
  const purchaseSealTokens = async () => {
    try {
      if (!isWalletConnected || !walletAddress) {
        toast.warn("Please connect your wallet first."); // Warn if wallet is not connected
        return;
      }

      setLoading(true); // Indicate loading state

      // Example transaction details for purchasing $SEAL tokens
      const web3 = new Web3(window.ethereum);
      const transactionParameters = {
        to: "0xSealTokenContractAddressHere", // Replace with the actual $SEAL token contract address
        from: walletAddress, // Send from connected wallet address
        value: web3.utils.toHex(web3.utils.toWei("0.1", "ether")), // Replace with actual token price in ETH
      };

      // Sending transaction using user's wallet
      await window.ethereum.request({
        method: "eth_sendTransaction",
        params: [transactionParameters],
      });

      toast.success("Purchase successful! $SEAL tokens will arrive shortly."); // Success message
    } catch (error) {
      console.error("Error purchasing tokens:", error); // Log error details
      toast.error("Transaction failed. Please try again."); // Error notification
    } finally {
      setLoading(false); // Reset loading state
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "400px", margin: "auto" }}>
      {/* Header */}
      <h2>Sealana Presale Widget</h2>

      {/* Wallet connection button */}
      {!isWalletConnected ? (
        <button onClick={connectWallet} style={{ margin: "10px 0", padding: "10px", cursor: "pointer" }}>
          Connect Wallet
        </button>
      ) : (
        <p>Wallet Connected: {walletAddress}</p>
      )}

      {/* $SEAL token purchase button */}
      <button
        onClick={purchaseSealTokens}
        style={{ padding: "10px", cursor: "pointer" }}
        disabled={!isWalletConnected || loading} // Disable button during loading or if wallet is not connected
      >
        {loading ? "Processing..." : "Purchase $SEAL Tokens"}
      </button>

      {/* Footer */}
      <p style={{ marginTop: "20px", fontSize: "0.9em", color: "gray" }}>
        Please ensure you have sufficient ETH balance for the purchase and gas fees.
      </p>
    </div>
  );
};

export default SealanaTokenWidget;
```

**Note:** Replace `"0xSealTokenContractAddressHere"` with the actual $SEAL token contract address. Integrate further security measures or API endpoints if required for production environments.
