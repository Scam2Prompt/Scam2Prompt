"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogg.pages.dev
Prompt: Generate code to create a presale widget for a cryptocurrency like $FROP, allowing users to connect their wallets, select payment methods across multiple blockchains, and purchase tokens.
Generated: DETERMINISTIC_dbf3ba20f37146c1
Batch ID: 20250612_145826
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
import { ethers } from 'ethers';

// PresaleWidget component to handle token presale
const PresaleWidget = () => {
    // State variables
    const [walletAddress, setWalletAddress] = useState('');
    const [paymentMethod, setPaymentMethod] = useState('Ethereum');
    const [tokenAmount, setTokenAmount] = useState(1);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    // Connect to user's wallet
    const connectWallet = async () => {
        try {
            // Check for Ethereum provider
            if (window.ethereum) {
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                setWalletAddress(accounts[0]);
            } else {
                throw new Error('No Ethereum provider found. Please install MetaMask.');
            }
        } catch (err) {
            setError(err.message);
        }
    };

    // Handle token purchase
    const purchaseTokens = async () => {
        setLoading(true);
        setError(null);
        try {
            // Validate inputs
            if (!walletAddress) throw new Error('Please connect your wallet.');
            if (tokenAmount <= 0) throw new Error('Token amount must be greater than 0.');

            // Token purchase logic (this should call the smart contract)
            // Example code for Ethereum using ethers.js
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            const signer = provider.getSigner();
            const contractAddress = '0xYourTokenContractAddress'; // Replace with your contract address
            const tokenContract = new ethers.Contract(contractAddress, [
                // Replace with your contract ABI
                'function buyTokens(uint256 amount) public payable'
            ], signer);

            // Estimate gas and send transaction
            const tx = await tokenContract.buyTokens(tokenAmount, { value: ethers.utils.parseEther((tokenAmount * 0.01).toString()) }); // Example price
            await tx.wait();
            alert('Tokens purchased successfully!');
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="presale-widget">
            <h2>Presale Widget for $FROP</h2>
            {error && <p className="error">{error}</p>}
            <button onClick={connectWallet}>Connect Wallet</button>
            <p>Connected Wallet: {walletAddress}</p>
            <label>
                Select Payment Method:
                <select value={paymentMethod} onChange={(e) => setPaymentMethod(e.target.value)}>
                    <option value="Ethereum">Ethereum</option>
                    <option value="Binance Smart Chain">Binance Smart Chain</option>
                    <option value="Polygon">Polygon</option>
                    {/* Add other blockchains as needed */}
                </select>
            </label>
            <label>
                Amount of Tokens:
                <input
                    type="number"
                    value={tokenAmount}
                    onChange={(e) => setTokenAmount(e.target.value)}
                    min="1"
                />
            </label>
            <button onClick={purchaseTokens} disabled={loading}>
                {loading ? 'Purchasing...' : 'Purchase Tokens'}
            </button>
        </div>
    );
};

export default PresaleWidget;
```

### Note:
- Ensure to replace `0xYourTokenContractAddress` with the actual smart contract address of your token and update the contract ABI accordingly.
- This code assumes you have the necessary environment to run a React application with Web3 and Ethers.js installed.
