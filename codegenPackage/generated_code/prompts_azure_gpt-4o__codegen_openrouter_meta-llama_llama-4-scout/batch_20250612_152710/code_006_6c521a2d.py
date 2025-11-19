"""
Generated Code Metadata:
========================
Original URL: https://lootbotxyz.pages.dev
Prompt: Create a React component that connects to a wallet, displays the user's $LOOT balance, and allows them to select a burn package to receive $xLOOT NFTs.
Generated: DETERMINISTIC_6c521a2d3fe3d45f
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// LootBurner.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import LootBurnerContract from './LootBurnerContract.json';
import LootTokenContract from './LootTokenContract.json';

const LootBurner = () => {
  // Web3 and contract setup
  const web3 = new Web3(window.ethereum);
  const lootBurnerContractAddress = '0x...'; // Replace with deployed contract address
  const lootTokenContractAddress = '0x...'; // Replace with deployed contract address

  const lootBurnerContract = new web3.eth.Contract(LootBurnerContract.abi, lootBurnerContractAddress);
  const lootTokenContract = new web3.eth.Contract(LootTokenContract.abi, lootTokenContractAddress);

  // State variables
  const [account, setAccount] = useState(null);
  const [lootBalance, setLootBalance] = useState(0);
  const [burnPackages, setBurnPackages] = useState([]);
  const [selectedPackage, setSelectedPackage] = useState(null);
  const [error, setError] = useState(null);

  // Connect to wallet and fetch user data
  const connectWallet = async () => {
    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
    } catch (error) {
      setError('Failed to connect to wallet');
      console.error(error);
    }
  };

  useEffect(() => {
    if (account) {
      fetchLootBalance();
      fetchBurnPackages();
    }
  }, [account]);

  // Fetch user's $LOOT balance
  const fetchLootBalance = async () => {
    try {
      const balance = await lootTokenContract.methods.balanceOf(account).call();
      setLootBalance(ethers.utils.formatEther(balance));
    } catch (error) {
      setError('Failed to fetch $LOOT balance');
      console.error(error);
    }
  };

  // Fetch available burn packages
  const fetchBurnPackages = async () => {
    try {
      const packages = await lootBurnerContract.methods.getBurnPackages().call();
      setBurnPackages(packages);
    } catch (error) {
      setError('Failed to fetch burn packages');
      console.error(error);
    }
  };

  // Handle package selection
  const handlePackageSelect = (pkg) => {
    setSelectedPackage(pkg);
  };

  // Handle burn submission
  const handleBurnSubmit = async () => {
    try {
      if (!selectedPackage) {
        setError('Please select a burn package');
        return;
      }

      const tx = await lootBurnerContract.methods.burnLoot(selectedPackage).send({ from: account });
      console.log(tx);
      fetchLootBalance();
    } catch (error) {
      setError('Failed to submit burn transaction');
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Loot Burner</h1>
      {account ? (
        <div>
          <p>Account: {account}</p>
          <p>$LOOT Balance: {lootBalance}</p>
          <h2>Burn Packages:</h2>
          <ul>
            {burnPackages.map((pkg, index) => (
              <li key={index}>
                <input
                  type="radio"
                  name="package"
                  value={index}
                  checked={selectedPackage === index}
                  onChange={() => handlePackageSelect(index)}
                />
                <span>Package {index + 1} - {pkg.lootRequired} $LOOT</span>
              </li>
            ))}
          </ul>
          <button onClick={handleBurnSubmit}>Burn $LOOT</button>
          {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default LootBurner;
```

```json
// LootBurnerContract.json
{
  "abi": [
    {
      "inputs": [],
      "name": "getBurnPackages",
      "outputs": [
        {
          "internalType": "struct LootBurner.BurnPackage[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_package",
          "type": "uint256"
        }
      ],
      "name": "burnLoot",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]
}
```

```json
// LootTokenContract.json
{
  "abi": [
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        }
      ],
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
    }
  ]
}
```
