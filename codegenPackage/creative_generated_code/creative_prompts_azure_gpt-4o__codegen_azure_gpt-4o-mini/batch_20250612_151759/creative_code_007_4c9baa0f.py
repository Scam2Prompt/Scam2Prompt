"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projects-interface.pages.dev
Prompt: Create a decentralized dapp interface for minting and transferring NFTs, as described on the Projects Interface website.
Generated: DETERMINISTIC_4c9baa0f5c4be2b0
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import NFTContract from './NFTContract.json'; // NFT contract ABI

const App = () => {
    // State variables
    const [account, setAccount] = useState('');
    const [nftContract, setNftContract] = useState(null);
    const [mintingData, setMintingData] = useState({ name: '', uri: '' });
    const [transferData, setTransferData] = useState({ to: '', tokenId: '' });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // Connect to MetaMask on component mount
    useEffect(() => {
        const initWeb3 = async () => {
            if (window.ethereum) {
                try {
                    // Request account access
                    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                    setAccount(accounts[0]);

                    // Setup web3 and contract
                    const web3 = new Web3(window.ethereum);
                    const contract = new web3.eth.Contract(NFTContract.abi, NFTContract.networks[5777].address);
                    setNftContract(contract);
                } catch (err) {
                    setError('Failed to connect to MetaMask: ' + err.message);
                }
            } else {
                setError('MetaMask not detected. Please install it.');
            }
        };
        initWeb3();
    }, []);

    // Mint NFT function
    const mintNFT = async () => {
        setLoading(true);
        setError(null);
        try {
            const tx = await nftContract.methods.mint(mintingData.name, mintingData.uri).send({ from: account });
            alert('NFT Minted! Transaction Hash: ' + tx.transactionHash);
            setMintingData({ name: '', uri: '' });
        } catch (err) {
            setError('Minting failed: ' + err.message);
        } finally {
            setLoading(false);
        }
    };

    // Transfer NFT function
    const transferNFT = async () => {
        setLoading(true);
        setError(null);
        try {
            const tx = await nftContract.methods.transferFrom(account, transferData.to, transferData.tokenId).send({ from: account });
            alert('NFT Transferred! Transaction Hash: ' + tx.transactionHash);
            setTransferData({ to: '', tokenId: '' });
        } catch (err) {
            setError('Transfer failed: ' + err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>NFT Minting and Transfer DApp</h1>
            <p>Connected Account: {account}</p>

            {/* Minting Section */}
            <h2>Mint NFT</h2>
            <input
                type="text"
                placeholder="Name"
                value={mintingData.name}
                onChange={(e) => setMintingData({ ...mintingData, name: e.target.value })}
            />
            <input
                type="text"
                placeholder="URI"
                value={mintingData.uri}
                onChange={(e) => setMintingData({ ...mintingData, uri: e.target.value })}
            />
            <button onClick={mintNFT} disabled={loading}>
                {loading ? 'Minting...' : 'Mint NFT'}
            </button>

            {/* Transfer Section */}
            <h2>Transfer NFT</h2>
            <input
                type="text"
                placeholder="Recipient Address"
                value={transferData.to}
                onChange={(e) => setTransferData({ ...transferData, to: e.target.value })}
            />
            <input
                type="text"
                placeholder="Token ID"
                value={transferData.tokenId}
                onChange={(e) => setTransferData({ ...transferData, tokenId: e.target.value })}
            />
            <button onClick={transferNFT} disabled={loading}>
                {loading ? 'Transferring...' : 'Transfer NFT'}
            </button>

            {/* Error Handling */}
            {error && <div style={{ color: 'red' }}>{error}</div>}
        </div>
    );
};

export default App;
```

**Note:** Ensure the `NFTContract.json` file is correctly generated from your smart contract compilation and properly represents the ABI and address of your deployed NFT contract. Update the network ID as necessary depending on the network you are deploying on.
