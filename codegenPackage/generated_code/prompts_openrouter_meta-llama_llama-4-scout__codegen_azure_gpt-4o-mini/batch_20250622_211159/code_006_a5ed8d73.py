"""
Generated Code Metadata:
========================
Original URL: https://nft-curve.com
Prompt: Develop a MetaMask Snap that enables users to purchase and manage NFTs directly within their wallet, using the MetaMask SDK and Web3 Services.
Generated: DETERMINISTIC_a5ed8d73c65d39a6
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from MetaMask SDK and Web3
import { Onboarding } from '@metamask/onboarding';
import Web3 from 'web3';

// Initialize the onboarding process
const onboarding = new Onboarding();

// Check if MetaMask is installed
if (!Onboarding.isMetaMaskInstalled()) {
    onboarding.startOnboarding();
}

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Function to connect to MetaMask
async function connectWallet() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Error connecting to wallet:', error);
        throw new Error('Wallet connection failed');
    }
}

// Function to purchase an NFT
async function purchaseNFT(contractAddress, tokenId, price) {
    const account = await connectWallet();
    const nftContract = new web3.eth.Contract(NFT_ABI, contractAddress);

    try {
        const transaction = await nftContract.methods.purchase(tokenId).send({
            from: account,
            value: web3.utils.toWei(price, 'ether'),
        });
        console.log('NFT purchased successfully:', transaction);
    } catch (error) {
        console.error('Error purchasing NFT:', error);
        throw new Error('NFT purchase failed');
    }
}

// Function to fetch owned NFTs
async function fetchOwnedNFTs(contractAddress) {
    const account = await connectWallet();
    const nftContract = new web3.eth.Contract(NFT_ABI, contractAddress);

    try {
        const balance = await nftContract.methods.balanceOf(account).call();
        const ownedNFTs = [];
        for (let i = 0; i < balance; i++) {
            const tokenId = await nftContract.methods.tokenOfOwnerByIndex(account, i).call();
            ownedNFTs.push(tokenId);
        }
        console.log('Owned NFTs:', ownedNFTs);
        return ownedNFTs;
    } catch (error) {
        console.error('Error fetching owned NFTs:', error);
        throw new Error('Failed to fetch owned NFTs');
    }
}

// Function to display NFTs in the wallet
async function displayNFTs() {
    const contractAddress = 'YOUR_NFT_CONTRACT_ADDRESS'; // Replace with your NFT contract address
    try {
        const ownedNFTs = await fetchOwnedNFTs(contractAddress);
        // Render NFTs in the UI (implementation depends on your UI framework)
        renderNFTs(ownedNFTs);
    } catch (error) {
        console.error('Error displaying NFTs:', error);
    }
}

// Function to render NFTs (placeholder for actual UI rendering logic)
function renderNFTs(nfts) {
    // Implement your UI rendering logic here
    console.log('Rendering NFTs:', nfts);
}

// Event listener for wallet connection
document.getElementById('connectButton').addEventListener('click', connectWallet);

// Event listener for NFT purchase
document.getElementById('purchaseButton').addEventListener('click', () => {
    const contractAddress = 'YOUR_NFT_CONTRACT_ADDRESS'; // Replace with your NFT contract address
    const tokenId = document.getElementById('tokenIdInput').value;
    const price = document.getElementById('priceInput').value;
    purchaseNFT(contractAddress, tokenId, price);
});

// Event listener to display NFTs
document.getElementById('displayButton').addEventListener('click', displayNFTs);
```

**Note:** Replace `YOUR_NFT_CONTRACT_ADDRESS` with the actual NFT contract address and ensure that `NFT_ABI` is defined with the correct ABI for your NFT contract.
