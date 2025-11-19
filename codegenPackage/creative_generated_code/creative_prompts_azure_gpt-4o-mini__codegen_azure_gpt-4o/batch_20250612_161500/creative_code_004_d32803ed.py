"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phi-f1z.pages.dev
Prompt: What are the steps to build a dApp that utilizes the Phi Protocol for showcasing onchain credentials and NFTs?
Generated: DETERMINISTIC_d32803ed79392099
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready code example for building a decentralized application (dApp) using the Phi Protocol to showcase on-chain credentials and NFTs. This example assumes the use of JavaScript and a React-based frontend with Ethers.js for Ethereum interaction:

```javascript
// Import necessary dependencies
import React, { useEffect, useState } from "react";
import { ethers } from "ethers";
import "./App.css"; // Add custom styling if needed

// Phi Protocol smart contract ABI (example, replace with actual ABI)
const PHI_PROTOCOL_ABI = [
  // Replace with actual ABI definition
  {
    "constant": true,
    "inputs": [{ "name": "_address", "type": "address" }],
    "name": "getCredentials",
    "outputs": [{ "name": "", "type": "string[]" }],
    "type": "function",
  },
  {
    "constant": true,
    "inputs": [{ "name": "_address", "type": "address" }],
    "name": "getNFTs",
    "outputs": [{ "name": "", "type": "string[]" }],
    "type": "function",
  },
];

const PHI_PROTOCOL_ADDRESS = "0xYourPhiProtocolContractAddress"; // Replace with actual contract address

// Main App Component
function App() {
  const [account, setAccount] = useState(null);
  const [credentials, setCredentials] = useState([]);
  const [nfts, setNFTs] = useState([]);
  const [provider, setProvider] = useState(null);
  const [contract, setContract] = useState(null);

  // Connect wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        alert("Please install MetaMask!");
        return;
      }

      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await window.ethereum.request({
        method: "eth_requestAccounts",
      });

      setProvider(web3Provider);
      setAccount(accounts[0]);

      const phiContract = new ethers.Contract(
        PHI_PROTOCOL_ADDRESS,
        PHI_PROTOCOL_ABI,
        web3Provider
      );
      setContract(phiContract);
    } catch (error) {
      console.error("Error connecting wallet:", error);
      alert("Failed to connect wallet.");
    }
  };

  // Fetch credentials from Phi Protocol
  const fetchCredentials = async () => {
    try {
      if (!contract || !account) {
        alert("Connect wallet first.");
        return;
      }

      const credentialsData = await contract.getCredentials(account);
      setCredentials(credentialsData);
    } catch (error) {
      console.error("Error fetching credentials:", error);
      alert("Failed to retrieve credentials.");
    }
  };

  // Fetch NFTs from Phi Protocol
  const fetchNFTs = async () => {
    try {
      if (!contract || !account) {
        alert("Connect wallet first.");
        return;
      }

      const nftsData = await contract.getNFTs(account);
      setNFTs(nftsData);
    } catch (error) {
      console.error("Error fetching NFTs:", error);
      alert("Failed to retrieve NFTs.");
    }
  };

  // Auto-fetch data when account changes
  useEffect(() => {
    if (contract && account) {
      fetchCredentials();
      fetchNFTs();
    }
  }, [contract, account]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Phi Protocol dApp</h1>
        {!account ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <div>
            <p>Connected Account: {account}</p>
            <button onClick={fetchCredentials}>Fetch Credentials</button>
            <button onClick={fetchNFTs}>Fetch NFTs</button>
          </div>
        )}
        {credentials.length > 0 && (
          <div>
            <h2>Onchain Credentials</h2>
            <ul>
              {credentials.map((credential, index) => (
                <li key={index}>{credential}</li>
              ))}
            </ul>
          </div>
        )}
        {nfts.length > 0 && (
          <div>
            <h2>Showcased NFTs</h2>
            <ul>
              {nfts.map((nft, index) => (
                <li key={index}>{nft}</li>
              ))}
            </ul>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
```

### Notes:
1. Replace `PHI_PROTOCOL_ABI` with the actual ABI of the Phi Protocol smart contract.
2. Replace `PHI_PROTOCOL_ADDRESS` with the deployed address of the Phi Protocol contract.
3. Ensure dependencies (`ethers`, `react`, etc.) are installed via `npm install ethers react`.
4. Always test and validate the smart contract interactions locally and on testnets before deploying to production.
