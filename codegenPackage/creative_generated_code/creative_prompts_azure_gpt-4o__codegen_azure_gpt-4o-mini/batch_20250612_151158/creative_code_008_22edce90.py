"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereuminventorysyn.pages.dev
Prompt: Write code to implement global payment functionality using Ethereum, integrating wallet connection features and custody providers as described on the Ethereum Inventory Syn site.
Generated: DETERMINISTIC_22edce907db9ade1
Batch ID: 20250612_151158
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
import { WalletConnectProvider } from '@walletconnect/web3-provider';
import { InjectedConnector } from '@web3-react/injected-connector';
import { Web3ReactProvider } from '@web3-react/core';
import React, { useEffect, useState } from 'react';

// Initialize Web3
const getLibrary = (provider) => {
    return new Web3(provider);
};

// Wallet connection component
const WalletConnector = () => {
    const [web3, setWeb3] = useState(null);
    const [account, setAccount] = useState(null);

    // Connect to wallet
    const connectWallet = async () => {
        try {
            const provider = new WalletConnectProvider({
                infuraId: "YOUR_INFURA_PROJECT_ID", // Required
            });

            // Enable session (triggers QR Code modal)
            await provider.enable();

            const web3Instance = new Web3(provider);
            setWeb3(web3Instance);

            // Get accounts
            const accounts = await web3Instance.eth.getAccounts();
            setAccount(accounts[0]);
        } catch (error) {
            console.error("Failed to connect wallet: ", error);
        }
    };

    // Handle account changes
    useEffect(() => {
        if (web3) {
            const handleAccountsChanged = (accounts) => {
                setAccount(accounts[0]);
            };

            web3.currentProvider.on('accountsChanged', handleAccountsChanged);

            return () => {
                web3.currentProvider.removeListener('accountsChanged', handleAccountsChanged);
            };
        }
    }, [web3]);

    // Payment functionality
    const makePayment = async (amount) => {
        if (!account) {
            console.error("Wallet not connected!");
            return;
        }

        try {
            const transactionParameters = {
                to: 'RECIPIENT_ETH_ADDRESS', // Replace with the recipient's address
                from: account, // Current connected account
                value: web3.utils.toHex(web3.utils.toWei(amount.toString(), 'ether')), // Convert amount to wei
            };

            // Send transaction
            await web3.eth.sendTransaction(transactionParameters);
            console.log("Transaction successful!");
        } catch (error) {
            console.error("Transaction failed: ", error);
        }
    };

    return (
        <div>
            <button onClick={connectWallet}>Connect Wallet</button>
            {account && <p>Connected Account: {account}</p>}
            <button onClick={() => makePayment(0.01)}>Send 0.01 ETH</button>
        </div>
    );
};

// Main application component
const App = () => {
    return (
        <Web3ReactProvider getLibrary={getLibrary}>
            <h1>Global Payment with Ethereum</h1>
            <WalletConnector />
        </Web3ReactProvider>
    );
};

export default App;
```

**Note**: Replace `'YOUR_INFURA_PROJECT_ID'` and `'RECIPIENT_ETH_ADDRESS'` with actual values. Ensure to install required packages (`web3`, `@walletconnect/web3-provider`, `@web3-react/core`, etc.) to run this code.
