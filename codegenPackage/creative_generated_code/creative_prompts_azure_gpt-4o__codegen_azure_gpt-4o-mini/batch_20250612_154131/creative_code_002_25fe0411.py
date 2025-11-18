"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sorta.finance
Prompt: Generate code to detect wallet connection status and handle errors when accessing the Sorta Finance app.
Generated: DETERMINISTIC_25fe0411b0fd36e2
Batch ID: 20250612_154131
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
import Web3 from 'web3';

// Define the SortaFinanceApp component
const SortaFinanceApp = () => {
    // State to hold wallet connection status and error messages
    const [isConnected, setIsConnected] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');

    // Initialize Web3 instance
    const web3 = new Web3(window.ethereum); // Using MetaMask's provider

    // Function to check wallet connection status
    const checkWalletConnection = async () => {
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            
            // Set connection status to true
            setIsConnected(true);
            setErrorMessage('');
        } catch (error) {
            // Handle errors during wallet connection
            setErrorMessage('Failed to connect wallet: ' + error.message);
            console.error('Wallet connection error:', error);
        }
    };

    // Effect to check connection status on component mount
    useEffect(() => {
        const checkConnection = async () => {
            if (window.ethereum) {
                // Check if there are accounts connected
                const accounts = await web3.eth.getAccounts();
                if (accounts.length > 0) {
                    setIsConnected(true);
                } else {
                    setIsConnected(false);
                }
            } else {
                setErrorMessage('Ethereum provider not found. Please install MetaMask.');
            }
        };

        checkConnection();
    }, [web3]);

    return (
        <div>
            <h1>Sorta Finance App</h1>
            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
            <div>
                {isConnected ? (
                    <p>Wallet is connected!</p>
                ) : (
                    <button onClick={checkWalletConnection}>Connect Wallet</button>
                )}
            </div>
        </div>
    );
};

// Export the SortaFinanceApp component
export default SortaFinanceApp;
```
