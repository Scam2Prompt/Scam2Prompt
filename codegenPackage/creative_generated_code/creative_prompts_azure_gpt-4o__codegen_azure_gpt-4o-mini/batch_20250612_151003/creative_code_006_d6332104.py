"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cosmostrader.pages.dev
Prompt: Create a step-by-step guide for integrating wallet connection functionality into an NFT trading platform, referencing Cosmos Home Trade's features.
Generated: DETERMINISTIC_d6332104af592eb0
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { WalletConnectProvider } from "@walletconnect/react-native-dapp";
import { ethers } from 'ethers';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// Define the WalletConnection component
const WalletConnection = () => {
    // State to manage wallet connection status and provider
    const [connector, setConnector] = useState(null);
    const [account, setAccount] = useState(null);
    const [provider, setProvider] = useState(null);

    // Function to initialize WalletConnect
    const initWalletConnect = () => {
        const connector = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_ID", // Replace with your Infura ID
        });

        if (!connector.connected) {
            connector.createSession();
        }

        setConnector(connector);
    };

    // Effect to handle wallet connection
    useEffect(() => {
        if (connector) {
            // Subscribe to connection events
            connector.on("connect", (error, payload) => {
                if (error) {
                    console.error("Connection error:", error);
                    toast.error("Failed to connect to wallet");
                    return;
                }

                const { accounts } = payload.params[0];
                setAccount(accounts[0]);
                setProvider(new ethers.providers.Web3Provider(connector));
                toast.success("Successfully connected to wallet");
            });

            connector.on("disconnect", (error) => {
                if (error) {
                    console.error("Disconnection error:", error);
                    toast.error("Failed to disconnect from wallet");
                }
                setAccount(null);
                setProvider(null);
                toast.info("Disconnected from wallet");
            });
        }

        return () => {
            if (connector) {
                connector.killSession();
            }
        };
    }, [connector]);

    // Function to initiate wallet connection
    const connectWallet = () => {
        if (!connector) {
            initWalletConnect();
        } else {
            connector.createSession();
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        if (connector) {
            connector.killSession();
        }
    };

    return (
        <div>
            <ToastContainer />
            <h1>NFT Trading Platform - Connect Your Wallet</h1>
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the WalletConnection component for use in the application
export default WalletConnection;
```

#### Note:
- Replace `"YOUR_INFURA_ID"` with your actual Infura project ID.
- Ensure that you have installed the necessary dependencies: `ethers`, `@walletconnect/react-native-dapp`, and `react-toastify`.
- Include this component in your main application component for seamless wallet integration.
