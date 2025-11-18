"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheemspet.web.app
Prompt: Create a web application that mimics the functionality of Cheemsverse, allowing users to connect their wallets and view token supply details, burned tokens, and current supply. Use React for the frontend and Web3.js for wallet integration.
Generated: DETERMINISTIC_532372dd7a9d91bb
Batch ID: 20250612_153812
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

// Smart contract ABI (replace with the actual ABI)
const contractABI = [
    // ... your contract ABI goes here
];

// Smart contract address (replace with the actual contract address)
const contractAddress = '0xYourContractAddressHere';

// Main application component
const CheemsverseApp = () => {
    const [account, setAccount] = useState('');
    const [tokenSupply, setTokenSupply] = useState(0);
    const [burnedTokens, setBurnedTokens] = useState(0);
    const [currentSupply, setCurrentSupply] = useState(0);
    const [web3, setWeb3] = useState(null);
    const [contract, setContract] = useState(null);

    // Effect to set up web3 and contract
    useEffect(() => {
        const initWeb3 = async () => {
            try {
                // Check if MetaMask is installed
                if (window.ethereum) {
                    const web3Instance = new Web3(window.ethereum);
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);
                    setWeb3(web3Instance);

                    // Initialize contract
                    const contractInstance = new web3Instance.eth.Contract(contractABI, contractAddress);
                    setContract(contractInstance);

                    // Fetch token details
                    await fetchTokenDetails(contractInstance);
                } else {
                    alert('Please install MetaMask!');
                }
            } catch (error) {
                console.error('Error initializing web3:', error);
            }
        };

        initWeb3();
    }, []);

    // Function to fetch token details
    const fetchTokenDetails = async (contractInstance) => {
        try {
            const totalSupply = await contractInstance.methods.totalSupply().call();
            const burned = await contractInstance.methods.burnedTokens().call();
            const current = totalSupply - burned;

            setTokenSupply(totalSupply);
            setBurnedTokens(burned);
            setCurrentSupply(current);
        } catch (error) {
            console.error('Error fetching token details:', error);
        }
    };

    return (
        <div style={styles.container}>
            <h1>Cheemsverse Token Dashboard</h1>
            <p>Connected Account: {account || 'Not connected'}</p>
            <div style={styles.infoContainer}>
                <h2>Token Supply Details</h2>
                <p>Total Supply: {tokenSupply}</p>
                <p>Burned Tokens: {burnedTokens}</p>
                <p>Current Supply: {currentSupply}</p>
            </div>
        </div>
    );
};

// Basic styles for the application
const styles = {
    container: {
        textAlign: 'center',
        padding: '20px',
        fontFamily: 'Arial, sans-serif',
        backgroundColor: '#f4f4f4',
        borderRadius: '8px',
        boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
        margin: 'auto',
        maxWidth: '600px',
    },
    infoContainer: {
        marginTop: '20px',
        padding: '10px',
        backgroundColor: '#fff',
        borderRadius: '5px',
        boxShadow: '0 0 5px rgba(0, 0, 0, 0.1)',
    },
};

// Export the main component for rendering
export default CheemsverseApp;
```

### Instructions for Usage:
1. Replace the `contractABI` placeholder with the actual ABI of the smart contract.
2. Update the `contractAddress` with the actual address of the deployed contract.
3. Ensure you have MetaMask installed and configured in your browser.
4. Use this component in a React application, or create a new React app using Create React App and replace the content of `App.js` with the above code.
