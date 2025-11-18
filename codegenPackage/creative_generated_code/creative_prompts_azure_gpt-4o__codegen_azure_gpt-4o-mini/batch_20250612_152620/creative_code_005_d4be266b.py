"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepewifhat.pages.dev
Prompt: Create a React component to display the user's PEPE WIF HAT NFT balance, mint price, and total supply, with a button to connect their wallet and mint an NFT.
Generated: DETERMINISTIC_d4be266bf7daf7bb
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define the contract address and ABI (Application Binary Interface)
const CONTRACT_ADDRESS = 'YOUR_CONTRACT_ADDRESS';
const CONTRACT_ABI = [
    // Add your contract's ABI here
];

const NFTComponent = () => {
    const [account, setAccount] = useState(null);
    const [balance, setBalance] = useState(0);
    const [mintPrice, setMintPrice] = useState(0);
    const [totalSupply, setTotalSupply] = useState(0);
    const [error, setError] = useState('');

    // Initialize web3
    const web3 = new Web3(window.ethereum);

    useEffect(() => {
        const loadBlockchainData = async () => {
            // Check if the wallet is connected
            if (account) {
                try {
                    const contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);

                    // Fetch the user's NFT balance
                    const balance = await contract.methods.balanceOf(account).call();
                    setBalance(balance);

                    // Fetch the mint price and total supply
                    const mintPrice = await contract.methods.mintPrice().call();
                    const totalSupply = await contract.methods.totalSupply().call();
                    setMintPrice(mintPrice);
                    setTotalSupply(totalSupply);
                } catch (err) {
                    setError('Error fetching data from the blockchain');
                }
            }
        };

        loadBlockchainData();
    }, [account]);

    // Function to connect the user's wallet
    const connectWallet = async () => {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
        } catch (err) {
            setError('Failed to connect wallet');
        }
    };

    // Function to mint an NFT
    const mintNFT = async () => {
        if (!account) {
            setError('Please connect your wallet first');
            return;
        }

        try {
            const contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);
            const tx = await contract.methods.mint().send({ from: account, value: mintPrice });
            console.log('Mint transaction:', tx);
            // Reload data after minting
            setBalance(await contract.methods.balanceOf(account).call());
        } catch (err) {
            setError('Error minting NFT');
        }
    };

    return (
        <div>
            <h1>PEPE WIF HAT NFT Dashboard</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <button onClick={connectWallet}>
                {account ? `Connected: ${account}` : 'Connect Wallet'}
            </button>
            <div>
                <h2>Your NFT Balance: {balance}</h2>
                <h2>Mint Price: {web3.utils.fromWei(mintPrice, 'ether')} ETH</h2>
                <h2>Total Supply: {totalSupply}</h2>
                <button onClick={mintNFT} disabled={!account}>
                    Mint NFT
                </button>
            </div>
        </div>
    );
};

export default NFTComponent;
```

Make sure to replace `YOUR_CONTRACT_ADDRESS` and add your contract's ABI in the code above to ensure it works correctly.
