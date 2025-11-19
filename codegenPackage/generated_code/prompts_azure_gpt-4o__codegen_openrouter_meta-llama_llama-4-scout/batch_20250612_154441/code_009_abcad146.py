"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Develop a web application using React and web3.js to display NFT minting progress and pledge completion status, similar to the Clone Force™ platform.
Generated: DETERMINISTIC_abcad146173e3045
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**NFT Minting Progress and Pledge Completion Status Tracker**

### Prerequisites

* Node.js (v14 or higher)
* npm (v6 or higher) or yarn (v1 or higher)
* React (v17 or higher)
* web3.js (v1 or higher)

### Code

```jsx
// Import required libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Set up web3 provider
const web3 = new Web3(window.ethereum);

// Contract ABI and address
const contractAbi = [
  {
    inputs: [],
    stateMutability: 'nonpayable',
    type: 'constructor',
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: true,
        name: 'account',
        type: 'address',
      },
      {
        indexed: true,
        name: 'id',
        type: 'uint256',
      },
    ],
    name: 'PledgeCreated',
    type: 'event',
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: true,
        name: 'account',
        type: 'address',
      },
      {
        indexed: true,
        name: 'id',
        type: 'uint256',
      },
    ],
    name: 'PledgeCompleted',
    type: 'event',
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: true,
        name: 'account',
        type: 'address',
      },
      {
        indexed: true,
        name: 'id',
        type: 'uint256',
      },
    ],
    name: 'NFTMinted',
    type: 'event',
  },
];

const contractAddress = '0x...';

// Create contract instance
const contract = new web3.eth.Contract(contractAbi, contractAddress);

// Component to display NFT minting progress and pledge completion status
function NFTTracker() {
  const [pledges, setPledges] = useState({});
  const [nfts, setNFTs] = useState({});
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    // Get user's Ethereum accounts
    web3.eth.getAccounts().then((accounts) => {
      setAccounts(accounts);
      // Listen for pledge events
      contract.events.PledgeCreated({ from: accounts[0] })
        .on('data', (event) => {
          const pledgeId = event.returnValues.id;
          const pledge = { ...pledges };
          pledge[pledgeId] = { status: 'pending' };
          setPledges(pledge);
        })
        .on('error', (error) => {
          console.error(error);
        });

      // Listen for pledge completion events
      contract.events.PledgeCompleted({ from: accounts[0] })
        .on('data', (event) => {
          const pledgeId = event.returnValues.id;
          const pledge = { ...pledges };
          pledge[pledgeId] = { status: 'completed' };
          setPledges(pledge);
        })
        .on('error', (error) => {
          console.error(error);
        });

      // Listen for NFT minting events
      contract.events.NFTMinted({ from: accounts[0] })
        .on('data', (event) => {
          const nftId = event.returnValues.id;
          const nft = { ...nfts };
          nft[nftId] = { status: 'minted' };
          setNFTs(nft);
        })
        .on('error', (error) => {
          console.error(error);
        });
    });
  }, [accounts]);

  // Function to get pledge status
  const getPledgeStatus = (pledgeId) => {
    if (pledges[pledgeId]) {
      return pledges[pledgeId].status;
    }
    return 'unknown';
  };

  // Function to get NFT status
  const getNFTStatus = (nftId) => {
    if (nfts[nftId]) {
      return nftIds[nftId].status;
    }
    return 'unknown';
  };

  return (
    <div>
      <h1>NFT Minting Progress and Pledge Completion Status</h1>
      <h2>Pledges:</h2>
      <ul>
        {Object.keys(pledges).map((pledgeId) => (
          <li key={pledgeId}>
            Pledge {pledgeId}: {getPledgeStatus(pledgeId)}
          </li>
        ))}
      </ul>
      <h2> NFTs:</h2>
      <ul>
        {Object.keys(nfts).map((nftId) => (
          <li key={nftId}>
            NFT {nftId}: {getNFTStatus(nftId)}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default NFTTracker;
```

```javascript
// App.js
import React from 'react';
import NFTTracker from './NFTTracker';

function App() {
  return (
    <div>
      <NFTTracker />
    </div>
  );
}

export default App;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```css
/* styles.css */
body {
  font-family: Arial, sans-serif;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

li:last-child {
  border-bottom: none;
}
```
