"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write code to integrate MetaMask into a DApp using Web3 React, referencing the connection methods described in the Dapp Starter template.
Generated: DETERMINISTIC_b023caa9a9cc0d77
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { Button } from 'reactstrap'; // Assuming reactstrap is being used for UI components

// Define the main App component
const App = () => {
    // Declare state variables for the Web3 instance and user account
    const [web3, setWeb3] = useState(null);
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);

    // UseEffect hook to initialize Web3 and check for MetaMask
    useEffect(() => {
        const initWeb3 = async () => {
            try {
                // Check if MetaMask is installed
                if (window.ethereum) {
                    // Create a Web3 instance with the provided provider
                    const web3Instance = new Web3(window.ethereum);
                    setWeb3(web3Instance);

                    // Request account access if needed
                    await window.ethereum.request({ method: 'eth_requestAccounts' });

                    // Get the user's accounts
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);
                } else {
                    throw new Error('MetaMask is not installed. Please install MetaMask and try again.');
                }
            } catch (err) {
                // Handle any errors that occur during initialization
                console.error(err);
                setError(err.message);
            }
        };

        // Call the initWeb3 function to set up Web3
        initWeb3();
    }, []);

    // Function to handle account change
    const handleAccountChange = async () => {
        if (web3) {
            const accounts = await web3.eth.getAccounts();
            setAccount(accounts[0]);
        }
    };

    // Event listener for account changes
    useEffect(() => {
        if (window.ethereum) {
            window.ethereum.on('accountsChanged', handleAccountChange);
        }

        // Cleanup event listener on component unmount
        return () => {
            if (window.ethereum) {
                window.ethereum.removeListener('accountsChanged', handleAccountChange);
            }
        };
    }, [web3]);

    return (
        <div className="App">
            <h1>MetaMask DApp Integration</h1>
            {error && <div className="error">{error}</div>}
            {account ? (
                <div>
                    <p>Connected account: {account}</p>
                </div>
            ) : (
                <Button color="primary" onClick={() => window.ethereum.request({ method: 'eth_requestAccounts' })}>
                    Connect MetaMask
                </Button>
            )}
        </div>
    );
};

export default App;
```
