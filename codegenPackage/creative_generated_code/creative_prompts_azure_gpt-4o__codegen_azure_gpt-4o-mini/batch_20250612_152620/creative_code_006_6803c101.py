"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimicguard.web.app
Prompt: Write a smart contract that verifies wallet ownership and integrates with a web app for Discord access control, inspired by MimicGuard.
Generated: DETERMINISTIC_6803c10195a4b005
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

contract WalletOwnershipVerifier is Ownable {
    using ECDSA for bytes32;

    // Mapping to track authorized wallets
    mapping(address => bool) private authorizedWallets;

    // Event emitted when a wallet is authorized or revoked
    event WalletAuthorizationChanged(address indexed wallet, bool isAuthorized);

    // The ERC721 token contract used for ownership verification
    IERC721 public nftContract;

    // Constructor to initialize the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    // Function to authorize a wallet for access
    function authorizeWallet(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid wallet address");
        authorizedWallets[wallet] = true;
        emit WalletAuthorizationChanged(wallet, true);
    }

    // Function to revoke authorization from a wallet
    function revokeWallet(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid wallet address");
        authorizedWallets[wallet] = false;
        emit WalletAuthorizationChanged(wallet, false);
    }

    // Function to check if a wallet is authorized
    function isWalletAuthorized(address wallet) external view returns (bool) {
        return authorizedWallets[wallet];
    }

    // Function to verify ownership of a specific NFT
    function verifyNFTOwnership(address owner, uint256 tokenId) external view returns (bool) {
        return nftContract.ownerOf(tokenId) == owner;
    }
    
    // Function to authorize wallet based on NFT ownership
    function authorizeWalletByNFT(uint256 tokenId) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        authorizedWallets[msg.sender] = true;
        emit WalletAuthorizationChanged(msg.sender, true);
    }
}
```

### Web App Integration (JavaScript Example)

```javascript
// Example of integrating with the WalletOwnershipVerifier smart contract
const Web3 = require('web3');
const contractABI = require('./WalletOwnershipVerifierABI.json'); // ABI of the contract
const contractAddress = 'YOUR_CONTRACT_ADDRESS';

const web3 = new Web3(window.ethereum); // Assume MetaMask is used

async function checkWalletAuthorization(walletAddress) {
    const contract = new web3.eth.Contract(contractABI, contractAddress);

    try {
        const isAuthorized = await contract.methods.isWalletAuthorized(walletAddress).call();
        return isAuthorized;
    } catch (error) {
        console.error('Error checking wallet authorization:', error);
        throw new Error('Failed to check wallet authorization');
    }
}

async function authorizeWallet(tokenId) {
    const contract = new web3.eth.Contract(contractABI, contractAddress);
    
    try {
        const accounts = await web3.eth.getAccounts();
        await contract.methods.authorizeWalletByNFT(tokenId).send({ from: accounts[0] });
        console.log('Wallet authorized based on NFT ownership');
    } catch (error) {
        console.error('Error authorizing wallet:', error);
        throw new Error('Failed to authorize wallet');
    }
}

// Event listener example for Discord bot integration
async function onDiscordCommandReceived(command, walletAddress) {
    if (command === 'check') {
        const isAuthorized = await checkWalletAuthorization(walletAddress);
        // Implement logic to manage access based on isAuthorized
    } else if (command === 'authorize') {
        // Token ID should be passed as an argument
        const tokenId = 1; // Example token ID
        await authorizeWallet(tokenId);
    }
}
```
