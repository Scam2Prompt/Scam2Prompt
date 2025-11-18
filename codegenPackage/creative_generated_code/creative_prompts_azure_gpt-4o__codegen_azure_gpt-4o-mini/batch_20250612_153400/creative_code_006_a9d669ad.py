"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica19.vercel.app
Prompt: Write code to integrate wallet authentication for Solana, Ethereum, and Polygon networks into a web application, inspired by the Matrica login functionality.
Generated: DETERMINISTIC_a9d669adf72d4498
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries for wallet integration
import { useEffect, useState } from 'react';
import Web3 from 'web3'; // for Ethereum and Polygon
import { Connection, clusterApiUrl } from '@solana/web3.js'; // for Solana
import WalletConnectProvider from '@walletconnect/web3-provider'; // for WalletConnect
import { InjectedConnector } from '@web3-react/injected-connector'; // for MetaMask

// Create a connector for Ethereum and Polygon
const injected = new InjectedConnector({ supportedChainIds: [1, 137] }); // Mainnet Ethereum and Polygon

const WalletAuth = () => {
    const [account, setAccount] = useState(null);
    const [network, setNetwork] = useState(null);

    // Function to connect to Ethereum or Polygon
    const connectWallet = async () => {
        try {
            // Check if MetaMask is installed
            if (window.ethereum) {
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                setAccount(accounts[0]);
                determineNetwork(); // Determine the network after connecting
            } else {
                throw new Error('MetaMask is not installed');
            }
        } catch (error) {
            console.error('Connection Error: ', error);
            alert('Failed to connect wallet. Please try again.');
        }
    };

    // Function to determine the current network
    const determineNetwork = async () => {
        try {
            const web3 = new Web3(window.ethereum);
            const currentChainId = await web3.eth.getChainId();
            switch (currentChainId) {
                case 1:
                    setNetwork('Ethereum Mainnet');
                    break;
                case 137:
                    setNetwork('Polygon Mainnet');
                    break;
                default:
                    setNetwork('Unsupported Network');
            }
        } catch (error) {
            console.error('Network Detection Error: ', error);
        }
    };

    // Function to connect to Solana
    const connectSolanaWallet = async () => {
        try {
            const provider = window.solana;
            if (provider) {
                const response = await provider.connect();
                setAccount(response.publicKey.toString());
                setNetwork('Solana');
            } else {
                throw new Error('Solana Wallet is not installed');
            }
        } catch (error) {
            console.error('Solana Connection Error: ', error);
            alert('Failed to connect Solana wallet. Please try again.');
        }
    };

    // Effect to handle wallet connection on component mount
    useEffect(() => {
        // Optionally, check if a wallet is already connected
        if (window.ethereum) {
            window.ethereum.on('accountsChanged', (accounts) => {
                if (accounts.length > 0) {
                    setAccount(accounts[0]);
                } else {
                    setAccount(null);
                    setNetwork(null);
                }
            });
        }
    }, []);

    return (
        <div>
            <h1>Wallet Authentication</h1>
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <p>Network: {network}</p>
                </div>
            ) : (
                <div>
                    <button onClick={connectWallet}>Connect Ethereum/Polygon Wallet</button>
                    <button onClick={connectSolanaWallet}>Connect Solana Wallet</button>
                </div>
            )}
        </div>
    );
};

export default WalletAuth;
```

This code provides a React component for integrating wallet authentication for Solana, Ethereum, and Polygon networks, ensuring to handle errors and provide a user-friendly experience.
