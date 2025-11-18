"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6051142952.pages.dev
Prompt: Create a tutorial for developers on how to use MetaMask's SDK to build a decentralized application that supports NFT transactions.
Generated: DETERMINISTIC_161748a498054dfd
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { MetaMaskSDK } from '@metamask/sdk';
import { ethers } from 'ethers';
import './App.css';  // Assuming you have some basic CSS for styling

// Initialize MetaMask SDK
const sdk = new MetaMaskSDK({ 
    // Your MetaMask SDK configuration options here
});
const metamaskProvider = sdk.getProvider();

const App = () => {
    const [account, setAccount] = useState('');
    const [nftContractAddress, setNftContractAddress] = useState('');
    const [nftTokenId, setNftTokenId] = useState('');

    // Connect to MetaMask
    const connectWallet = async () => {
        try {
            const accounts = await metamaskProvider.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
        } catch (error) {
            console.error("Failed to connect wallet:", error);
            alert("Failed to connect wallet. Please try again.");
        }
    };

    // Function to mint an NFT
    const mintNFT = async () => {
        if (!account || !nftContractAddress || !nftTokenId) {
            alert("Please enter all required fields.");
            return;
        }

        try {
            const contract = new ethers.Contract(nftContractAddress, nftAbi, metamaskProvider);
            const transaction = await contract.mint(account, nftTokenId);
            await transaction.wait();
            alert(`NFT minted successfully! Transaction Hash: ${transaction.hash}`);
        } catch (error) {
            console.error("Error minting NFT:", error);
            alert("Failed to mint NFT. Please check console for details.");
        }
    };

    // Sample NFT contract ABI (replace with your actual contract ABI)
    const nftAbi = [
        // Minimal ABI required to mint an NFT
        "function mint(address to, uint256 tokenId) public"
    ];

    // Render the UI
    return (
        <div className="App">
            <h1>MetaMask NFT Minting DApp</h1>
            {!account ? (
                <button onClick={connectWallet}>Connect MetaMask</button>
            ) : (
                <div>
                    <p>Connected Account: {account}</p>
                    <input 
                        type="text" 
                        placeholder="NFT Contract Address" 
                        value={nftContractAddress} 
                        onChange={(e) => setNftContractAddress(e.target.value)} 
                    />
                    <input 
                        type="number" 
                        placeholder="NFT Token ID" 
                        value={nftTokenId} 
                        onChange={(e) => setNftTokenId(e.target.value)} 
                    />
                    <button onClick={mintNFT}>Mint NFT</button>
                </div>
            )}
        </div>
    );
};

export default App;
```

### Notes:
- Ensure that you have the necessary dependencies installed: `npm install react @metamask/sdk ethers`.
- This code assumes that you have a smart contract deployed that follows the ERC721 standard for NFTs.
- Replace the minimal ABI with the actual ABI of your NFT contract.
- Be sure to handle additional edge cases and validations in a production application.
