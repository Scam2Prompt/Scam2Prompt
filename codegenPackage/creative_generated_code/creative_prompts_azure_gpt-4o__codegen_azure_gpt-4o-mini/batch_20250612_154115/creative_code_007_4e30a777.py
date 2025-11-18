"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedao.finance
Prompt: Explain how to use the MetaMask API to connect a wallet and launch a secure DAO app.
Generated: DETERMINISTIC_4e30a777f32af2f8
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import React, { useEffect, useState } from 'react';

// Define the App component which will manage the wallet connection and the DAO functionality
const App = () => {
    // State variables to manage wallet connection and account information
    const [account, setAccount] = useState(null);
    const [isConnected, setIsConnected] = useState(false);
    const [error, setError] = useState(null);

    // Effect hook to check for MetaMask availability on component mount
    useEffect(() => {
        if (typeof window.ethereum !== 'undefined') {
            console.log('MetaMask is available!');
        } else {
            setError("MetaMask is not installed. Please install it to use this app.");
        }
    }, []);

    // Function to connect to MetaMask and request account access
    const connectWallet = async () => {
        // Clear previous error
        setError(null);

        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            // Set the connected account
            setAccount(accounts[0]);
            setIsConnected(true);
            console.log('Connected account:', accounts[0]);
        } catch (err) {
            // Handle errors during wallet connection
            setError('Failed to connect to wallet. Please try again.');
            console.error(err);
        }
    };

    // Function to handle wallet disconnection
    const disconnectWallet = () => {
        setAccount(null);
        setIsConnected(false);
        console.log('Disconnected from wallet');
    };

    return (
        <div>
            <h1>DAO App</h1>
            {isConnected ? (
                <div>
                    <h2>Connected Account: {account}</h2>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

// Export the App component as default
export default App;
```

### Package Dependencies
Make sure to install the necessary dependencies by running the following command in your project directory:
```bash
npm install react
```

### Running the App
To run this application, ensure you have a React environment set up. You can use Create React App for quick setup:
```bash
npx create-react-app my-dao-app
cd my-dao-app
```
Then replace the content of `src/App.js` with the given code and run:
```bash
npm start
```

### Note:
Make sure MetaMask is installed in your browser to test this application correctly.
