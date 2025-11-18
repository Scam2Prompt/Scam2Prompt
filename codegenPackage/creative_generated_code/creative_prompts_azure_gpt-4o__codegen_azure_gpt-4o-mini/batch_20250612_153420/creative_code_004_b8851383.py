"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapsale-io.pages.dev
Prompt: Create a web application interface for purchasing presale tokens on UniswapSale, ensuring compatibility with ERC20, BEP20, MATIC, and SOL networks.
Generated: DETERMINISTIC_b8851383e087d6cb
Batch ID: 20250612_153420
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
import axios from 'axios';

// Define the main application component
const PresaleTokenPurchase = () => {
    const [network, setNetwork] = useState('');
    const [amount, setAmount] = useState('');
    const [walletAddress, setWalletAddress] = useState('');
    const [tokenAddress, setTokenAddress] = useState('');
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    // Hook to detect the user's web3 provider
    useEffect(() => {
        if (window.ethereum) {
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            getNetwork(provider);
        } else {
            setError('Please install a web3 wallet like MetaMask.');
        }
    }, []);

    // Function to get the user's current network
    const getNetwork = async (provider) => {
        const network = await provider.getNetwork();
        setNetwork(network.name);
    };

    // Function to handle the token purchase
    const purchaseTokens = async () => {
        try {
            setIsLoading(true);
            setError('');

            // Validate inputs
            if (!amount || !walletAddress || !tokenAddress) {
                throw new Error('All fields are required.');
            }

            const provider = new ethers.providers.Web3Provider(window.ethereum);
            const signer = provider.getSigner();

            // Create a contract instance (this should be the specific presale contract address)
            const presaleContract = new ethers.Contract(tokenAddress, presaleABI, signer);

            // Execute the purchase function (assumes a function 'buyTokens' exists in the contract)
            const tx = await presaleContract.buyTokens(walletAddress, ethers.utils.parseUnits(amount, 18));
            await tx.wait(); // Wait for the transaction to be mined

            alert('Purchase successful!');
        } catch (err) {
            setError(err.message);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div>
            <h1>Presale Token Purchase</h1>
            <p>Current Network: {network}</p>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <input
                type="text"
                placeholder="Token Address"
                value={tokenAddress}
                onChange={(e) => setTokenAddress(e.target.value)}
            />
            <input
                type="text"
                placeholder="Amount"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
            />
            <input
                type="text"
                placeholder="Wallet Address"
                value={walletAddress}
                onChange={(e) => setWalletAddress(e.target.value)}
            />
            <button onClick={purchaseTokens} disabled={isLoading}>
                {isLoading ? 'Processing...' : 'Buy Tokens'}
            </button>
        </div>
    );
};

// Define the presale contract ABI (simplified example)
const presaleABI = [
    // Define the contract functions you need to interact with.
    // For example:
    "function buyTokens(address buyer, uint256 amount) public"
];

// Export the main component
export default PresaleTokenPurchase;
```
