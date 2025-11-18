"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Develop a web application using React and web3.js to display NFT minting progress and pledge completion status, similar to the Clone Force™ platform.
Generated: DETERMINISTIC_abcad146173e3045
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import './App.css'; // CSS for styling the application

const App = () => {
  // State variables
  const [account, setAccount] = useState(null); // User's wallet address
  const [contract, setContract] = useState(null); // Smart contract instance
  const [mintingProgress, setMintingProgress] = useState(0); // NFT minting progress
  const [pledgeStatus, setPledgeStatus] = useState(false); // Pledge completion status
  const [loading, setLoading] = useState(true); // Loading state

  // Smart contract ABI and address (replace with actual values)
  const contractABI = [
    // Example ABI
    {
      constant: true,
      inputs: [],
      name: 'getMintingProgress',
      outputs: [{ name: '', type: 'uint256' }],
      payable: false,
      stateMutability: 'view',
      type: 'function',
    },
    {
      constant: true,
      inputs: [],
      name: 'isPledgeCompleted',
      outputs: [{ name: '', type: 'bool' }],
      payable: false,
      stateMutability: 'view',
      type: 'function',
    },
  ];
  const contractAddress = '0xYourContractAddressHere';

  // Initialize Web3 and connect to the blockchain
  useEffect(() => {
    const initBlockchainConnection = async () => {
      try {
        if (window.ethereum) {
          const web3 = new Web3(window.ethereum);
          await window.ethereum.enable(); // Request wallet connection
          const accounts = await web3.eth.getAccounts(); // Get user accounts
          setAccount(accounts[0]); // Set the first account as active
          const instance = new web3.eth.Contract(contractABI, contractAddress);
          setContract(instance);
        } else {
          alert('Please install MetaMask to use this application.');
        }
      } catch (error) {
        console.error('Error connecting to blockchain:', error);
        alert('Failed to connect to blockchain.');
      }
    };

    initBlockchainConnection();
  }, []);

  // Fetch minting progress and pledge status from the smart contract
  useEffect(() => {
    const fetchContractData = async () => {
      if (contract && account) {
        try {
          const progress = await contract.methods.getMintingProgress().call();
          const pledgeCompleted = await contract.methods.isPledgeCompleted().call();
          setMintingProgress(progress);
          setPledgeStatus(pledgeCompleted);
        } catch (error) {
          console.error('Error fetching contract data:', error);
        } finally {
          setLoading(false); // Data fetching is complete
        }
      }
    };

    fetchContractData();
  }, [contract, account]);

  // Render the application
  return (
    <div className="App">
      <header className="App-header">
        <h1>NFT Minting Progress & Pledge Status</h1>
        {loading ? (
          <p>Loading data from blockchain...</p>
        ) : (
          <div>
            <p>
              <strong>Wallet Address:</strong> {account || 'Not connected'}
            </p>
            <p>
              <strong>Minting Progress:</strong> {mintingProgress} NFTs minted
            </p>
            <p>
              <strong>Pledge Status:</strong> {pledgeStatus ? 'Completed' : 'Incomplete'}
            </p>
          </div>
        )}
      </header>
    </div>
  );
};

export default App;
```

Note:
- Replace `contractABI` and `contractAddress` with the actual ABI and address of the deployed smart contract.
- Add appropriate CSS styles in the `App.css` file to enhance the design.
