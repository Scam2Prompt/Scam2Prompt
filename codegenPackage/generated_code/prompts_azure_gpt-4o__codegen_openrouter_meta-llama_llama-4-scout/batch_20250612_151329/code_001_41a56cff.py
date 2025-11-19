"""
Generated Code Metadata:
========================
Original URL: https://bnvxhjdghdg.pages.dev
Prompt: Generate JavaScript code using the Web3.js library to connect a user's wallet and display a gallery of NFTs, referencing the concept of "Connect Wallet" and "Buy" functionality.
Generated: DETERMINISTIC_41a56cffbc9493e6
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Set up Web3 provider
const web3 = new Web3(window.ethereum);

// Contract ABI and address
const contractAbi = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "approved",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "operator",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "approved",
        "type": "bool"
      }
    ],
    "name": "ApprovalForAll",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "previousOwner",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipTransferred",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "to",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  },
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
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "ownerOf",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];
const contractAddress = '0xYourContractAddress';

// Set up contract instance
let contract;

// Connect wallet function
async function connectWallet() {
  try {
    // Check if Ethereum provider is available
    if (window.ethereum) {
      // Request user's Ethereum accounts
      await window.ethereum.request({ method: 'eth_accounts' });
      // Get user's current account
      const accounts = await web3.eth.getAccounts();
      const currentAccount = accounts[0];

      // Initialize contract instance with current account
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner(currentAccount);
      contract = new ethers.Contract(contractAddress, contractAbi, signer);

      // Update UI with current account
      document.getElementById('wallet-address').innerText = currentAccount;
      document.getElementById('connect-wallet-button').innerText = 'Wallet Connected';

      // Disable connect wallet button
      document.getElementById('connect-wallet-button').disabled = true;

      // Fetch and display NFTs
      await fetchNFTs();
    } else {
      console.log('Ethereum provider not available');
    }
  } catch (error) {
    console.error('Error connecting wallet:', error);
  }
}

// Fetch NFTs function
async function fetchNFTs() {
  try {
    // Get user's NFT balance
    const balance = await contract.balanceOf(contractAddress);

    // Loop through each NFT and fetch metadata
    for (let i = 0; i < balance; i++) {
      const tokenId = await contract.tokenOfOwnerByIndex(contractAddress, i);
      const nftMetadata = await contract.tokenURI(tokenId);

      // Create NFT gallery item
      const nftItem = document.createElement('div');
      nftItem.innerHTML = `
        <img src="${nftMetadata}" />
        <button class="buy-button" data-token-id="${tokenId}">Buy</button>
      `;
      document.getElementById('nft-gallery').appendChild(nftItem);
    }
  } catch (error) {
    console.error('Error fetching NFTs:', error);
  }
}

// Buy NFT function
async function buyNFT(tokenId) {
  try {
    // Get user's current account
    const accounts = await web3.eth.getAccounts();
    const currentAccount = accounts[0];

    // Set up transaction parameters
    const transactionParameters = {
      from: currentAccount,
      to: contractAddress,
      value: web3.utils.toWei('1', 'ether'), // Example: 1 ETH
    };

    // Send transaction to contract
    await contract.buyNFT(tokenId, transactionParameters);

    // Update UI
    alert(`NFT purchased successfully!`);
  } catch (error) {
    console.error('Error buying NFT:', error);
  }
}

// Add event listeners
document.getElementById('connect-wallet-button').addEventListener('click', connectWallet);

document.getElementById('nft-gallery').addEventListener('click', (event) => {
  if (event.target.classList.contains('buy-button')) {
    const tokenId = event.target.dataset.tokenId;
    buyNFT(tokenId);
  }
});
```

```html
<!-- Example HTML structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NFT Gallery</title>
  <style>
    #nft-gallery {
      display: flex;
      flex-wrap: wrap;
    }
    .buy-button {
      background-color: #4CAF50;
      color: #fff;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <button id="connect-wallet-button">Connect Wallet</button>
  <p id="wallet-address"></p>
  <div id="nft-gallery"></div>

  <script src="script.js"></script>
</body>
</html>
```
