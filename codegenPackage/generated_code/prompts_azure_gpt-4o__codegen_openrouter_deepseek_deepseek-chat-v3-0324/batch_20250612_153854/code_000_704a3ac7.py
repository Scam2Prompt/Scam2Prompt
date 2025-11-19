"""
Generated Code Metadata:
========================
Original URL: https://hypurrnft.org
Prompt: Write code to integrate a wallet connection feature for an NFT minting portal, referencing the Genesis Collection and minting process described on the Hypurr NFT Mint Portal.
Generated: DETERMINISTIC_704a3ac7389bfe07
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { ethers } from 'ethers';
import { useState, useEffect } from 'react';
import Web3Modal from 'web3modal';

// NFT Contract ABI (simplified for example)
const NFT_CONTRACT_ABI = [
  {
    "inputs": [],
    "name": "mint",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "totalSupply",
    "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
    "stateMutability": "view",
    "type": "function"
  }
];

// Contract address for the Genesis Collection
const NFT_CONTRACT_ADDRESS = "0x..."; // Replace with actual contract address

export default function NFTMintPortal() {
  const [walletConnected, setWalletConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState("");
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [contract, setContract] = useState(null);
  const [minting, setMinting] = useState(false);
  const [mintStatus, setMintStatus] = useState("");
  const [totalMinted, setTotalMinted] = useState(0);

  // Initialize Web3Modal
  const web3Modal = new Web3Modal({
    network: "mainnet", // Change to appropriate network
    cacheProvider: true,
    providerOptions: {}
  });

  // Connect wallet function
  const connectWallet = async () => {
    try {
      const instance = await web3Modal.connect();
      const provider = new ethers.providers.Web3Provider(instance);
      const signer = provider.getSigner();
      const address = await signer.getAddress();

      setProvider(provider);
      setSigner(signer);
      setWalletAddress(address);
      setWalletConnected(true);

      // Initialize contract
      const contract = new ethers.Contract(
        NFT_CONTRACT_ADDRESS,
        NFT_CONTRACT_ABI,
        signer
      );
      setContract(contract);

      // Listen for account changes
      instance.on("accountsChanged", (accounts) => {
        if (accounts.length === 0) {
          resetWalletConnection();
        } else {
          setWalletAddress(accounts[0]);
        }
      });

      // Listen for chain changes
      instance.on("chainChanged", () => {
        window.location.reload();
      });

      // Get initial total supply
      updateTotalSupply();
    } catch (err) {
      console.error("Wallet connection error:", err);
      setMintStatus("Failed to connect wallet");
    }
  };

  // Reset wallet connection
  const resetWalletConnection = () => {
    setWalletConnected(false);
    setWalletAddress("");
    setProvider(null);
    setSigner(null);
    setContract(null);
  };

  // Update total supply from contract
  const updateTotalSupply = async () => {
    if (!contract) return;
    try {
      const supply = await contract.totalSupply();
      setTotalMinted(supply.toNumber());
    } catch (err) {
      console.error("Error fetching total supply:", err);
    }
  };

  // Mint NFT function
  const mintNFT = async () => {
    if (!contract || !walletConnected) return;
    
    setMinting(true);
    setMintStatus("Minting in progress...");
    
    try {
      const tx = await contract.mint({
        value: ethers.utils.parseEther("0.08") // Example mint price
      });
      
      setMintStatus("Transaction sent. Waiting for confirmation...");
      await tx.wait();
      
      setMintStatus("Mint successful!");
      updateTotalSupply();
    } catch (err) {
      console.error("Minting error:", err);
      setMintStatus("Mint failed. Please try again.");
    } finally {
      setMinting(false);
    }
  };

  // Check if wallet is already connected on component mount
  useEffect(() => {
    if (web3Modal.cachedProvider) {
      connectWallet();
    }
  }, []);

  return (
    <div className="nft-mint-portal">
      <h1>Hypurr NFT Mint Portal</h1>
      <h2>Genesis Collection</h2>
      
      {!walletConnected ? (
        <button onClick={connectWallet} className="connect-wallet-btn">
          Connect Wallet
        </button>
      ) : (
        <div className="wallet-info">
          <p>Connected: {walletAddress.substring(0, 6)}...{walletAddress.substring(walletAddress.length - 4)}</p>
          <p>Total Minted: {totalMinted}</p>
          
          <button 
            onClick={mintNFT} 
            disabled={minting}
            className="mint-btn"
          >
            {minting ? "Minting..." : "Mint NFT"}
          </button>
          
          {mintStatus && <p className="status">{mintStatus}</p>}
        </div>
      )}
    </div>
  );
}
```
