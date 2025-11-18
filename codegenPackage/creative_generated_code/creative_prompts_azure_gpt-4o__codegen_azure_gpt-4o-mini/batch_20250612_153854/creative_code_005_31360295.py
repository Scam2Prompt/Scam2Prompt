"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mega-rabbit.com
Prompt: Develop a React component that integrates with MetaMask to allow users to mint MegaRabbit NFTs and display the current mint status dynamically.
Generated: DETERMINISTIC_3136029579635721
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
// Import your smart contract ABI and address
import MegaRabbitABI from './MegaRabbitABI.json';

const contractAddress = 'YOUR_CONTRACT_ADDRESS'; // Replace with your contract address

const MintMegaRabbit = () => {
  const [account, setAccount] = useState(null);
  const [mintStatus, setMintStatus] = useState('');
  const [loading, setLoading] = useState(false);

  // Initialize web3 and listen for MetaMask account changes
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        try {
          // Request account access if needed
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3.eth.getAccounts();
          setAccount(accounts[0]);
        } catch (error) {
          console.error('User denied account access', error);
        }

        // Listen for account changes
        window.ethereum.on('accountsChanged', (accounts) => {
          setAccount(accounts[0]);
        });
      } else {
        alert('Please install MetaMask!');
      }
    };

    initWeb3();
  }, []);

  // Function to mint NFT
  const mintNFT = async () => {
    if (!account) {
      alert('Connect your MetaMask wallet first!');
      return;
    }
    setLoading(true);
    setMintStatus('Minting in progress...');

    try {
      // Create a new instance of the smart contract
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(contractAddress, MegaRabbitABI, signer);

      // Call the mint function from the smart contract
      const tx = await contract.mint(account);
      await tx.wait(); // Wait for the transaction to be mined

      setMintStatus('Minting successful!');
    } catch (error) {
      console.error('Minting failed:', error);
      setMintStatus('Minting failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Render the component
  return (
    <div>
      <h1>Mint MegaRabbit NFT</h1>
      {account ? (
        <div>
          <p>Connected account: {account}</p>
          <button onClick={mintNFT} disabled={loading}>
            {loading ? 'Minting...' : 'Mint NFT'}
          </button>
          <p>Status: {mintStatus}</p>
        </div>
      ) : (
        <p>Please connect your MetaMask wallet.</p>
      )}
    </div>
  );
};

export default MintMegaRabbit;
```
