"""
Generated Code Metadata:
========================
Original URL: https://pepewifhat.pages.dev
Prompt: Create a React component to display the user's PEPE WIF HAT NFT balance, mint price, and total supply, with a button to connect their wallet and mint an NFT.
Generated: DETERMINISTIC_d4be266bf7daf7bb
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// PEPEWIFHATNFT.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import PEPEWIFHATNFTContract from './PEPEWIFHATNFTContract.json';

const PEPEWIFHATNFT = () => {
  // Constants
  const CONTRACT_ADDRESS = '0x...'; // Replace with contract address
  const CONTRACT_ABI = PEPEWIFHATNFTContract.abi;

  // State variables
  const [balance, setBalance] = useState(0);
  const [mintPrice, setMintPrice] = useState(0);
  const [totalSupply, setTotalSupply] = useState(0);
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);

  // Connect wallet and initialize contract
  const connectWallet = async () => {
    try {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      setWeb3(provider);
      const signer = provider.getSigner();
      const contractInstance = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer);
      setContract(contractInstance);
      const accounts = await provider.listAccounts();
      setAccount(accounts[0]);
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  // Get user's NFT balance, mint price, and total supply
  const getNFTInfo = async () => {
    try {
      if (contract && account) {
        const balance = await contract.balanceOf(account);
        setBalance(balance.toNumber());
        const mintPrice = await contract.mintPrice();
        setMintPrice(mintPrice.toNumber());
        const totalSupply = await contract.totalSupply();
        setTotalSupply(totalSupply.toNumber());
      }
    } catch (error) {
      console.error('Error fetching NFT info:', error);
    }
  };

  // Mint NFT
  const mintNFT = async () => {
    try {
      if (contract) {
        const tx = await contract.mint({ value: mintPrice });
        await tx.wait();
        getNFTInfo();
      }
    } catch (error) {
      console.error('Error minting NFT:', error);
    }
  };

  // Update NFT info when account or contract changes
  useEffect(() => {
    getNFTInfo();
  }, [account, contract]);

  return (
    <div>
      <h1>PEPE WIF HAT NFT</h1>
      {account ? (
        <div>
          <p>Balance: {balance}</p>
          <p>Mint Price: {mintPrice}</p>
          <p>Total Supply: {totalSupply}</p>
          <button onClick={mintNFT}>Mint NFT</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default PEPEWIFHATNFT;
```

```json
// PEPEWIFHATNFTContract.json
{
  "abi": [
    {
      "inputs": [],
      "name": "balanceOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "mintPrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalSupply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "mint",
      "outputs": [],
      "payable": true,
      "stateMutability": "payable",
      "type": "function"
    }
  ]
}
```
