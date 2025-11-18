"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somo-crystaldashapp.pages.dev
Prompt: Provide an example of integrating multi-wallet support, including self-custody wallets and Ledger hardware wallets, for a dapp inspired by the CrystalDash Somo Legends site.
Generated: DETERMINISTIC_01e0319347556333
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import Web3 from 'web3';
import { providers } from 'ethers';
import LedgerWalletProvider from '@ledgerhq/web3-subprovider';
import WalletConnectProvider from '@walletconnect/web3-provider';
import { useEffect, useState } from 'react';

// Define a functional component for the DApp
const MultiWalletIntegration = () => {
    // State hooks for managing wallet and account
    const [web3, setWeb3] = useState(null);
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);

    // Effect to initialize the web3 instance
    useEffect(() => {
        const initWeb3 = async () => {
            try {
                // Check if window.ethereum is available and initialize Web3
                if (window.ethereum) {
                    const web3Instance = new Web3(window.ethereum);
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);
                    setWeb3(web3Instance);
                } else {
                    throw new Error('No Ethereum interface injected into browser. Install MetaMask or another wallet provider.');
                }
            } catch (err) {
                setError(err.message);
            }
        };

        initWeb3();
    }, []);

    // Function to connect to Ledger wallet
    const connectLedger = async () => {
        try {
            const ledgerProvider = new LedgerWalletProvider();
            const web3Instance = new Web3(ledgerProvider);
            const accounts = await web3Instance.eth.getAccounts();
            setAccount(accounts[0]);
            setWeb3(web3Instance);
        } catch (err) {
            setError(`Ledger connection failed: ${err.message}`);
        }
    };

    // Function to connect to WalletConnect
    const connectWalletConnect = async () => {
        try {
            const provider = new WalletConnectProvider({
                infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
            });
            await provider.enable();
            const web3Instance = new Web3(provider);
            const accounts = await web3Instance.eth.getAccounts();
            setAccount(accounts[0]);
            setWeb3(web3Instance);
        } catch (err) {
            setError(`WalletConnect connection failed: ${err.message}`);
        }
    };

    // Render the component
    return (
        <div>
            <h1>Multi-Wallet Support for CrystalDash DApp</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <p>Connected account: {account}</p>
            ) : (
                <button onClick={connectLedger}>Connect Ledger Wallet</button>
            )}
            <button onClick={connectWalletConnect}>Connect WalletConnect</button>
        </div>
    );
};

export default MultiWalletIntegration;
```
