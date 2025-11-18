"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hypurrnft.org
Prompt: Suggest tools or frameworks to build an NFT minting portal that supports wallet connection and event-specific minting, referencing the Genesis Collection described on the Hypurr NFT Mint Portal.
Generated: DETERMINISTIC_505ed734eaa21e7a
Batch ID: 20250612_153854
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
import { ethers } from 'ethers';

// Define the main App component
const App = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [nftContract, setNftContract] = useState(null);
  const [mintingStatus, setMintingStatus] = useState('Not Minted');

  // Initialize Web3 and check for wallet connection
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
        
        // Request account access
        try {
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } catch (error) {
          console.error("Error connecting to wallet: ", error);
        }
      } else {
        console.error("MetaMask not detected");
      }
    };
    
    initWeb3();
  }, []);

  // Function to mint NFT
  const mintNFT = async (eventId) => {
    if (!web3 || !account || !nftContract) {
      console.error("Web3 is not initialized, or user is not connected.");
      return;
    }

    try {
      setMintingStatus('Minting...');
      
      // Call the mint function on the NFT contract
      const tx = await nftContract.methods.mint(account, eventId).send({ from: account });
      console.log('Transaction successful:', tx);
      setMintingStatus('Minted Successfully!');
    } catch (error) {
      console.error("Minting error: ", error);
      setMintingStatus('Minting Failed');
    }
  };

  // Load the NFT contract
  const loadContract = async () => {
    const contractAddress = '0xYourNFTContractAddress'; // Change to your contract address
    const abi = []; // Add your contract ABI here

    const nftInstance = new web3.eth.Contract(abi, contractAddress);
    setNftContract(nftInstance);
  };

  // Call loadContract on component mount
  useEffect(() => {
    if (web3) {
      loadContract();
    }
  }, [web3]);

  return (
    <div>
      <h1>NFT Minting Portal</h1>
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={() => mintNFT('event-specific-id')}>Mint NFT</button>
          <p>Status: {mintingStatus}</p>
        </div>
      ) : (
        <p>Please connect your wallet</p>
      )}
    </div>
  );
};

// Export the App component
export default App;
```
**Note:** Make sure to replace '0xYourNFTContractAddress' with the actual contract address and include the ABI for the NFT contract in the `abi` variable.
