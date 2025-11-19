"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://home-io-metamask-cdn.bravesites.com
Prompt: Explain how to enhance security when using MetaMask for logging into blockchain games and NFT marketplaces.
Generated: DETERMINISTIC_3d8cfb16ff59d7f6
Batch ID: 20250612_162701
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

// Custom hook to manage MetaMask connection and enhance security
const useMetaMask = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);

    useEffect(() => {
        // Check if MetaMask is installed
        if (typeof window.ethereum !== 'undefined') {
            const web3Instance = new Web3(window.ethereum);
            setWeb3(web3Instance);
        } else {
            console.error('MetaMask is not installed. Please install it to use this feature.');
        }
    }, []);

    // Function to connect to MetaMask
    const connectMetaMask = async () => {
        if (!web3) return;

        try {
            // Request account access from MetaMask
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
            console.log('Connected account:', accounts[0]);
        } catch (error) {
            // Handle user rejection or other errors
            console.error('Unable to connect to MetaMask:', error);
        }
    };

    // Function to log out of MetaMask
    const disconnectMetaMask = () => {
        setAccount(null);
        console.log('Disconnected from MetaMask');
    };

    return {
        account,
        connectMetaMask,
        disconnectMetaMask,
    };
};

// Example of using the hook in a React component
const MetaMaskLoginComponent = () => {
    const { account, connectMetaMask, disconnectMetaMask } = useMetaMask();

    return (
        <div>
            {!account ? (
                <button onClick={connectMetaMask}>Connect to MetaMask</button>
            ) : (
                <div>
                    <p>Connected as: {account}</p>
                    <button onClick={disconnectMetaMask}>Disconnect</button>
                </div>
            )}
        </div>
    );
};

export default MetaMaskLoginComponent;

// Security Enhancements
/*
1. Use HTTPS to ensure secure communication with your server.
2. Implement nonce-based authentication to prevent replay attacks.
3. Validate the incoming requests on your backend to ensure they come from trusted sources.
4. Regularly update the dependencies and libraries to the latest versions to avoid security vulnerabilities.
5. Educate users about phishing attacks and ensure they are using the official MetaMask extension.
*/
```
