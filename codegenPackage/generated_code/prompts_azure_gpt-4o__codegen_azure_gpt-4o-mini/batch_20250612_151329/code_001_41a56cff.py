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
// Import the Web3 library
import Web3 from 'web3';

// Define the NFT contract ABI and address (replace with actual values)
const NFT_CONTRACT_ABI = [ /* ABI array here */ ];
const NFT_CONTRACT_ADDRESS = '0xYourNFTContractAddress';

// Initialize Web3
let web3;
let nftContract;

// DOM elements
const connectButton = document.getElementById('connectWallet');
const galleryContainer = document.getElementById('nftGallery');

// Function to connect to the user's wallet
async function connectWallet() {
    if (window.ethereum) {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            web3 = new Web3(window.ethereum);
            nftContract = new web3.eth.Contract(NFT_CONTRACT_ABI, NFT_CONTRACT_ADDRESS);
            console.log('Connected account:', accounts[0]);
            fetchNFTs();
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
        }
    } else {
        alert('Please install MetaMask or another Ethereum wallet to use this feature.');
    }
}

// Function to fetch NFTs from the contract
async function fetchNFTs() {
    try {
        const totalSupply = await nftContract.methods.totalSupply().call();
        for (let i = 0; i < totalSupply; i++) {
            const tokenId = await nftContract.methods.tokenByIndex(i).call();
            const tokenURI = await nftContract.methods.tokenURI(tokenId).call();
            displayNFT(tokenId, tokenURI);
        }
    } catch (error) {
        console.error('Error fetching NFTs:', error);
    }
}

// Function to display an NFT in the gallery
function displayNFT(tokenId, tokenURI) {
    const nftElement = document.createElement('div');
    nftElement.className = 'nft-item';
    
    // Fetch NFT metadata
    fetch(tokenURI)
        .then(response => response.json())
        .then(metadata => {
            nftElement.innerHTML = `
                <h3>${metadata.name}</h3>
                <img src="${metadata.image}" alt="${metadata.name}" />
                <button onclick="buyNFT(${tokenId})">Buy</button>
            `;
            galleryContainer.appendChild(nftElement);
        })
        .catch(error => console.error('Error fetching NFT metadata:', error));
}

// Function to buy an NFT
async function buyNFT(tokenId) {
    const accounts = await web3.eth.getAccounts();
    const buyerAddress = accounts[0];

    try {
        // Replace with the actual price and payment method
        const price = web3.utils.toWei('0.1', 'ether'); // Example price in Ether
        await nftContract.methods.buyNFT(tokenId).send({ from: buyerAddress, value: price });
        alert('NFT purchased successfully!');
    } catch (error) {
        console.error('Error purchasing NFT:', error);
        alert('Transaction failed. Please try again.');
    }
}

// Event listener for the connect wallet button
connectButton.addEventListener('click', connectWallet);
```

```html
<!-- HTML structure for the NFT gallery -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Gallery</title>
    <style>
        /* Basic styles for the gallery */
        #nftGallery {
            display: flex;
            flex-wrap: wrap;
        }
        .nft-item {
            border: 1px solid #ccc;
            margin: 10px;
            padding: 10px;
            width: 200px;
            text-align: center;
        }
    </style>
</head>
<body>
    <button id="connectWallet">Connect Wallet</button>
    <div id="nftGallery"></div>
    <script type="module" src="path/to/your/javascript/file.js"></script>
</body>
</html>
```
