"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createra-genesis-land.netlify.app
Prompt: How can I create a user interface for a minting dApp that displays minting progress, similar to the Createra Genesis Land site?
Generated: DETERMINISTIC_603e5862efc0cf71
Batch ID: 20250612_163423
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
import './MintingApp.css'; // Import custom CSS for styling

// Setup Web3 and contract details
const web3 = new Web3(window.ethereum);
const contractAddress = 'YOUR_CONTRACT_ADDRESS_HERE';
const contractABI = [ /* Your Contract ABI Here */ ];

const MintingApp = () => {
    const [mintingProgress, setMintingProgress] = useState(0);
    const [isMinting, setIsMinting] = useState(false);
    const [error, setError] = useState(null);
    const [account, setAccount] = useState('');

    // Function to connect to MetaMask
    const connectWallet = async () => {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
        } catch (err) {
            setError('Failed to connect wallet. Please ensure MetaMask is installed.');
        }
    };

    // Function to mint tokens
    const mintTokens = async () => {
        if (!account) {
            setError('Please connect your wallet first.');
            return;
        }

        const contract = new web3.eth.Contract(contractABI, contractAddress);
        
        setIsMinting(true);
        setMintingProgress(0);

        try {
            // Simulate minting process
            for (let i = 0; i <= 100; i++) {
                setMintingProgress(i);
                await new Promise(resolve => setTimeout(resolve, 50)); // Simulate time delay
            }

            // Call the mint function of your contract
            await contract.methods.mint().send({ from: account });

            setMintingProgress(100);
        } catch (err) {
            setError('Minting failed. Please try again.');
        } finally {
            setIsMinting(false);
        }
    };

    // Effect to handle wallet connection on component mount
    useEffect(() => {
        connectWallet();
    }, []);

    return (
        <div className="minting-app">
            <h1>Minting dApp</h1>
            {error && <div className="error-message">{error}</div>}
            <div>
                <button onClick={mintTokens} disabled={isMinting}>
                    {isMinting ? 'Minting...' : 'Mint'}
                </button>
            </div>
            <div className="progress-bar">
                <div className="progress" style={{ width: `${mintingProgress}%` }} />
            </div>
            <div className="progress-text">{mintingProgress}%</div>
        </div>
    );
};

export default MintingApp;
```

```css
/* MintingApp.css */
.minting-app {
    text-align: center;
    font-family: Arial, sans-serif;
}

.error-message {
    color: red;
    margin-bottom: 20px;
}

.progress-bar {
    width: 100%;
    background-color: #e0e0e0;
    border-radius: 5px;
    overflow: hidden;
    margin: 20px 0;
}

.progress {
    height: 20px;
    background-color: #76c7c0;
    transition: width 0.5s ease;
}
```
