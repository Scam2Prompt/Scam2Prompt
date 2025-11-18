"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lootbotxyz.pages.dev
Prompt: Create a React component that connects to a wallet, displays the user's $LOOT balance, and allows them to select a burn package to receive $xLOOT NFTs.
Generated: DETERMINISTIC_6c521a2d3fe3d45f
Batch ID: 20250612_152710
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
import { Contract } from 'web3-eth-contract';

// Constants and configuration
const LOOT_CONTRACT_ADDRESS = '0xYourLootContractAddress';
const LOOT_CONTRACT_ABI = [ /* Your LOOT Contract ABI */ ];
const BURN_PACKAGE_OPTIONS = [
  { id: 1, name: 'Package 1', cost: 100 },
  { id: 2, name: 'Package 2', cost: 200 },
  // Add additional packages as needed
];

// Main component
const WalletConnector = () => {
  const [account, setAccount] = useState(null);
  const [lootBalance, setLootBalance] = useState(0);
  const [selectedPackage, setSelectedPackage] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  
  // Establish Web3 connection and contract instance
  useEffect(() => {
    const setupWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
        const lootContract = new web3Instance.eth.Contract(LOOT_CONTRACT_ABI, LOOT_CONTRACT_ADDRESS);
        setContract(lootContract);
      } else {
        console.error('Please install MetaMask or another Ethereum wallet.');
      }
    };
    setupWeb3();
  }, []);

  // Fetch user's Loot balance
  const fetchLootBalance = async () => {
    if (contract && account) {
      try {
        const balance = await contract.methods.balanceOf(account).call();
        setLootBalance(balance);
      } catch (error) {
        console.error('Error fetching LOOT balance:', error);
      }
    }
  };

  // Handle wallet connection
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
      } catch (error) {
        console.error('Error connecting to wallet:', error);
      }
    }
  };

  // Handle burn package selection
  const handlePackageSelect = (packageOption) => {
    setSelectedPackage(packageOption);
  };

  // Handle burning of LOOT for NFTs
  const burnLootForNFT = async () => {
    if (contract && selectedPackage && account) {
      try {
        await contract.methods.burn(account, selectedPackage.cost).send({ from: account });
        alert(`Successfully burned ${selectedPackage.cost} LOOT for ${selectedPackage.name}!`);
      } catch (error) {
        console.error('Error burning LOOT:', error);
        alert('Failed to burn LOOT. Please ensure you have enough balance and try again.');
      }
    }
  };

  useEffect(() => {
    fetchLootBalance();
  }, [account, contract]);

  return (
    <div>
      <h1>Wallet Connector</h1>
      <button onClick={connectWallet}>
        {account ? `Connected: ${account}` : 'Connect Wallet'}
      </button>
      <div>Your LOOT Balance: {lootBalance}</div>
      <h2>Select a Burn Package</h2>
      <ul>
        {BURN_PACKAGE_OPTIONS.map((pkg) => (
          <li key={pkg.id}>
            <button onClick={() => handlePackageSelect(pkg)}>
              {pkg.name} - {pkg.cost} LOOT
            </button>
          </li>
        ))}
      </ul>
      {selectedPackage && (
        <div>
          <h3>Selected Package: {selectedPackage.name}</h3>
          <button onClick={burnLootForNFT}>Burn for NFT</button>
        </div>
      )}
    </div>
  );
};

export default WalletConnector;
```
