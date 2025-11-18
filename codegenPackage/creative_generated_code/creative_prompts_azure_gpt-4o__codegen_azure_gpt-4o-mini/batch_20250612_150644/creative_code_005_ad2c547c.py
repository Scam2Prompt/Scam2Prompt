"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vesting-cookie.online
Prompt: Write code to integrate a wallet connection feature into a blockchain-based vesting portal using audited smart contracts, as implemented by Cookie DAO.
Generated: DETERMINISTIC_ad2c547c3a9984e5
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';
import { useState, useEffect } from 'react';

// Define a function to connect to the user's wallet
const useWalletConnection = () => {
    const [account, setAccount] = useState(null);
    const [provider, setProvider] = useState(null);
    const [error, setError] = useState(null);
    
    // Initialize Web3 provider and handle wallet connection
    const connectWallet = async () => {
        try {
            // Check if MetaMask is installed
            if (window.ethereum) {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                
                // Set the connected account and provider
                setAccount(accounts[0]);
                const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
                setProvider(web3Provider);
            } else {
                setError('MetaMask is not installed. Please install it to use this feature.');
            }
        } catch (err) {
            // Handle errors during wallet connection
            console.error("Error connecting wallet:", err);
            setError('Failed to connect to wallet. Please try again.');
        }
    };

    return { account, provider, connectWallet, error };
};

// Example component to use the wallet connection hook
const WalletConnectButton = () => {
    const { account, connectWallet, error } = useWalletConnection();

    return (
        <div>
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                </div>
            ) : (
                <button onClick={connectWallet}>
                    Connect Wallet
                </button>
            )}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

// Main application component
const App = () => {
    return (
        <div>
            <h1>Blockchain Vesting Portal</h1>
            <WalletConnectButton />
        </div>
    );
};

// Render the application
const rootElement = document.getElementById('root');
ReactDOM.render(<App />, rootElement);
```

### Notes:
- Ensure that this code is part of a React application and that you have the required dependencies installed (`web3`, `ethers`, and `react`).
- The code initializes a wallet connection using MetaMask. Error handling is implemented to catch potential issues during the connection process.
- The user interface provides feedback on the wallet connection status and any errors that may occur.
