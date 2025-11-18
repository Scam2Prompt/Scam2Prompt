"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oooooo-money.pages.dev
Prompt: Write code to integrate a wallet connection feature for a treasure-hunting game using blockchain APIs, referencing the "CHEST CHASE BRIDGE" functionality.
Generated: DETERMINISTIC_c2aeb307b59f3c1b
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3'; // Web3 library for blockchain interactions
import { useEffect, useState } from 'react'; // React hooks for state management

// Define the WalletConnection component
const WalletConnection = () => {
    const [account, setAccount] = useState(null); // State to hold the connected wallet account
    const [web3, setWeb3] = useState(null); // State to hold the Web3 instance
    const [error, setError] = useState(null); // State to hold error messages

    // Effect for initializing Web3 and connecting to the wallet
    useEffect(() => {
        // Function to initialize Web3
        const initWeb3 = async () => {
            // Check if window.ethereum is available for wallet connection
            if (window.ethereum) {
                try {
                    // Create a new Web3 instance
                    const web3Instance = new Web3(window.ethereum);
                    setWeb3(web3Instance);

                    // Request account access from the user
                    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                    if (accounts.length > 0) {
                        setAccount(accounts[0]); // Set the connected account
                    }
                } catch (err) {
                    setError('Failed to connect to wallet.'); // Handle connection error
                    console.error(err);
                }
            } else {
                setError('Please install MetaMask to use this feature.'); // Prompt for wallet installation
            }
        };

        initWeb3(); // Call the initialization function
    }, []); // Empty dependency array ensures this runs only once

    // Function to handle wallet disconnection
    const disconnectWallet = () => {
        setAccount(null); // Clear the account state
        setWeb3(null); // Clear the Web3 instance
        setError(null); // Clear any errors
    };

    return (
        <div>
            <h2>Wallet Connection</h2>
            {error && <div className="error">{error}</div>} {/* Display error messages if any */}
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={() => window.ethereum.request({ method: 'eth_requestAccounts' })}>
                    Connect Wallet
                </button>
            )}
        </div>
    );
};

// Export the component for use in the application
export default WalletConnection;
```
