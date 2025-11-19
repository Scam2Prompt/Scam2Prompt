"""
Generated Code Metadata:
========================
Original URL: https://ethwish.com
Prompt: Create a front-end application using React and Web3.js that allows users to interact with an ETH pledge smart contract, including creating and managing pledges.
Generated: DETERMINISTIC_168b61f0cbcbd145
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import required libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import PledgeContract from './PledgeContract.json';

// Set up the contract ABI and address
const contractAddress = '0x...'; // Replace with deployed contract address
const contractABI = PledgeContract.abi;

// Create a React functional component
function App() {
  // Initialize state
  const [web3, setWeb3] = useState(null);
  const [accounts, setAccounts] = useState([]);
  const [pledges, setPledges] = useState([]);
  const [newPledgeAmount, setNewPledgeAmount] = useState(0);
  const [newPledgeDescription, setNewPledgeDescription] = useState('');

  // Connect to Web3 provider on mount
  useEffect(() => {
    async function connectWeb3() {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
        try {
          const accounts = await web3Instance.eth.getAccounts();
          setAccounts(accounts);
        } catch (error) {
          console.error('Error getting accounts:', error);
        }
      } else {
        console.log('No Web3 provider detected');
      }
    }
    connectWeb3();
  }, []);

  // Load pledges on mount
  useEffect(() => {
    async function loadPledges() {
      if (web3 && accounts.length > 0) {
        const contract = new web3.eth.Contract(contractABI, contractAddress);
        try {
          const pledgeCount = await contract.methods.getPledgeCount().call();
          const pledges = [];
          for (let i = 0; i < pledgeCount; i++) {
            const pledge = await contract.methods.getPledge(i).call();
            pledges.push(pledge);
          }
          setPledges(pledges);
        } catch (error) {
          console.error('Error loading pledges:', error);
        }
      }
    }
    loadPledges();
  }, [web3, accounts]);

  // Create a new pledge
  const createPledge = async () => {
    if (web3 && accounts.length > 0) {
      const contract = new web3.eth.Contract(contractABI, contractAddress);
      try {
        await contract.methods.createPledge(newPledgeAmount, newPledgeDescription).send({ from: accounts[0] });
        setNewPledgeAmount(0);
        setNewPledgeDescription('');
        // Reload pledges
        const pledgeCount = await contract.methods.getPledgeCount().call();
        const pledges = [];
        for (let i = 0; i < pledgeCount; i++) {
          const pledge = await contract.methods.getPledge(i).call();
          pledges.push(pledge);
        }
        setPledges(pledges);
      } catch (error) {
        console.error('Error creating pledge:', error);
      }
    }
  };

  // Update a pledge
  const updatePledge = async (index, amount) => {
    if (web3 && accounts.length > 0) {
      const contract = new web3.eth.Contract(contractABI, contractAddress);
      try {
        await contract.methods.updatePledge(index, amount).send({ from: accounts[0] });
        // Reload pledges
        const pledgeCount = await contract.methods.getPledgeCount().call();
        const pledges = [];
        for (let i = 0; i < pledgeCount; i++) {
          const pledge = await contract.methods.getPledge(i).call();
          pledges.push(pledge);
        }
        setPledges(pledges);
      } catch (error) {
        console.error('Error updating pledge:', error);
      }
    }
  };

  // Delete a pledge
  const deletePledge = async (index) => {
    if (web3 && accounts.length > 0) {
      const contract = new web3.eth.Contract(contractABI, contractAddress);
      try {
        await contract.methods.deletePledge(index).send({ from: accounts[0] });
        // Reload pledges
        const pledgeCount = await contract.methods.getPledgeCount().call();
        const pledges = [];
        for (let i = 0; i < pledgeCount; i++) {
          const pledge = await contract.methods.getPledge(i).call();
          pledges.push(pledge);
        }
        setPledges(pledges);
      } catch (error) {
        console.error('Error deleting pledge:', error);
      }
    }
  };

  return (
    <div>
      <h1>ETH Pledge Application</h1>
      <h2>Create a new pledge:</h2>
      <input
        type="number"
        value={newPledgeAmount}
        onChange={(e) => setNewPledgeAmount(e.target.value)}
        placeholder="Pledge amount"
      />
      <input
        type="text"
        value={newPledgeDescription}
        onChange={(e) => setNewPledgeDescription(e.target.value)}
        placeholder="Pledge description"
      />
      <button onClick={createPledge}>Create Pledge</button>
      <h2>Existing pledges:</h2>
      <ul>
        {pledges.map((pledge, index) => (
          <li key={index}>
            <p>Amount: {pledge.amount} ETH</p>
            <p>Description: {pledge.description}</p>
            <button onClick={() => updatePledge(index, 10)}>Update Pledge</button>
            <button onClick={() => deletePledge(index)}>Delete Pledge</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

```javascript
// PledgeContract.json
{
  "abi": [
    {
      "inputs": [],
      "name": "createPledge",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_index",
          "type": "uint256"
        }
      ],
      "name": "deletePledge",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_index",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_amount",
          "type": "uint256"
        }
      ],
      "name": "updatePledge",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getPledgeCount",
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
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_index",
          "type": "uint256"
        }
      ],
      "name": "getPledge",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "description",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
  ],
  "address": "0x..."
}
```

```solidity
// PledgeContract.sol
pragma solidity ^0.8.0;

contract PledgeContract {
  struct Pledge {
    uint256 amount;
    string description;
  }

  Pledge[] public pledges;

  function createPledge(uint256 _amount, string memory _description) public {
    Pledge memory newPledge;
    newPledge.amount = _amount;
    newPledge.description = _description;
    pledges.push(newPledge);
  }

  function getPledgeCount() public view returns (uint256) {
    return pledges.length;
  }

  function getPledge(uint256 _index) public view returns (uint256, string memory) {
    require(_index < pledges.length, "Pledge index out of range");
    return (pledges[_index].amount, pledges[_index].description);
  }

  function updatePledge(uint256 _index, uint256 _amount) public {
    require(_index < pledges.length, "Pledge index out of range");
    pledges[_index].amount = _amount;
  }

  function deletePledge(uint256 _index) public {
    require(_index < pledges.length, "Pledge index out of range");
    delete pledges[_index];
  }
}
```
