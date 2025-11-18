"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Create a web application interface in React that allows users to connect their Ethereum wallet, select the number of NFTs to mint (up to 5 per transaction), and display the total mint cost, as described on KevinLand.
Generated: DETERMINISTIC_e7d37b2375c33be3
Batch ID: 20250612_152827
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
import './App.css'; // Import custom CSS for styling

// Define the main App component
const App = () => {
    // State variables
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [nftCount, setNftCount] = useState(1);
    const [mintCost, setMintCost] = useState(0);
    const NFT_PRICE = 0.05; // Set the price of each NFT in ETH

    // Effect to initialize Web3
    useEffect(() => {
        const initWeb3 = async () => {
            // Check if MetaMask is installed
            if (window.ethereum) {
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);
                // Request account access
                try {
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);
                } catch (error) {
                    console.error("User denied account access", error);
                }
            } else {
                alert('Please install MetaMask to use this app');
            }
        };

        initWeb3();
    }, []);

    // Function to handle NFT count change
    const handleCountChange = (event) => {
        const value = parseInt(event.target.value);
        if (value >= 1 && value <= 5) {
            setNftCount(value);
        }
    };

    // Function to calculate the total mint cost
    const calculateMintCost = () => {
        const totalCost = NFT_PRICE * nftCount;
        setMintCost(totalCost);
    };

    // Effect to calculate mint cost whenever nftCount changes
    useEffect(() => {
        calculateMintCost();
    }, [nftCount]);

    // Function to simulate minting NFTs (replace with actual contract interaction)
    const mintNFTs = async () => {
        if (!account || !web3) {
            alert('Web3 is not initialized or account is not connected');
            return;
        }

        // Here you would typically call the smart contract's mint function
        console.log(`Minting ${nftCount} NFTs for ${mintCost} ETH from account: ${account}`);
        // Simulate success message
        alert(`Successfully minted ${nftCount} NFTs!`);
    };

    return (
        <div className="App">
            <h1>Mint Your NFTs</h1>
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <label>
                        Select number of NFTs to mint (1-5):
                        <input
                            type="number"
                            value={nftCount}
                            onChange={handleCountChange}
                            min="1"
                            max="5"
                        />
                    </label>
                    <p>Total Mint Cost: {mintCost} ETH</p>
                    <button onClick={mintNFTs}>Mint NFTs</button>
                </div>
            ) : (
                <button onClick={() => window.ethereum.request({ method: 'eth_requestAccounts' })}>
                    Connect Wallet
                </button>
            )}
        </div>
    );
};

export default App;
```
