"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexappsresolve.com
Prompt: Can you provide a code example for integrating decentralized applications with self-custodial wallets?
Generated: DETERMINISTIC_149c320f172351de
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3'; // For interacting with the Ethereum blockchain
import { ethers } from 'ethers'; // For self-custodial wallet integration
import { useState, useEffect } from 'react'; // For React state management
import { toast } from 'react-toastify'; // For user notifications

// Initialize Web3 and Ethereum provider
const web3 = new Web3(window.ethereum); // Assuming MetaMask is available

// Function to connect to a self-custodial wallet
async function connectWallet() {
    try {
        // Request account access if needed
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Log the connected account
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        // Handle errors (e.g., user denied access)
        console.error('User denied account access:', error);
        toast.error('Failed to connect wallet. Please try again.');
        throw error;
    }
}

// Function to fetch and display account balance
async function getAccountBalance(account) {
    try {
        const balance = await web3.eth.getBalance(account);
        // Convert balance from Wei to Ether
        const etherBalance = web3.utils.fromWei(balance, 'ether');
        console.log('Account balance:', etherBalance, 'ETH');
        return etherBalance;
    } catch (error) {
        console.error('Error fetching account balance:', error);
        toast.error('Failed to fetch balance. Please try again.');
        throw error;
    }
}

// React component for wallet integration
const WalletConnect = () => {
    const [account, setAccount] = useState(null);
    const [balance, setBalance] = useState(null);

    useEffect(() => {
        // Check if wallet is already connected
        const checkWalletConnection = async () => {
            if (window.ethereum) {
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                if (accounts.length > 0) {
                    setAccount(accounts[0]);
                    const balance = await getAccountBalance(accounts[0]);
                    setBalance(balance);
                }
            }
        };
        
        checkWalletConnection();
    }, []);

    const handleConnectWallet = async () => {
        const connectedAccount = await connectWallet();
        setAccount(connectedAccount);
        const balance = await getAccountBalance(connectedAccount);
        setBalance(balance);
    };

    return (
        <div>
            <h1>Decentralized Application</h1>
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <p>Balance: {balance} ETH</p>
                </div>
            ) : (
                <button onClick={handleConnectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default WalletConnect;
```

**Note:** Ensure you have the required dependencies in your project:
```bash
npm install web3 ethers react react-toastify
```
