"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-worldlibertfinancialcom.pages.dev
Prompt: Develop a script to connect a cryptocurrency wallet to a website, ensuring the wallet contents can be read securely without incurring gas costs, as described on the $WLFI Token Presale page.
Generated: DETERMINISTIC_1215c4f6edc66f80
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { useEffect, useState } from 'react';

// Define the WalletConnector component
const WalletConnector = () => {
    // State to hold wallet address and balance
    const [walletAddress, setWalletAddress] = useState('');
    const [balance, setBalance] = useState('0');
    const [error, setError] = useState('');

    // Initialize web3 instance
    const web3 = new Web3(window.ethereum);

    // Function to connect to the wallet
    const connectWallet = async () => {
        try {
            // Request wallet connection
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setWalletAddress(accounts[0]);
            fetchBalance(accounts[0]);
        } catch (err) {
            setError('Failed to connect wallet: ' + err.message);
            console.error(err);
        }
    };

    // Function to fetch wallet balance
    const fetchBalance = async (address) => {
        try {
            // Get the balance in Wei
            const balanceInWei = await web3.eth.getBalance(address);
            // Convert Wei to Ether
            const balanceInEther = web3.utils.fromWei(balanceInWei, 'ether');
            setBalance(balanceInEther);
        } catch (err) {
            setError('Failed to fetch balance: ' + err.message);
            console.error(err);
        }
    };

    // Effect to check if wallet is already connected
    useEffect(() => {
        const checkWalletConnection = async () => {
            if (window.ethereum) {
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                if (accounts.length > 0) {
                    setWalletAddress(accounts[0]);
                    fetchBalance(accounts[0]);
                }
            } else {
                setError('Please install MetaMask!');
            }
        };

        checkWalletConnection();
    }, []);

    return (
        <div>
            <h1>Connect Your Wallet</h1>
            {error && <div className="error">{error}</div>}
            <button onClick={connectWallet}>Connect Wallet</button>
            {walletAddress && (
                <div>
                    <h2>Wallet Address: {walletAddress}</h2>
                    <h3>Balance: {balance} ETH</h3>
                </div>
            )}
        </div>
    );
};

export default WalletConnector;
```

**Note**: Ensure that you have installed the `web3` library in your project by running `npm install web3`, and that you are using this component within a React application. Additionally, make sure that MetaMask or another Ethereum wallet is installed in the user's browser for this code to function correctly.
