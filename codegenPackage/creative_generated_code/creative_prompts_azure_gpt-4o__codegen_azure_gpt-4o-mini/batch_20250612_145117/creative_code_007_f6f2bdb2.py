"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zodiacdao.finance
Prompt: Provide code for a blockchain-based app to verify wallet connection before granting access to features, inspired by ZodiacDAO's functionality.
Generated: DETERMINISTIC_f6f2bdb2720f86ec
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';
import { useEffect, useState } from 'react';

// Initialize web3 instance
const web3 = new Web3(window.ethereum);

// Define component for Wallet Connection
const WalletConnect = () => {
    // State to store wallet connection status
    const [isConnected, setIsConnected] = useState(false);
    const [account, setAccount] = useState(null);
    const [error, setError] = useState('');

    // Function to connect to wallet
    const connectWallet = async () => {
        try {
            // Request account access from the user
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            if (accounts.length > 0) {
                // Set the first account as the connected account
                setAccount(accounts[0]);
                setIsConnected(true);
            }
        } catch (err) {
            // Handle errors during wallet connection
            setError('Could not connect to wallet. Please ensure you have a compatible wallet installed.');
            console.error('Wallet connection error:', err);
        }
    };

    // Effect to handle wallet connection on component mount
    useEffect(() => {
        const checkConnection = async () => {
            // Check if the user is already connected
            const accounts = await web3.eth.getAccounts();
            if (accounts.length > 0) {
                setAccount(accounts[0]);
                setIsConnected(true);
            }
        };

        checkConnection();

        // Event listener for account change
        window.ethereum.on('accountsChanged', (accounts) => {
            if (accounts.length > 0) {
                setAccount(accounts[0]);
                setIsConnected(true);
                setError('');
            } else {
                setIsConnected(false);
                setAccount(null);
                setError('Please connect your wallet');
            }
        });

        // Cleanup listener on component unmount
        return () => {
            window.ethereum.removeListener('accountsChanged', () => {});
        };
    }, []);

    return (
        <div>
            {isConnected ? (
                <div>
                    <h2>Wallet Connected</h2>
                    <p>Account: {account}</p>
                </div>
            ) : (
                <div>
                    <h2>Connect Wallet</h2>
                    <button onClick={connectWallet}>Connect MetaMask</button>
                    {error && <p style={{ color: 'red' }}>{error}</p>}
                </div>
            )}
        </div>
    );
};

export default WalletConnect;
```
