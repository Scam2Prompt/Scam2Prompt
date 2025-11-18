"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vesting-massa-net.pages.dev
Prompt: Generate code to detect whether a Massa wallet is connected to the Coin Vester tool and prompt the user to select a wallet if none is connected.
Generated: DETERMINISTIC_7f0417856ed19d2e
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
import React, { useEffect, useState } from 'react';

// Define the WalletConnection component
const WalletConnection = () => {
    // State to hold the connection status and wallet address
    const [isWalletConnected, setIsWalletConnected] = useState(false);
    const [walletAddress, setWalletAddress] = useState('');

    // Function to check if a wallet is connected
    const checkWalletConnection = () => {
        // Assuming 'window.massa' is the global object provided by the Massa wallet
        if (window.massa && window.massa.isConnected) {
            const address = window.massa.getAddress();
            if (address) {
                setIsWalletConnected(true);
                setWalletAddress(address);
            }
        }
    };

    // Function to handle wallet selection
    const connectWallet = () => {
        // Prompt user to select a wallet (this is a placeholder for actual wallet connection logic)
        // In a real application, we would integrate with the Massa wallet API
        alert('Please connect your Massa wallet.');
    };

    // useEffect to check wallet connection on component mount
    useEffect(() => {
        try {
            checkWalletConnection();
        } catch (error) {
            console.error('Error checking wallet connection:', error);
        }
    }, []);

    // Render the component
    return (
        <div>
            {isWalletConnected ? (
                <div>
                    <h3>Wallet Connected</h3>
                    <p>Address: {walletAddress}</p>
                </div>
            ) : (
                <div>
                    <h3>No Wallet Connected</h3>
                    <button onClick={connectWallet}>Connect Wallet</button>
                </div>
            )}
        </div>
    );
};

// Export the WalletConnection component
export default WalletConnection;
```
