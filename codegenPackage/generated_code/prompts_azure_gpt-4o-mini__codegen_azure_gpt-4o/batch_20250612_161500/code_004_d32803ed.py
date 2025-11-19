"""
Generated Code Metadata:
========================
Original URL: https://phi-f1z.pages.dev
Prompt: What are the steps to build a dApp that utilizes the Phi Protocol for showcasing onchain credentials and NFTs?
Generated: DETERMINISTIC_d32803ed79392099
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready code example for building a decentralized application (dApp) that utilizes the Phi Protocol to showcase on-chain credentials and NFTs. The code is written in JavaScript/TypeScript using the React framework and ethers.js for Ethereum interaction.

```typescript
// Import necessary libraries
import React, { useState, useEffect } from "react";
import { ethers } from "ethers";
import { PhiProtocol } from "phi-protocol-sdk"; // Hypothetical SDK for Phi Protocol
import "./App.css"; // Import styles

// Define constants
const PHI_CONTRACT_ADDRESS = "0xYourPhiProtocolContractAddress"; // Replace with actual contract address
const PHI_ABI = [
  // Replace with the actual ABI of the Phi Protocol contract
  {
    "constant": true,
    "inputs": [{ "name": "user", "type": "address" }],
    "name": "getCredentials",
    "outputs": [{ "name": "", "type": "string[]" }],
    "type": "function",
  },
  {
    "constant": true,
    "inputs": [{ "name": "user", "type": "address" }],
    "name": "getNFTs",
    "outputs": [{ "name": "", "type": "string[]" }],
    "type": "function",
  },
];

function App() {
  const [provider, setProvider] = useState<ethers.providers.Web3Provider | null>(null);
  const [signer, setSigner] = useState<ethers.Signer | null>(null);
  const [credentials, setCredentials] = useState<string[]>([]);
  const [nfts, setNFTs] = useState<string[]>([]);
  const [userAddress, setUserAddress] = useState<string>("");

  // Initialize Ethereum provider
  useEffect(() => {
    const initProvider = async () => {
      if (window.ethereum) {
        try {
          const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(web3Provider);
          const signer = web3Provider.getSigner();
          setSigner(signer);
          const address = await signer.getAddress();
          setUserAddress(address);
        } catch (error) {
          console.error("Error initializing provider:", error);
        }
      } else {
        console.error("Ethereum provider not found. Please install MetaMask.");
      }
    };

    initProvider();
  }, []);

  // Fetch on-chain credentials and NFTs
  const fetchData = async () => {
    if (!provider || !signer || !userAddress) {
      console.error("Provider, signer, or user address is not initialized.");
      return;
    }

    try {
      const phiContract = new ethers.Contract(PHI_CONTRACT_ADDRESS, PHI_ABI, signer);

      // Fetch credentials
      const userCredentials = await phiContract.getCredentials(userAddress);
      setCredentials(userCredentials);

      // Fetch NFTs
      const userNFTs = await phiContract.getNFTs(userAddress);
      setNFTs(userNFTs);
    } catch (error) {
      console.error("Error fetching data from Phi Protocol:", error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Phi Protocol dApp</h1>
        <p>Showcasing On-Chain Credentials and NFTs</p>
        {userAddress ? (
          <p>Connected Wallet: {userAddress}</p>
        ) : (
          <p>Please connect your wallet.</p>
        )}
        <button onClick={fetchData}>Fetch Data</button>
        <div>
          <h2>On-Chain Credentials</h2>
          {credentials.length > 0 ? (
            <ul>
              {credentials.map((credential, index) => (
                <li key={index}>{credential}</li>
              ))}
            </ul>
          ) : (
            <p>No credentials found.</p>
          )}
        </div>
        <div>
          <h2>NFTs</h2>
          {nfts.length > 0 ? (
            <ul>
              {nfts.map((nft, index) => (
                <li key={index}>{nft}</li>
              ))}
            </ul>
          ) : (
            <p>No NFTs found.</p>
          )}
        </div>
      </header>
    </div>
  );
}

export default App;
```

### Notes:
1. Replace `PHI_CONTRACT_ADDRESS` and `PHI_ABI` with the actual contract address and ABI of the Phi Protocol.
2. Ensure the `phi-protocol-sdk` is installed or replace it with the appropriate SDK/library for interacting with the Phi Protocol.
3. Add proper styling in `App.css` for a polished UI.
4. Test the dApp thoroughly in different environments before deploying to production.
