"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rockycoinbase.pages.dev
Prompt: Create a web interface using React.js that allows users to connect their wallet, check eligibility, and claim $ROCKY token airdrops, as described on the Rocky on Base website.
Generated: DETERMINISTIC_a95ec753708a1a0f
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import './App.css'; // Assume there is an accompanying CSS file for styling

// Constants
const CONTRACT_ADDRESS = "<SMART_CONTRACT_ADDRESS>"; // Replace with actual smart contract address
const ABI = [...] // Replace with the ABI of the smart contract
const TOKEN_NAME = "$ROCKY";
const AIRDROP_EVENT = "ClaimAirdrop";

const App = () => {
  // State variables
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [isEligible, setIsEligible] = useState(false);
  const [eligibilityMessage, setEligibilityMessage] = useState("");
  const [loading, setLoading] = useState(false);

  // Connect wallet handler
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const provider = window.ethereum;
        const web3Instance = new Web3(provider);
        setWeb3(web3Instance);

        const accounts = await web3Instance.eth.requestAccounts();
        setAccount(accounts[0]);
      } else {
        alert("Please install MetaMask or another Ethereum-compatible wallet.");
      }
    } catch (error) {
      console.error("Error connecting wallet:", error);
      alert("Failed to connect wallet. Please try again.");
    }
  };

  // Check eligibility handler
  const checkEligibility = async () => {
    if (!web3 || !account) {
      alert("Please connect your wallet first.");
      return;
    }

    try {
      setLoading(true);
      const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);
      const eligible = await contract.methods.isEligible(account).call(); // Assume `isEligible` is a smart contract method
      setIsEligible(eligible);

      setEligibilityMessage(
        eligible
          ? `Congratulations! You are eligible to claim the ${TOKEN_NAME} airdrop!`
          : `Unfortunately, you are not eligible for the ${TOKEN_NAME} airdrop.`
      );
    } catch (error) {
      console.error("Error checking eligibility:", error);
      alert("Failed to check eligibility. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  // Claim airdrop handler
  const claimAirdrop = async () => {
    if (!web3 || !account) {
      alert("Please connect your wallet first.");
      return;
    }

    if (!isEligible) {
      alert("You are not eligible to claim the airdrop.");
      return;
    }

    try {
      setLoading(true);
      const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);
      await contract.methods.claimAirdrop().send({ from: account }); // Assume `claimAirdrop` is a smart contract method

      alert(`Successfully claimed your ${TOKEN_NAME} tokens!`);
    } catch (error) {
      console.error("Error claiming airdrop:", error);
      alert("Failed to claim airdrop. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  // Render the UI
  return (
    <div className="App">
      <header className="App-header">
        <h1>Rocky on Base - {TOKEN_NAME} Airdrop</h1>
      </header>

      <main>
        {!account ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <>
            <p>Connected Wallet: {account}</p>
            <button onClick={checkEligibility} disabled={loading}>
              {loading ? "Checking..." : "Check Eligibility"}
            </button>
            {eligibilityMessage && <p>{eligibilityMessage}</p>}
            {isEligible && (
              <button onClick={claimAirdrop} disabled={loading}>
                {loading ? "Claiming..." : "Claim Airdrop"}
              </button>
            )}
          </>
        )}
      </main>

      <footer>
        <p>Powered by Rocky on Base</p>
      </footer>
    </div>
  );
};

export default App;
```
