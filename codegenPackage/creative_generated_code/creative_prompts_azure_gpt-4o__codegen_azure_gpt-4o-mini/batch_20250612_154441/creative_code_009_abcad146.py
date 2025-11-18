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

```javascript
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { NFT_CONTRACT_ABI, NFT_CONTRACT_ADDRESS } from './config'; // Import your contract ABI and address from a config file

// Main App component
const App = () => {
  // State variables
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [contract, setContract] = useState(null);
  const [mintingProgress, setMintingProgress] = useState(0);
  const [pledgeStatus, setPledgeStatus] = useState(false);
  const [error, setError] = useState('');

  // Initialize Web3 and contract instance
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Check if user has Metamask installed
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
          const nftContract = new web3Instance.eth.Contract(NFT_CONTRACT_ABI, NFT_CONTRACT_ADDRESS);
          setWeb3(web3Instance);
          setContract(nftContract);
        } else {
          setError('Please install Metamask to use this application.');
        }
      } catch (err) {
        setError(`Error initializing Web3: ${err.message}`);
      }
    };

    initWeb3();
  }, []);

  // Function to get minting progress
  const fetchMintingProgress = async () => {
    try {
      if (contract) {
        const totalMinted = await contract.methods.totalMinted().call();
        const totalSupply = await contract.methods.totalSupply().call();
        const progress = (totalMinted / totalSupply) * 100;
        setMintingProgress(progress);
      }
    } catch (err) {
      setError(`Error fetching minting progress: ${err.message}`);
    }
  };

  // Function to check pledge status
  const checkPledgeStatus = async () => {
    try {
      if (contract) {
        const status = await contract.methods.checkPledge(account).call();
        setPledgeStatus(status);
      }
    } catch (err) {
      setError(`Error fetching pledge status: ${err.message}`);
    }
  };

  // Fetch progress and status on component mount
  useEffect(() => {
    fetchMintingProgress();
    checkPledgeStatus();
  }, [contract, account]);

  return (
    <div>
      <h1>NFT Minting Dashboard</h1>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <div>
        <h2>Minting Progress</h2>
        <div style={{ width: '100%', background: '#e0e0e0', borderRadius: '5px' }}>
          <div
            style={{
              width: `${mintingProgress}%`,
              height: '20px',
              background: '#76c7c0',
              borderRadius: '5px',
            }}
          ></div>
        </div>
        <p>{mintingProgress.toFixed(2)}% Minted</p>
      </div>
      <div>
        <h2>Pledge Status</h2>
        <p>{pledgeStatus ? 'Pledge Completed' : 'Pledge Not Completed'}</p>
      </div>
    </div>
  );
};

export default App;
```

```javascript
// config.js
export const NFT_CONTRACT_ABI = [
  // Your NFT contract ABI goes here
];

export const NFT_CONTRACT_ADDRESS = '0xYourContractAddressHere';
```

Make sure to replace the `NFT_CONTRACT_ABI` and `NFT_CONTRACT_ADDRESS` placeholders with your actual NFT contract ABI and address. Additionally, ensure that you have `web3.js` and `react` installed in your project.
